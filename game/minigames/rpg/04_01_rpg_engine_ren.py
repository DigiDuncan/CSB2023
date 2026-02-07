"""
CSB2023 RPG engine
"""
from __future__ import annotations

"""renpy
rpy python annotations
python early in RPG:
"""

from dataclasses import dataclass
from queue import Queue
from typing import Protocol, Callable, Concatenate, Any, Self
from functools import wraps
from collections.abc import Sequence
from enum import StrEnum, IntFlag, auto

# |---- UTIL ----|

# https://stackoverflow.com/questions/5189699/how-to-make-a-class-property
class classproperty[V]:
    def __init__(self, f: Callable[..., V]):
        self.f = f

    def __get__(self, _, owner: type):
        return self.f(owner)

# TODO:
# - Effect messages, they can be done in the effect functions, but this excludes when they decay due to duration
# - Linking with the screen / displayables
# - Reimplimenting all the content in the game
# - all the todos below

type Displayable = renpy.display.core.Displayable
Image = renpy.display.im.Image
random = renpy.random


# |---- RPG ENGINE ----|

# -- CONSTANTS --

CRIT_CHANCE = 5.0 / 100.0
DAMAGE_INDICATOR_TIME = 1.0

UNKNOWN_FIELD = Image("gui/rpg/unknown_field_sprite.png")
UNKNOWN_PORTRAIT = Image("gui/rpg/portraits/unknown.png")

# -- STR EUMS --

class CharacterStat(StrEnum):
    HIT_POINTS = "hp"
    ATTACK = "attack"
    DEFENSE = "defense"
    ACCURACY = "accuracy"

class CharacterFlag(IntFlag):
    NOTHING = 0
    ALLY = auto()
    ENEMY = auto()
    UCN = auto()
    UCN_ALLY = UCN | ALLY
    UCN_ENEMY = UCN | ENEMY

class AttackType(IntFlag):
    NOTHING = 0
    DAMAGE = auto()
    HEAL = auto()
    BUFF = auto()
    DEBUFF = auto()
    AOE = auto()
    EFFECT = auto()
    COMBO = auto()
    SACRIFICE = auto() # TODO: add to AI

class IndicatorType(StrEnum):
    HP = "hp"
    DEF = "def"
    ATK = "atk"
    ACC = "acc"

class TargetType(StrEnum):
    ALL = "all"
    ENEMY = "enemy"
    ALLY = "ally"
    SELF = "self"

class AIFocus(StrEnum):
    STRONG = "strong"
    WEAK = "weak"
    NONE = "none"

# -- Constant Data Objects --

# This decorator enables attack function creators to set the attack type,
# and Attack creators to set the options neatly.

class AttackFunc:

    def __init__(self, typ: AttackType, func: Callable[..., Any], options: dict[str, Any]):
        self.type: AttackType = typ
        self.func: Callable[..., Any] = func
        self.options: dict[str, Any] = options

    @classmethod
    def predefine(cls, typ: AttackType = AttackType.NOTHING):
        """
        predefine allows Attack creators to iteratively create an Attack.

        The first call to predefine passes in the type of the attack and returns the decorator wrapper
        the decorator wrapper then collects the function and returns the collect options function
        the collect options function is used by the Attack definers to set the options for the attack
        this returns the final AttackFunc used by the RPG.

        Args:
            typ (AttackType, optional): The type of the attack used for AI decision making. Defaults to AttackType.NOTHING.

        Returns:
            Callable[..., Self]: A wrapper for collecting the function.
        """
        def wrapper[**P](func: Callable[Concatenate[Encounter, Fighter, tuple[Fighter, ...], P], Any]) -> Callable[P, Self]:
            @wraps(func)
            def collect_options(*_: P.args, **kwds: P.kwargs) -> Self:
                return cls(typ, func, kwds)
            return collect_options
        return wrapper

    def __call__(self, encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]) -> Any:
        return self.func(encounter, fighter, targets, **self.options)

attack_def = AttackFunc.predefine

# The decorator also precalculates if an attack is a debuff/buff so no overrides have to be used
class StatAttackFunc(AttackFunc):
    def __init__(self, typ: AttackType, func: Callable[..., Any], options: dict[str, Any]):
        typ = typ | (AttackType.BUFF if options.get("mult", 1.0) < 1.0 else AttackType.DEBUFF)
        super().__init__(typ, func, options)

stat_attack_def = StatAttackFunc.predefine


class Attack:
    """
    An Attack defines on of the possible actions a character can do on their turn.
    It does not include any of the data that is encounter dependant. The type of
    the attack is determined automatically so there shouldn't be a reason to override
    it.

    """

    def __init__(
            self,
            name: str,
            description: str,
            func: AttackFunc,
            targets: TargetType = TargetType.ENEMY,
            target_count: int = 1,
            cooldown: int = 0,
            accuracy: int = 80,
            start_used: bool = False,
            *,
            typ: AttackType | None = None,
        ):

        if typ is None:
            typ = func.type
            if targets != TargetType.SELF and target_count > 1:
                # Automatically add AOE because the attack function
                # generally works for any number of attackers
                typ = typ | AttackType.AOE

        self.name: str = name
        self.description: str = description
        self.type: AttackType = typ # type of attack for AI

        self.func: AttackFunc = func # the function which applies the effects of the attack
        self.targets: TargetType = targets # what group of fighters to attack
        self.target_count: int = target_count # how many enemies to target
        self.cooldown: int = cooldown # how many turns to wait on the cool down
        self.accuracy: int = accuracy # percent change of hitting witht the attack
        self.start_used: bool = start_used # whether to start counting down from the beginning of the fight

    @property
    def options(self) -> dict[str, Any]:
        return self.func.options

    def __str__(self) -> str:
        return f"<Attack {self.name}>"

    def __repr__(self) -> str:
        return self.__str__()

class ComboAttack:
    """
    A ComboAttack has multiple attacks
    that work together.

    TODO: add ability to choose different targets for different attacks
    """

    def __init__(
            self,
            name: str,
            description: str,
            attacks: Sequence[Attack],
            targets: TargetType | None = None,
            target_count: int | None = None,
            cooldown: int | None = None,
            accuracy: int | None = None,
            start_used: bool | None = None,
            shared_targets: bool = False, # TODO: use to allow for mixed targetting
            *,
            typ: AttackType | None = None,
            ):
        self.name: str = name
        self.description: str = description
        if typ is None:
            typ = AttackType.COMBO
            # TODO: Merge types of attacks.

        self.type: AttackType = typ

        self.attacks = attacks # What attacks to run through

        # Same as normal Attack
        self.targets: TargetType = self.attacks[0].targets if targets is None else targets
        self.target_count: int = self.attacks[0].target_count if target_count is None else target_count
        self.cooldown: int = self.attacks[0].cooldown if cooldown is None else cooldown
        self.accuracy: int = self.attacks[0].accuracy if accuracy is None else accuracy
        self.start_used: bool = self.attacks[0].start_used if start_used is None else start_used

    def func(self, encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
        for attack in self.attacks:
            attack.func(encounter, fighter, targets)

    @property
    def options(self) -> dict[str, Any]:
        # Options is a bit unclear for combo it could also be a mix of all the options of the sub-attacks?
        return {}

    def __str__(self) -> str:
        return f"<ComboAttack {self.name} ({self.attacks})>"

    def __repr__(self) -> str:
        return self.__str__()

class _EffectCollectFunc[S, **P](Protocol):
    def __call__(self, message: str | None = None, *args: P.args, **kwds: P.kwargs) -> S: ...

class EffectFunc[R]:

    def __init__(self, message: str | None, func: Callable[..., Any], options: dict[str, Any]):
        self.message: str | None = message
        self.func: Callable[..., Any] = func
        self.options: dict[str, Any] = options

    @classmethod
    def predefine[**P](cls, func: Callable[Concatenate[Encounter, Fighter, Fighter, P], R]) -> _EffectCollectFunc[Self, P]:
        @wraps(func)
        def collect_options(message: str | None = None, *_: P.args, **kwds: P.kwargs) -> Self:
            return cls(message, func, kwds)
        return collect_options

    def __call__(self, encounter: Encounter, source: Fighter, target: Fighter, overrides: dict[str, Any] | None = None) -> Any:
        options = self.options if not overrides else (self.options | overrides)
        return self.func(encounter, source, target, **options)


apply_def = EffectFunc[Any].predefine
update_def = EffectFunc[Any].predefine
resolved_def = EffectFunc[bool].predefine

class Effect:
    """
    An Effect happens over multiple turns and
    is controlled by the encounter. Attacks
    and Fighters can spawn effects, and
    encounters can have passive background
    effects.
    """

    def __init__(
            self,
            name: str,
            description: str,
            positive: bool,
            icon: Displayable | None = None,
            duration: int = 0,
            apply: EffectFunc[Any] | str | None = None,
            update: EffectFunc[Any] | str | None = None,
            resolved: EffectFunc[bool] | str | None = None,
            ):
        self.name: str = name
        self.description: str = description
        self.icon: Displayable = icon # Icon to show
        self.positive: bool = positive # whether the effect is considered helpful for 'cleanse' effects
        self.duration: int = duration # How many turns does the effect last? If 0 then forever.

        # What happens when the effect is applied
        self.apply: EffectFunc[Any] | None = None
        self.apply_message: str | None = None
        if isinstance(apply, str):
            self.apply_message = apply
        elif apply is not None:
            self.apply = apply
            self.apply_message = apply.message

        # What happens every turn the effect is applied
        self.update: EffectFunc[Any] | None = None
        self.update_message: str | None = None
        if isinstance(update, str):
            self.update_message = update
        elif update is not None:
            self.update = update
            self.update_message = update.message

        # Should the effect end other than the duration ending
        self.resolved: EffectFunc[bool] | None = None
        self.resolved_message: str | None = None
        if isinstance(resolved, str):
            self.resolved_message = resolved
        elif resolved is not None:
            self.resolved = resolved
            self.resolved_message = resolved.message


class AI:
    """
    The logic that decides what a fighter will
    do each turn. Uses the information provided
    by the encounter to decide on an Attack.
    """
    def __init__(self,
            name: str,
            heal_chance: float = 0.33,
            heal_threshold: float = 0.50,
            aggression: float = 1.0,
            crowd_control: float = 1.0,
            tacticity: float = 1.0,
            focus: AIFocus = AIFocus.NONE,
            preferred_targets: Sequence[str] = (),
            preference_weight: float = 2.0
        ) -> None:
        self.name: str = name
        self.heal_chance: float = heal_chance  # Skew towards healing attacks
        self.heal_threshold: float = heal_threshold  # When should I heal
        self.aggression: float = aggression  # Big bad hit things
        self.crowd_control: float = crowd_control  # Favors AOE over Single
        self.tacticity: float = tacticity  # Debuffs and Buffs, aka the Pokemon strat
        self.focus: AIFocus = focus  # Target 'strong' or 'weak'
        self.preferred_targets: Sequence[str] = preferred_targets  # I wanna smack this boy in particular >:C
        self.preference_weight: float = preference_weight  # Multiplier how many more times likely to smack this boy

    def choose_attack(self, encounter: Encounter, subject: Fighter) -> FighterAttack | None:
        party = encounter.enemies if subject.enemy else encounter.allies
        enemies = encounter.allies if subject.enemy else encounter.enemies

        # Sort enemies by weak-first
        enemies = sorted(enemies, key = lambda x: (x.hit_points * (1.0 - (x.defense / 100.0))))

        encounter.send_debug(f"{subject.character.display_name}: Choosing an attack...", "AI.choose_attack", ai = self, subject = subject)

        available_attacks = tuple(a for a in subject.attacks if a.available)

        if len(available_attacks) == 0: # No attacks to chose?
            return None
        if len(available_attacks) == 1: # Only one attack to chose.
            return available_attacks[0]

        # Choose an attack.

        # Find minimum party health percentage
        min_health = min(fighter.hit_points/fighter.max_hp for fighter in party)
        # Roll a die if we should heal or not.
        heal_party = random.random() < self.heal_chance if min_health <= self.heal_threshold else False


        # If we should heal, make sure we only have healing attacks available.
        if heal_party:
            all_attacks = available_attacks
            available_attacks = [a for a in available_attacks if a.type & AttackType.HEAL]
            if self.name == "COPGUY_EX" and encounter.HEAL_EX is not None:
                available_attacks = [encounter.HEAL_EX]
            if len(available_attacks) == 0:
                available_attacks = all_attacks
        else:
            available_attacks = [a for a in available_attacks if not a.type & AttackType.HEAL]

        scores: list[float] = []
        # Weight attack likelyhood.
        for atk in available_attacks:
            score = 1.0
            if atk.type & AttackType.DAMAGE or atk.type & AttackType.AOE:
                score *= (self.aggression * atk.options.get("mult", 1.0))
            elif atk.type & AttackType.BUFF or atk.type & AttackType.DEBUFF or atk.type & AttackType.EFFECT:
                score *= self.tacticity
            if atk.type & AttackType.AOE:
                score *= self.crowd_control
            if heal_party:
                score *= atk.options.get("mult", 1)  # weight towards better heals
            scores.append(score)

        # Choose an attack.
        encounter.send_debug(f"{available_attacks}, {scores}", "AI.choose_attack", AI = self, subject = subject)
        return random.choices(available_attacks, weights = scores)[0]

    def __str__(self) -> str:
        return f"<AI {self.name}>"

    def __repr__(self) -> str:
        return self.__str__()


class Character: # TODO: Workshop -- I'd like fighter to be used by encounter, but character doesn't make sense if there are multiple of the same person
    """
    A Character (previously Fighter) is the decription
    of a fighter. This includes their name, attacks, etc
    and is used by the encounter to setup the fighters
    """

    def __init__(self, name: str, hp: int, defense: int, attack: int, attacks: Sequence[Attack | ComboAttack], accuracy: int = 100, ai: AI | None = None, display_name: str | None = None, portrait: Displayable | None = None, sprite: Displayable | None = None, traits: CharacterFlag = CharacterFlag.NOTHING):
        self.name: str = name
        self.display_name: str = display_name or name
        self.assigned_name: str | None = None
        self.traits: CharacterFlag = traits

        self.base_hp: int = hp # how much hp will the fighter start with, and what is their max hp
        self.base_def: int = defense # how much defense will the fighter start with
        self.base_atk: int = attack # how much attack will the fighter start with
        self.base_acc: int = accuracy # how accurate will the fighter start with

        self.attacks: tuple[Attack | ComboAttack, ...] = tuple(attacks) # What attacks can the character use
        self.base_ai: AI | None = ai # Default AI for character
        self.portrait: Displayable = portrait or UNKNOWN_PORTRAIT # What image should represent the character on the player's side
        self.sprite: Displayable = sprite or UNKNOWN_FIELD # What image should represent the character on the field side

    def clone(self, name: str, hp: int | None = None, defense: int | None = None, attack: int | None = None, attacks: Sequence[Attack | ComboAttack] | None = None, accuracy: int | None = None, ai: AI | None = None, display_name: str | None = None, portrait: Displayable | None = None, sprite: Displayable | None = None) -> Character:
        return Character(
            name,
            hp if hp is not None else self.base_hp,
            defense if defense is not None else self.base_def,
            attack if attack is not None else self.base_atk,
            attacks if attacks is not None else self.attacks,
            accuracy if accuracy is not None else self.base_acc,
            ai if ai is not None else self.base_ai,
            display_name if display_name is not None else self.display_name,
            portrait if portrait is not None else self.portrait,
            sprite if sprite is not None else self.sprite
        )

    def __set_name__(self, owner: type, name: str):
        self.assigned_name = name


# -- Encounter Unique Objects --

class Fighter:
    """
    The actual fighter that is used
    by the encounter. Has the traits
    that the original system needed
    deepcopied
    """

    def __init__(
            self,
            character: Character,
            enemy: bool,
            level: float = 1.0,
            ai: AI | None = None,
            hp_override: int | None = None,
            def_override: int | None = None,
            atk_override: int | None = None,
            acc_override: int | None = None
        ): # TODO: consider -- would it be worth to add a sprite override and a display_name override? (and a max_hp override)

        self.character: Character = character # The stat basis for the character
        self.enemy: bool = enemy # What team is the fighter on
        self.level: float = level # What level is the fighter? Was originally the scale passed in the encounter
        self.ai: AI | None = ai or character.base_ai # What AI does the fighter use. If none the encouter defers to the player

        self.max_hp: int = int(character.base_hp * level) # Maximum hitpoints of a character
        self.hit_points: int = int(level * (character.base_hp if hp_override is None else hp_override))

        self.base_def: int = int(level * (character.base_def if def_override is None else def_override)) # percect of incoming damage reduced
        self.defense: int = self.base_def
        self.base_atk: int = int(level * (character.base_atk if atk_override is None else atk_override)) # Base amount of damage fighter does
        self.attack: int = self.base_atk
        self.base_acc: int = int(level * (character.base_acc if acc_override is None else acc_override)) # Percent change for fighter to hit (usually 100%)
        self.accuracy: int = self.base_acc

        # The attacks this fighter can do, and when they can use them next
        self.attacks: tuple[FighterAttack, ...] = tuple(FighterAttack(attack) for attack in self.character.attacks)
        self.next_attack: FighterAttack | None = None
        self.next_targets: tuple[Fighter, ...] = ()

        self.effects: list[FighterEffect] = []

    def reset_effects(self):
        self.defense = self.base_def
        self.attack = self.base_atk
        self.accuracy = self.base_acc

    @property
    def portrait(self) -> Displayable:
        return self.character.portrait

    @property
    def sprite(self) -> Displayable:
        return self.character.sprite

    @property
    def dead(self) -> bool:
        return self.hit_points <= 0

    @property
    def name(self) -> str:
        return self.character.name

    @property
    def display_name(self) -> str:
        return self.character.display_name
    
    def set_next_attack(self, next_attack):
        self.next_attack = next_attack
    
    def set_next_targets(self, next_targets):
        self.next_targets = next_targets


class FighterAttack:
    """
    The tracker for when an attack can used
    by the figher that owns it
    """

    def __init__(self, attack: Attack | ComboAttack):
        self.attack: Attack | ComboAttack = attack

        self.used: bool = attack.start_used
        self.turns_until_available: int = 0 if not attack.start_used else attack.cooldown

    def use(self, encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]) -> None:
        self.turns_until_available = self.attack.cooldown
        self.attack.func(encounter, fighter, targets)

    @property
    def name(self) -> str:
        return self.attack.name

    @property
    def type(self) -> AttackType:
        return self.attack.type

    @property
    def options(self) -> dict[str, Any]:
        return self.attack.options

    @property
    def available(self) -> bool:
        return self.turns_until_available == 0


class FighterEffect:
    """
    The tracker for when an effect has been used
    each fighter has their own list of FighterEffects
    """
    def __init__(
            self,
            effect: Effect,
            source: Fighter,
            target: Fighter,
            start_turn: int,
            duration_override: int | None = None,
            overrides: dict[str, Any] | None = None
        ):
        self.effect: Effect = effect
        self.source: Fighter = source
        self.target: Fighter = target
        self.start_turn: int = start_turn
        self.duration = effect.duration if duration_override is None else duration_override

        self.apply_overrides: dict[str, Any] | None = None
        self.update_overrides: dict[str, Any] | None = None
        self.resolved_overrides: dict[str, Any] | None = None

        # In some cases the strength of the effect is modulated on a per-attack
        # basis. For example the BLEED effect has 3-4 different mult values.
        # This lets the attack function creators to use `update_mult` to override
        # BLEED's update function mult
        if overrides:
            if self.effect.apply:
                self.apply_overrides = {(name[6:] if name.startswith("apply_") else name): value for name, value in overrides.items() if not name.startswith("update_") and not name.startswith("resolved_")}
                if not self.apply_overrides:
                    self.apply_overrides = None
            if self.effect.update:
                self.update_overrides = {(name[7:] if name.startswith("update_") else name): value for name, value in overrides.items() if not name.startswith("apply_") and not name.startswith("resolved_")}
                if not self.update_overrides:
                    self.update_overrides = None
            if self.effect.resolved:
                self.resolved_overrides = {(name[9:] if name.startswith("resolved_") else name): value for name, value in overrides.items() if not name.startswith("apply_") and not name.startswith("update_")}
                if not self.resolved_overrides:
                    self.resolved_overrides = None

    @property
    def positive(self) -> bool:
        return self.effect.positive

    def get_apply_msg(self) -> str | None:
        if self.effect.apply_message is None:
            return
        return self.effect.apply_message.format(source=self.source.display_name, target=self.target.display_name)

    def get_tick_msg(self, resolved: bool) -> str | None:
        if resolved and self.effect.resolved_message is not None:
            return self.effect.resolved_message.format(source=self.source.display_name, target=self.target.display_name)
        if not resolved and self.effect.update_message is not None:
            return self.effect.update_message.format(source=self.source.display_name, target=self.target.display_name)
        return None

    def apply(self, encounter: Encounter) -> None:
        if self.effect.apply is None:
            return
        self.effect.apply(encounter, self.source, self.target, self.apply_overrides)

    def update(self, encounter: Encounter) -> None:
        if self.effect.update is None:
            return
        self.effect.update(encounter, self.source, self.target, self.update_overrides)

    def resolved(self, encounter: Encounter) -> bool:
        if self.duration != 0 and self.start_turn + self.duration <= encounter.turn + 1: # Add 1 as this means that effects that last 1 turn don't get two run_effects
            return True
        if self.effect.resolved is not None:
            return self.effect.resolved(encounter, self.source, self.target, self.resolved_overrides)
        return False


@dataclass
class Signal:
    pass

@dataclass
class MessageSignal(Signal):
    message: str

@dataclass
class CharacterSignal(Signal):
    message: str
    character: Fighter

@dataclass
class DebugSignal(Signal):
    message: str
    source: str
    details: dict[str, Any]

@dataclass
class AttackSignal(Signal):
    message: str
    attack: FighterAttack
    attacker: Fighter
    targets: tuple[Fighter, ...]

@dataclass
class EffectSignal(Signal):
    message: str
    effect: FighterEffect
    source: Fighter
    target: Fighter

@dataclass
class IndicatorSignal(Signal):
    target: Fighter
    typ: IndicatorType
    value: int | None = None

@dataclass
class EffectIndicatorSignal(Signal):
    target: Fighter
    typ: Effect
    value: int | None = None

class Signals: # Can't be an enum if we want the cool type mapping in match blocks
    BASE = Signal
    MESSAGE = MessageSignal
    CHARACTER = CharacterSignal
    DEBUG = DebugSignal
    ATTACK = AttackSignal
    EFFECT = EffectSignal
    INDICATOR = IndicatorSignal
    EFFECT_INDICATOR = EffectIndicatorSignal


class Encounter:
    """
    The master control class of an encounter.
    Attacks and Effects use the Encounter object
    to manipulate fighters.
    """
    DEFEND_ACTION: FighterAttack | None = None
    HEAL_EX: FighterAttack | None = None

    def __init__(self, fighters: Sequence[Fighter], background: Displayable, music: str, on_win: str, on_lose: str = "start", intro_text: str = "A challenger approaches!", initial_turn: int = 0):
        self.fighters: list[Fighter] = list(fighters)

        self.background: Displayable = background # Background image for fight
        self.music = music # background music
        self.on_win = on_win # scene to go to on win
        self.on_lose = on_lose # scene to go to on lose
        self.intro_text = intro_text # intro display text
        self.turn: int = initial_turn # current turn

        self.upcoming_attacks: list[tuple[Fighter, FighterAttack | None, tuple[Fighter, ...]]] = []
        self.signal_queue: Queue[Signal] = Queue()

    @property
    def allies(self) -> tuple[Fighter, ...]:
        return tuple(fighter for fighter in self.fighters if not fighter.enemy)

    @property
    def enemies(self) -> tuple[Fighter, ...]:
        return tuple(fighter for fighter in self.fighters if fighter.enemy)

    @property
    def turn_order(self) -> tuple[Fighter, ...]:
        return self.allies + self.enemies

    def get_team(self, enemy: bool = False) -> tuple[Fighter, ...]:
        return tuple(fighter for fighter in self.fighters if fighter.enemy == enemy)

    @property
    def won(self) -> bool | None:
        if len(self.allies) == 0:
            return False
        # This special exception occurs since DB is the only fighter to not be "on the field."
        elif len(self.allies) == 1 and self.allies[0].name == "DB05":
            return False
        elif len(self.enemies) == 0:
            return True
        else:
            return None

    # -- SIGNAL METHODS --

    def display_indicator(self, target: Fighter, typ: IndicatorType | Effect, amount: int | None = None):
        if isinstance(typ, IndicatorType):
            self.send_signal(IndicatorSignal(target, typ, amount))
            return
        self.send_signal(EffectIndicatorSignal(target, typ, amount))

    def send_debug(self, message: str, source: str, **kwds: Any):
        self.send_signal(DebugSignal(message, source, kwds))

    def send_message(self, message: str, character: Fighter | None = None):
        if character is None:
            self.send_signal(MessageSignal(message))
            return
        self.send_signal(CharacterSignal(message, character))

    def signal_attack(self, message: str, attack: FighterAttack, attacker: Fighter, targets: tuple[Fighter, ...]):
        self.send_signal(AttackSignal(message, attack, attacker, targets))

    def signal_effect(self, message: str, effect: FighterEffect):
        self.send_signal(EffectSignal(message, effect, effect.source, effect.target))

    def send_signal(self, message: Signal):
        self.signal_queue.put(message)

    def get_next_signal(self) -> Signal | None:
        if self.signal_queue.empty():
            return
        return self.signal_queue.get()

    def has_signals(self) -> bool:
        return not self.signal_queue.empty()

    # -- FIGHTER MANIPULATION METHODS --

    def defend_fighter(self, fighter: Fighter):
        fighter.next_attack = self.DEFEND_ACTION
        fighter.next_targets = (fighter,)

    def affect_fighter(self, fighter: Fighter):
        fighter.reset_effects()
        self.send_debug(f"{fighter.name} reset effects!", "Encounter.affect_fighter", fighter=fighter)
        for effect in fighter.effects:
            effect.apply(self)

    def damage_fighter(self, fighter: Fighter, damage: float, roll_crit: bool = False, ignore_armour: bool = False):
        # We generally only let the player's fighters roll crit.
        if roll_crit and random.random() <= CRIT_CHANCE:
            damage = damage * 1.5

        if not ignore_armour:
            fraction = fighter.defense / 100.0
            damage = damage * (1.0/16.0)**(fraction*fraction) # this makes it so 0 defense is 100%, 50 is 50%, but 100 isn't 0%

        fighter.hit_points -= int(damage)

        self.display_indicator(fighter, IndicatorType.HP, int(-damage))

    def heal_fighter(self, fighter: Fighter, amount: float, overheal: bool = False):
        fighter.hit_points += int(amount)
        if not overheal:
            fighter.hit_points = min(fighter.hit_points, fighter.max_hp)
        self.display_indicator(fighter, IndicatorType.HP, int(amount))

    def apply_effect(self, effect: Effect, source: Fighter, target: Fighter, duration_override: int | None = None, silent: bool = False, lazy: bool = False, **kwds: Any):
        new_effect = FighterEffect(effect, source, target, self.turn, duration_override, kwds)
        target.effects.append(new_effect)

        if not silent and (msg := new_effect.get_apply_msg()):
            self.signal_effect(msg, new_effect)

        if not lazy:
            self.affect_fighter(target)

    def remove_effect(self, effect: FighterEffect, silent: bool = False, lazy: bool = False):
        if effect.target not in self.fighters:
            self.send_debug("How did we get here??? (A non-existant/dead fighter has lost an effect)", "Encounter.remove_effect", effect = effect)
        effect.target.effects.remove(effect)

        if not silent and (msg := effect.get_tick_msg(resolved=True)):
            self.signal_effect(msg, effect)

        if not lazy:
            self.affect_fighter(effect.target)

    def cleanse_fighter(self, fighter: Fighter, negative: bool = True, positive: bool = True, silent: bool = False):
        for effect in tuple(fighter.effects):
            if (negative and not effect.positive) or (positive and effect.positive):
                fighter.effects.remove(effect)
        fighter.reset_effects()
        for fighter_effect in fighter.effects:
            fighter_effect.apply(self)

        if not silent:
            if positive and not negative:
                group = "all positive"
            elif negative and not positive:
                group = "all negative"
            else:
                group = "all"
            self.send_message(f"{fighter.display_name} had {group} effects removed!", fighter)

    def modify_fighter(self, fighter: Fighter, stat: CharacterStat, amount: float, permanent: bool = True):
        match stat:
            case CharacterStat.HIT_POINTS:
                old = fighter.hit_points
                new = int(old + amount)
                fighter.hit_points = new
                self.display_indicator(fighter, IndicatorType.HP, new - old)
                self.send_debug(f"Set {fighter.character.display_name}'s hit points to {fighter.hit_points}!", "Encounter.modify_fighter", stat=stat, old = old, new = new, prem = permanent)
            case CharacterStat.DEFENSE:
                old = fighter.defense
                new = int(old + amount)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defense = new
                self.display_indicator(fighter, IndicatorType.DEF, change)
                self.send_debug(f"Set {fighter.character.display_name}'s defense to {fighter.defense}!", "Encounter.modify_fighter", stat=stat, old = old, new = new, prem = permanent)
            case CharacterStat.ATTACK:
                old = fighter.attack
                new = max(5, int(old + amount))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
                self.send_debug(f"Set {fighter.character.display_name}'s attack to {fighter.attack}!", "Encounter.modify_fighter", stat=stat, old = old, new = new, prem = permanent)
            case CharacterStat.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old + amount)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)
                self.send_debug(f"Set {fighter.character.display_name}'s accuracy to {fighter.accuracy}!", "Encounter.modify_fighter", stat=stat, old = old, new = new, prem = permanent)

    def scale_fighter(self, fighter: Fighter, stat: CharacterStat, mult: float, permanent: bool = True):
        match stat:
            case CharacterStat.HIT_POINTS:
                old = fighter.hit_points
                new = int(old * mult)
                fighter.hit_points = new
                self.display_indicator(fighter, IndicatorType.HP, new - old)
                self.send_debug(f"Scaled {fighter.character.display_name}'s hit points by {mult}x!", "Encounter.scale_fighter", stat=stat, old = old, new = new, prem = permanent)
            case CharacterStat.DEFENSE:
                old = fighter.defense
                new = int(old * mult)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defense = new
                self.display_indicator(fighter, IndicatorType.DEF, change)
                self.send_debug(f"Scaled {fighter.character.display_name}'s defense by {mult}x!", "Encounter.scale_fighter", stat=stat, old = old, new = new, prem = permanent)
            case CharacterStat.ATTACK:
                old = fighter.attack
                new = max(5, int(old * mult))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
                self.send_debug(f"Scaled {fighter.character.display_name}'s attack by {mult}x!", "Encounter.scale_fighter", stat=stat, old = old, new = new, prem = permanent)
            case CharacterStat.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old * mult)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)
                self.send_debug(f"Scaled {fighter.character.display_name}'s accuracy by {mult}x!", "Encounter.scale_fighter", stat=stat, old = old, new = new, prem = permanent)

    # -- UTIL TARGETTING METHODS --

    def possible_targets(self, fighter: Fighter, attack: Attack | ComboAttack) -> tuple[Fighter, ...]:
        match attack.targets:
            case TargetType.SELF:
                return (fighter,)
            case TargetType.ALLY:
                return self.get_team(fighter.enemy)
            case TargetType.ALL:
                return tuple(self.fighters)
            case _:
                return self.get_team(not fighter.enemy)

    def choose_fighters(self, fighter: Fighter, attack: Attack | ComboAttack) -> tuple[Fighter, ...]:
        if fighter.ai is None:
            return ()

        # Return self when attack type is SELF, this may never happen depending on the AI
        if attack.targets == TargetType.SELF:
            return (fighter,)

        possible_targets = self.possible_targets(fighter, attack)

        # Shortcut and return all the possible targets when the count is 0
        if attack.target_count == 0:
            return possible_targets

        weights: list[float] = []
        for target in possible_targets:
            score = fighter.ai.preference_weight if target.character.display_name in fighter.ai.preferred_targets else 1.0
            # These may be wild numbers, but since they are all being changed by attack they will all be wild
            if fighter.ai.focus == AIFocus.STRONG:
                score *= target.attack
            elif fighter.ai.focus == AIFocus.WEAK:
                score /= target.attack
            weights.append(score)

        return tuple(random.choices(possible_targets, weights)[0] for _ in range(attack.target_count))

    # -- GAME LOOP METHODS --

    # These are seperate so that we can see the consequences of the player applying the defend effect etc
    def run_attacks(self):
        # run once every actor has chosen their next attack
        # Do the attack of every fighter and tick their attacks
        self.upcoming_attacks.clear()
        for fighter in self.turn_order:
            attack = fighter.next_attack
            targets = fighter.next_targets
            if attack is None:
                if fighter.ai is None:
                    # player has not picked an attack for this fighter so they just defend.
                    self.upcoming_attacks.append((fighter, self.DEFEND_ACTION, (fighter,)))
                    continue
                else:
                    # fighter has not picked attack and has an AI
                    if fighter.dead: # Dead AI fighters don't get to act
                        continue
                    attack = fighter.ai.choose_attack(self, fighter)
                    if attack is None:
                        self.upcoming_attacks.append((fighter, self.DEFEND_ACTION, (fighter,)))
                        continue
                    targets = self.choose_fighters(fighter, attack.attack)

            self.upcoming_attacks.append((fighter, attack, targets))

        # ! NOTE ! Because all attacks happen after the AI have chosen they behave differently in previous engine
        for fighter, attack, targets in self.upcoming_attacks:
            if attack is None:
                continue
            self.signal_attack(f"{fighter.display_name} used {attack.name}!", attack, fighter, targets)
            hit = random.random() <= (attack.attack.accuracy / 100.0 * fighter.accuracy / 100.0) and not fighter.dead

            if hit:
                attack.use(self, fighter, targets) # Actually use the fighter's attack so call `damage_fighters`
            else:
                self.send_message(f"{fighter.character.display_name} missed!", fighter)

            # print(f"[AI: {self.name}] {subject.name} uses {atk.name} on {sentence_join([t.name for t in subwho])}!")  # type: ignore
            # renpy.notify(f"{subject.display_name} uses {what.name} on {sentence_join([t.display_name for t in subwho])}!")  # type: ignore

    def run_effects(self):
        # Update the effects applied to every fighter.
        # This happens after all of the attacks are done for "fairness"
        # This does a bunch of repeated iteration, but at the number of
        # effects that will be applied it is fine.
        for fighter in self.turn_order:
            for effect in tuple(fighter.effects):
                effect.update(self)
                is_resolved = effect.resolved(self)
                if msg := effect.get_tick_msg(is_resolved):
                    self.signal_effect(msg, effect)
                if is_resolved:
                    self.remove_effect(effect, silent = True)
            self.affect_fighter(fighter)

    def cleanup_turn(self):
        for fighter in tuple(self.fighters):
            fighter.next_attack = None
            fighter.next_targets = ()
            # cool downs
            for attack in fighter.attacks:
                if attack.available:
                    continue
                attack.turns_until_available -= 1
                if attack.turns_until_available == 0:
                    self.send_message(f"{fighter.character.display_name}: {attack.name} now available!", fighter)
                else:
                    self.send_message(f"{fighter.character.display_name}: {attack.name} available in {attack.turns_until_available} turns!", fighter)

            if fighter.dead:
                self.send_message(f"{fighter.display_name} is dead!", fighter)
                self.fighters.remove(fighter)
                fighter.effects.clear()
        self.turn += 1

    def __str__(self) -> str:
        return f"<Encounter {self.allies} vs {self.enemies}>"

    def __repr__(self) -> str:
        return self.__str__()
