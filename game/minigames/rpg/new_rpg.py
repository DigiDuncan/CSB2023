from __future__ import annotations

from renpy.display.core import Displayable
from renpy.display.im import Image
from renpy import random, register_statement, jump

# This is the equivalent of a python early block in a .rpy file.
"""renpy
rpy python annotations
python early:
"""
from dataclasses import dataclass
from queue import Queue
from typing import Callable, Any, Self, Protocol
from functools import wraps
from collections.abc import Sequence
from enum import StrEnum, IntFlag, auto


# |---- UTIL ----|

# https://stackoverflow.com/questions/5189699/how-to-make-a-class-property
class classproperty(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner):
        return self.f(owner)

def override_random(new_random):
    global random
    random = new_random

# TODO:
# - Effect messages, they can be done in the effect functions, but this excludes when they decay due to duration
# - Linking with the screen / displayables
# - Reimplimenting all the content in the game
# - all the todos below

# |---- RPG ENGINE ----|

# -- CONSTANTS --

CRIT_CHANCE = 5.0 / 100.0
DAMAGE_INDICATOR_TIME = 1.0

UNKNOWN_FIELD = Image("game/gui/rpg/unknown_field_sprite.png")
UNKNOWN_PORTRAIT = Image("game/gui/rpg/portraits/unknown.png")

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


# class AttackType(StrEnum):
#     ATTACK = "attack"
#     HEAL = "heal"
#     BUFF = "buff"
#     DEBUFF = "debuff"
#     AOE = "aoe"
#    EFFECT = "effect" # previously confuse + DOT


class IndicatorType(StrEnum):
    HP = "hp"
    DEF = "def"
    ATK = "atk"
    ACC = "acc"
    CONFUSION = "confusion"

class MessageType(StrEnum):
    DEBUG = "debug"
    ATTACK = "attack"
    CHARACTER = "character"
    EFFECT = "effect"

class TargetType(StrEnum):
    ENEMY = "enemy"
    ALLY = "ally"
    ALL = "all"
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
    def predefine(cls, typ: AttackType = AttackType.NOTHING) -> Callable[..., Self]:
        def wrapper(func: Callable[..., Any]):
            @wraps(func)
            def collect_options(**kwds) -> Self:
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
        self.cooldown: int = self.attacks[0].cooldown if cooldown is None else cooldown
        self.accuracy: int = self.attacks[0].accuracy if accuracy is None else accuracy
        self.start_used: bool = self.attacks[0].start_used if start_used is None else start_used

        # Empty options dict
        self.options: dict[str, Any] = {}

    def func(self, encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], **kwds):
        for attack in self.attacks:
            attack.func(encounter, fighter, targets, **attack.options)

    def __str__(self) -> str:
        return f"<ComboAttack {self.name} ({self.attacks})>"

    def __repr__(self) -> str:
        return self.__str__()

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
            apply_func: Callable[..., Any] | None = None,
            update_func: Callable[..., Any] | None = None,
            decay_func: Callable[..., bool] | None = None,
            apply_options: dict[str, Any] | None = None,
            update_options: dict[str, Any] | None = None,
            decay_options: dict[str, Any] | None = None
            ):
        self.name: str = name
        self.description: str = description
        self.icon: Displayable = icon # Icon to show
        self.positive: bool = positive # whether the effect is considered helpful for 'cleanse' effects
        self.duration: int = duration # How many turns does the effect last? If 0 then forever.

        self.apply = apply_func # What happens when the effect is applied
        self.update = update_func # What happens every turn the effect is applied
        self.decay = decay_func # Should the effect end other than the duration ending

        self.apply_options = apply_options or {} # Additional arguments when applying the effect
        self.update_options = update_options or {} # Additonal arguments when updating the effect
        self.decay_options = decay_options or {} # Additional arguments when decaying the effect

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

        encounter.send_message(f"{subject.character.display_name}: Choosing an attack...", MessageType.DEBUG)

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
            if len(available_attacks) == 0:
                available_attacks = all_attacks
            if self.name == "COPGUY_EX":
                # TODO: add special exception for copguy_ex
                # available_attacks = [Attacks.HEAL_EX]
                return None
        else:
            available_attacks = [a for a in available_attacks if not a.type & AttackType.HEAL]

        scores = []
        # Weight attack likelyhood.
        for atk in available_attacks:
            score = 1.0
            if atk.type & AttackType.ATTACK or atk.type & AttackType.AOE:
                score *= (self.aggression * atk.func.options.get("mult", 1.0))
            elif atk.type & AttackType.BUFF or atk.type & AttackType.DEBUFF or atk.type & AttackType.EFFECT:
                score *= self.tacticity
            if atk.type & AttackType.AOE:
                score *= self.crowd_control
            if heal_party:
                score *= atk.func.options.get("mult", 1)  # weight towards better heals
            scores.append(score)

        # Choose an attack.
        encounter.send_message(f"{available_attacks}, {scores}", MessageType.DEBUG)
        return random.choices(available_attacks, weights = scores)[0]

        # print(f"[AI: {self.name}] {subject.name} uses {atk.name} on {sentence_join([t.name for t in subwho])}!")  # type: ignore
        # renpy.notify(f"{subject.display_name} uses {what.name} on {sentence_join([t.display_name for t in subwho])}!")  # type: ignore

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
        owner.characters[name] = self # Automatically add the Character to the dict for Characters.get
        if self.traits & CharacterFlag.ALLY:
            owner.allies[name] = self
        if self.traits & CharacterFlag.ENEMY:
            owner.enemies[name] = self
        if self.traits & CharacterFlag.UCN:
            owner.ucn[name] = self

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
    def dead(self) -> bool:
        return self.hit_points <= 0


class FighterAttack:
    """
    The tracker for when an attack can used
    by the figher that owns it
    """

    def __init__(self, attack: Attack):
        self.attack: Attack = attack

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
            fighter: Fighter,
            start_turn: int,
            duration_override: int | None = None,
            apply_override: dict[str, Any] | None = None,
            update_override: dict[str, Any] | None = None,
            decay_override: dict[str, Any] | None = None
        ):
        self.effect: Effect = effect
        self.fighter: Fighter = fighter
        self.start_turn: int = start_turn
        self.duration = effect.duration if duration_override is None else duration_override

        # Have to use | operator as it creates a new dict rather than updating in-place
        self.apply_options = self.effect.apply_options if apply_override is None else self.effect.apply_options | apply_override
        self.update_options = self.effect.update_options if update_override is None else self.effect.update_options | update_override
        self.decay_options = self.effect.decay_options if decay_override is None else self.effect.decay_options | decay_override

    def apply(self, encounter: Encounter) -> None:
        if self.effect.apply is None:
            return
        self.effect.apply(encounter, self.fighter, **self.apply_options)

    def update(self, encounter: Encounter) -> None:
        if self.effect.update is None:
            return
        self.effect.update(encounter, self.fighter, **self.update_options)

    def decay(self, encounter: Encounter) -> bool:
        if self.duration != 0 and self.start_turn + self.duration <= encounter.turn:
            return True
        if self.effect.decay is None:
            return False
        return self.effect.decay(encounter, self.fighter, **self.decay_options)

@dataclass
class Indicator:
    source: Fighter
    typ: IndicatorType
    value: int | None = None

@dataclass
class Message:
    message: str
    typ: MessageType

class Encounter:
    """
    The master control class of an encounter.
    Attacks and Effects use the Encounter object
    to manipulate fighters.
    """

    def __init__(self, fighters: Sequence[Fighter], background: Displayable, music: str, on_win: str, on_lose: str = "start", intro_text: str = "A challenger approaches!", initial_turn: int = 0):
        self.fighters: list[Fighter] = list(fighters)

        self.background: Displayable = background # Background image for fight
        self.music = music # background music
        self.on_win = on_win # scene to go to on win
        self.on_lose = on_lose # scene to go to on lose
        self.intro_text = intro_text # intro display text
        self.turn: int = initial_turn # current turn

        self.upcoming_attacks: list[tuple[FighterAttack, tuple[Fighter, ...]]] = []
        self.indicator_queue: Queue[Indicator] = Queue()
        self.message_queue: Queue[Message] = Queue()
        self.global_effects: list[Effect] = [] # TODO: better handle global effects because this just slowly fills up

        self._shared_defend_attack: FighterAttack = FighterAttack(Attacks.DEFEND)

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

    def display_indicator(self, target: Fighter, typ: IndicatorType, amount: int | None = None):
        self.indicator_queue.put(Indicator(target, typ, amount))

    def get_next_indicator(self) -> Indicator | None:
        if self.indicator_queue.empty:
            return
        return self.indicator_queue.get()

    def send_message(self, text: str, typ: MessageType):
        self.message_queue.put(Message(text, typ))

    def get_next_message(self) -> Message | None:
        if self.message_queue.empty:
            return
        return self.message_queue.get()

    def defend_fighter(self, fighter: Fighter):
        fighter.next_attack = self._shared_defend_attack
        fighter.next_targets = (fighter,)

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

    def apply_effect(self, effect: Effect, fighter: Fighter | None = None, duration_override: int | None = None, apply_override: dict[str, Any] | None = None, update_override: dict[str, Any] | None = None, decay_override: dict[str, Any] | None = None, silent: bool = False):
        if fighter is None: # apply to all fighters
            self.global_effects.append(effect)
            for fighter in self.fighters:
                self.apply_effect(effect, fighter, duration_override)
            return

        fighter.effects.append(FighterEffect(effect, fighter, self.turn, duration_override, apply_override, update_override, decay_override))

        if not silent:
            effect.fighter.reset_effects()
            for fighter_effect in effect.fighter.effects:
                fighter_effect.apply(self)

    def remove_effect(self, effect: FighterEffect, silent: bool = False):
        if effect.fighter not in self.fighters:
            self.send_message("How did we get here??? (A non-existant/dead fighter has lost an effect)", MessageType.DEBUG)
        effect.fighter.effects.remove(effect)

        if not silent:
            effect.fighter.reset_effects()
            for fighter_effect in effect.fighter.effects:
                fighter_effect.apply(self)

    def cleanse_fighter(self, fighter: Fighter, negative: bool = True, positive: bool = True):
        for effect in tuple(fighter.effects):
            if (negative and not effect.positive) or (positive and effect.positive):
                fighter.effects.remove(effect)
        fighter.reset_effects()
        for fighter_effect in effect.fighter.effects:
            fighter_effect.apply(self)

    def modify_fighter(self, fighter: Fighter, stat: CharacterStat, amount: float, permanent: bool = True):
        match stat:
            case CharacterStat.HIT_POINTS:
                old = fighter.hit_points
                new = int(old + amount)
                fighter.hit_points = new
                self.display_indicator(fighter, IndicatorType.HP, new - old)
                self.send_message(f"Set {fighter.character.display_name}'s hit points to {fighter.hit_points}!", MessageType.DEBUG)
            case CharacterStat.DEFENSE:
                old = fighter.defense
                new = int(old + amount)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defense = new
                self.display_indicator(fighter, IndicatorType.DEF, change)
                self.send_message(f"Set {fighter.character.display_name}'s defense to {fighter.defense}!", MessageType.DEBUG)
            case CharacterStat.ATTACK:
                old = fighter.attack
                new = max(5, int(old + amount))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
                self.send_message(f"Set {fighter.character.display_name}'s attack to {fighter.attack}!", MessageType.DEBUG)
            case CharacterStat.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old + amount)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)
                self.send_message(f"Set {fighter.character.display_name}'s accuracy to {fighter.accuracy}!", MessageType.DEBUG)

    def scale_fighter(self, fighter: Fighter, stat: CharacterStat, mult: float, permanent: bool = True):
        match stat:
            case CharacterStat.HIT_POINTS:
                old = fighter.hit_points
                new = int(old * mult)
                fighter.hit_points = new
                self.display_indicator(fighter, IndicatorType.HP, new - old)
                self.send_message(f"Scaled {fighter.character.display_name}'s hit points by {mult}x!", MessageType.DEBUG)
            case CharacterStat.DEFENSE:
                old = fighter.defense
                new = int(old * mult)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defense = new
                self.display_indicator(fighter, IndicatorType.DEF, change)
                self.send_message(f"Scaled {fighter.character.display_name}'s defense by {mult}x!", MessageType.DEBUG)
            case CharacterStat.ATTACK:
                old = fighter.attack
                new = max(5, int(old * mult))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
                self.send_message(f"Scaled {fighter.character.display_name}'s attack by {mult}x!", MessageType.DEBUG)
            case CharacterStat.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old * mult)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)
                self.send_message(f"Scaled {fighter.character.display_name}'s accuracy by {mult}x!", MessageType.DEBUG)

    def choose_fighters(self, fighter: Fighter, attack: Attack) -> tuple[Fighter, ...]:
        if fighter.ai is None:
            return ()

        # Return self when attack type is SELF, this may never happen depending on the AI
        if attack.targets == TargetType.SELF:
            return (fighter, )


        match attack.targets:
            case TargetType.ALLY:
                possible_targets = self.get_team(fighter.enemy)
            case TargetType.All:
                possible_targets = self.fighters
            case _:
                possible_targets = self.get_team(not fighter.enemy)

        # Shortcut and return all the possible targets when the count is 0
        if attack.target_count == 0:
            return possible_targets

        weights = []
        for target in possible_targets:
            score = fighter.ai.preference_weight if target.character.display_name in fighter.ai.preferred_targets else 1.0
            # These may be wild numbers, but since they are all being changed by attack they will all be wild
            if fighter.ai.focus == AIFocus.STRONG:
                score *= target.attack
            elif fighter.ai.focus == AIFocus.WEAK:
                score /= target.attack
            weights.append(score)

        return tuple(random.choices(possible_targets, weights)[0] for _ in range(attack.target_count))

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
                    continue # TODO: give fighter defend attack once it is created
                else:
                    if fighter.dead: # Dead AI fighters don't get to act
                        continue
                    # fighter has not picked attack and has an AI
                    attack = fighter.ai.choose_attack(self, fighter)
                    if attack is None:
                        self.upcoming_attacks.append((None, ()))
                        continue # Still no attack
                    targets = self.choose_fighters(fighter, attack)

                    self.send_message(f"[AI: {fighter.ai.name}] {fighter.character.name} uses {attack.name} on {", ".join(target.name for target in targets)}!", MessageType.DEBUG)

            self.upcoming_attacks.append((attack, targets))

        # ! NOTE ! Because all attacks happen after the AI have chosen they behave differently in previous engine
        for fighter, (attack, targets) in zip(self.turn_order, self.upcoming_attacks):
            if attack is None:
                continue
            hit = random.random <= (attack.attack.accuracy / 100.0 * fighter.accuracy / 100.0) and not fighter.dead

            if hit:
                attack.use(self, fighter, targets) # Actually use the fighter's attack so call `damage_fighters`
            else:
                self.send_message(f"{fighter.character.display_name} missed!", MessageType.ATTACK)

    def run_effects(self):
        # Update the effects applied to every fighter.
        # This happens after all of the attacks are done for "fairness"
        # This does a bunch of repeated iteration, but at the number of
        # effects that will be applied it is fine.
        for fighter in self.turn_order:
            for effect in tuple(fighter.effects):
                effect.update(self)
                should_decay = effect.decay(self)
                if should_decay:
                    self.remove_effect(effect, fighter, silent=True)

            fighter.reset_effects()
            for effect in fighter.effects:
                effect.apply()

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
                    self.send_message(f"{fighter.character.display_name}: {attack.name} now available!", MessageType.ATTACK)
                else:
                    self.send_message(f"{fighter.character.display_name}: {attack.name} available in {attack.turns_until_available} turns!", MessageType.ATTACK)

            if fighter.dead:
                self.fighters.remove(fighter)
                fighter.effects = ()
        self.turn += 1

    def __str__(self) -> str:
        return f"<Encounter {self.allies} vs {self.enemies}>"

    def __repr__(self) -> str:
        return self.__str__()

# |---- RPG Content ----|

# -- Effect Functions --
def apply_status_effect(encounter: Encounter, fighter: Fighter, stat: CharacterStat, amount: float, scale: bool = False):
    """
    Temporarily change the stats of a fighter.

    Options:
        stat (CharacterStat): The chacter stat to change out of Defence, Attack, Accuracy
        amount (float): The amount to change the stat by (negative or positive)
        scale (bool, optional): Whether the amount is a scale factor or a flat amount. Defaults to False.
    """
    if stat == CharacterStat.HIT_POINTS:
        encounter.send_message("Cannot change HIT POINTS as a status effect", MessageType.DEBUG)
        return

    if scale:
        encounter.scale_fighter(fighter, stat, amount, permanent=False)
    else:
        encounter.modify_fighter(fighter, stat, amount, permanent=False)


def update_damage_over_time(encounter: Encounter, fighter: Fighter, damage: float = 10, ignore_armour: bool = False):
    """
    Deal a set amount of damage every turn for a few turns

    Options:
        damage (float): Amount of damage to do each turn
        ignore_armour (bool, optional): whether the DOT should ignore the armour of the fighter. Defaults to False.
    """
    encounter.damage_fighter(fighter, damage, roll_crit=False, ignore_armour=ignore_armour)


def decay_chance(encounter: Encounter, fighter: Fighter, chance: float = 0.5) -> bool:
    """
    A random chance for the effect to end

    Options:
        chance (float, optional): Percent chance for effect to end. Defaults to 0.5.
    """
    return random.random() <= chance


# -- Attack Functions --

@attack_def(AttackType.DAMAGE)
def damage_fighters(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult: float = 1.0, count: int = 1):
    """
    Damage the target fighters

    Options:
        mult (float, optional): The multiplier on top of attacker's ATK. Defaults to 1.0.
        count (int, optional): number of times to apply damage. Defaults to 1.
    """
    for target in targets:
        for _ in range(count):
            encounter.damage_fighter(target, mult * fighter.attack)

@attack_def(AttackType.HEAL)
def heal_fighters(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult: float = 1.0, overheal: bool = False):
    """
    Heal the target fighters based on healer's ATK

    Options:
        mult (float, optional): The multiplier on top of attacker's ATK. Defaults to 1.0.
        overheal (bool, optional): Whether to allow targets to heal over their max health.
    """
    for target in targets:
        if target.dead:
            continue
        encounter.heal_fighter(target, mult * fighter.attack, overheal)

@attack_def(AttackType.DAMAGE | AttackType.EFFECT)
def damage_over_time(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult: float = 1.0,  duration: int = 1):
    """
    Apply damage over time to fighters

    Args:
        mult (float, optional): The multiplier on top of attacker's ATK. Defaults to 1.0.
        duration (int, optional): The number of turns to apply damage. Defaults to 1.
    """
    for target in targets:
        encounter.apply_effect(Effects.BLEED, target, duration, update_override={"damage": fighter.attack * mult})

@attack_def(AttackType.DAMAGE)
def damage_fighters_range(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult_min: float = 0.0, mult_max: float = 1.0):
    """
    Damage fighters by a randomly scaled amount

    Args:
        mult_min (float, optional): minimum damage multiplier. Defaults to 0.0.
        mult_max (float, optional): maximum damage multiplier. Defaults to 1.0.
    """
    for target in targets:
        mult = random.uniform(mult_min, mult_max)
        encounter.damage_fighter(target, fighter.attack * mult)

@attack_def(AttackType.DAMAGE | AttackType.EFFECT | AttackType.SACRIFICE)
def damage_sacrifice(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], harm_mult: float = 1.0, bleed_mult: float = 1.0, duration: int = 1):
    encounter.damage_fighter(fighter, fighter.attack * harm_mult)
    for target in targets:
        encounter.apply_effect(Effect.BLEED, target, duration, update_override={"damage": fighter.attack * bleed_mult})


@attack_def(AttackType.BUFF)
def defend_targets(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
    """
    Increase the targets defence for a single turn
    """
    for target in targets:
        if target.dead:
            continue
        encounter.apply_effect(Effects.DEFEND, target)

@attack_def(AttackType.DEBUFF | AttackType.EFFECT)
def confuse_targets(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
    """
    Apply the Confusion effect to target fighters
    """
    for target in targets:
        if target.dead:
            continue
        encounter.apply_effect(Effects.CONFUSION, target)

@stat_attack_def() # This decides the type based on if mult is >1.0 or not
def change_stat(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], stat: CharacterStat, mult: float = 1.0):
    """
    Scale target fighters' stats by the multiplier

    Args:
        stat (CharacterStat): The CharacterStat to scale
        mult (float, optional): How much to scale the specified stat by. Defaults to 1.0.
    """
    for target in targets:
        encounter.scale_fighter(target, stat, mult, permanent=True)

@attack_def(AttackType.BUFF | AttackType.DEBUFF)
def draw_in(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult: float = 1.0):
    attack_type = renpy.random.randint(1, 4)
    match attack_type:
        case 1: # ap up, allies
            encounter.send_message("[Draw In] DEF Up", MessageType.DEBUG)
            allies = True
            stat = CharacterStat.DEFENSE
        case 2: # ap down, enemies
            encounter.send_message("[Draw In] DEF Down", MessageType.DEBUG)
            allies = False
            stat = CharacterStat.DEFENSE
            mult = 1.0 / mult
        case 3: # atk up, allies
            encounter.send_message("[Draw In] ATK Up", MessageType.DEBUG)
            allies = True
            stat = CharacterStat.ATTACK
        case 4: # atk down, enemies
            encounter.send_message("[Draw In] ATK Down", MessageType.DEBUG)
            allies = False
            stat = CharacterStat.ATTACK
            mult = 1.0 / mult
        case _: # impossible case
            encounter.send_message("[Draw In] Impossible Result", MessageType.DEBUG)
            return

    for target in targets:
        if (allies and fighter.enemy == target.enemy) or (not allies and fighter.enemy != target.enemy):
            encounter.scale_fighter(target, stat, mult, permanent=True)

@attack_def(AttackType.DAMAGE | AttackType.HEAL | AttackType.BUFF | AttackType.DEBUFF | AttackType.EFFECT) # What could it beee??
def ai_mimic(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
    if targets[0].name == "Copguy EX":
        aa = [a for a in Attacks.ex_attacks if a.type & AttackType.AOE or a.type & AttackType.ATTACK]
        attack = random.choice(aa)
    else:
        attack = targets[0].character.attacks[0]
    if attack.name == "AI Mimic":
        attack = Attacks.PUNCH
    encounter.send_message(f"[AI Mimic] running {attack.name}...", MessageType.DEBUG)
    attack.func(encounter, fighter, targets)

class AIType:
    NEUTRAL = AI("Neutral")
    AGGRO = AI("Aggro", aggression = 3, tacticity = 0.5, crowd_control = 0.1, heal_threshold = 0.25, heal_chance = 0.25)
    DEFENSIVE = AI("Defensive", heal_threshold = 0.75, tacticity = 3, heal_chance = 0.60)
    SMART = AI("Smart", tacticity = 2, crowd_control = 2, heal_chance = 0.60)
    COPGUY_EX = AI("EX", aggression = 3, tacticity = 2, preferred_targets = ["CS"], heal_chance = 0.70)

    @classmethod
    def get(cls, ai: str, default: AI | None = None) -> AI | None:
        cls.__dict__.get(ai, default)

class Effects:
    CONFUSION = Effect("Confusion", "Confuse and befuddle!", None, False, 0, apply_func=apply_status_effect, apply_options={"stat": CharacterStat.ACCURACY, "amount": 0.5, "scale": True}, decay_func=decay_chance)
    BLEED = Effect("Bleed", "Bleed them dry!", None, False, 0, update_func=update_damage_over_time)
    DEFEND = Effect("Defend", "Not today!", None, True, 1, apply_func=apply_status_effect, apply_options={"stat": CharacterStat.DEFENSE, "amount": 1.5, "scale": True})

class Attacks:
    DEFEND = Attack("Defend", "Dragon doesn't know how to write these", defend_targets, AttackType.EFFECT, targets=TargetType.SELF)
    PUNCH = Attack("Punch", "A simple punch.", damage_fighters)
    RAW_CHOP = Attack("Raw Chop", "Hiya!", damage_fighters) # , ex = False
    CS_AP_DOWN = Attack("CS DEF Down", "Bring DEF of an enemy down.", change_stat, AttackType.DEBUFF, stat = CharacterStat.DEFENSE, mult = 0.75) # , ex = False
    CHOP = ComboAttack("Chop", "Hit an enemy and bring their DEF down.", [RAW_CHOP, CS_AP_DOWN])
    RAW_KICK = Attack("Raw Kick", "It's fuckin raw!", damage_fighters, mult = 2) # , ex = False
    YTP_MAGIC = Attack("YTP Magic", "Channel the power of YTP!", damage_fighters, cooldown = 10, mult = 20, accuracy = 100, used = True)
    YTP_MAGIC_NOCOOL = Attack("YTP Magic", "Let no one stand in your way.", damage_fighters, mult = 20, accuracy = 100) # , ex = False
    YTP_HEAL = Attack("Attack.HEAL", "No matter the cost.", heal_fighters, AttackType.HEAL, target_count = 0, target_type = TargetType.ALLY, cooldown = 1, mult = 3, accuracy = 100)
    FUN_VALUE = Attack("Fun Value", "A Dev's favorite attack.", damage_fighters, mult = 10, accuracy = 100,)
    KICK = ComboAttack("Kick", "A stronger attack, and lowers DEF.", [RAW_KICK, CS_AP_DOWN])
    BULLET_SPRAY = Attack("Bullet Spray", "Shred all enemies with your LMG!", damage_fighters, target_count = 0, cooldown = 3, mult = 1.5, accuracy = 70)
    RAW_SLASH = Attack("Raw Slash", "It's fuckin raw!", damage_fighters) # , ex = False
    BLEED = Attack("Bleed", "Bleed them dry!", damage_over_time, AttackType.EFFECT, mult = 0.25) # , ex = False
    SLASH = ComboAttack("Slash", "A cutting attack that bleeds out your enemies.", [RAW_SLASH, BLEED], accuracy = 85)
    LIGHT_CAST = Attack("Light Cast", "A strong blast of light that varies in damage.", damage_fighters_range, cooldown = 3, min_mult = 1, max_mult = 3)
    INSIGHT = Attack("Insight", "Lowers enemy's attack by a little.", change_stat, AttackType.DEBUFF, stat = CharacterStat.ATTACK, mult = 0.75, accuracy = 90)
    SHOTGUN = Attack("Shotgun", "Blast your enemies twice with a powerful shotgun blast!", damage_fighters, target_count = 2, cooldown = 3, mult = 2, accuracy = 70)
    ENCOURAGE = Attack("Encourage", "Heal one member with morale!", heal_fighters, target_count = 1, target_type = TargetType.ALLY, accuracy = 95)
    HIGH_NOON = Attack("High Noon", "Quickly blast 3 targets, or 3 shots on 1!", damage_fighters, target_count = 3, cooldown = 3, mult = 0.75, accuracy = 60)
    SCRATCH = Attack("Scratch", "A basic scratch attack.", damage_fighters, accuracy = 75)
    ARMOUR = Attack("Armour", "Boost one's defense!", change_stat, AttackType.BUFF, stat = CharacterStat.DEFENSE, target_count = 1, target_type = TargetType.ALLY, cooldown = 3, mult = 2.5, accuracy = 90)
    DAMAGE_SCREM = Attack("Damage Screm", "Yell as loud as possible to deafen your enemies!", damage_fighters, target_count = 0, mult = 0.5, accuracy = 75)
    SNACK_TIME = Attack("Snack Time", "Heal your team with the power of snacks!", heal_fighters, AttackType.HEAL, target_count = 0, target_type = TargetType.ALLY, cooldown = 3, accuracy = 95)
    ELDRITCH_BLAST = Attack("Eldritch Blast", "An unholy blast that does quite a bit of damage to an enemy.", damage_fighters, mult = 1.5)
    RAINBOW = Attack("Rainbow", "", confuse_targets, AttackType.EFFECT, cooldown = 3) # , ex = False
    VOMIT = Attack("Vomit", "", damage_over_time, AttackType.EFFECT, cooldown = 3, duration = 3) # , ex = False
    RAINBOW_NOCOOL = Attack("Rainbow", "", confuse_targets, AttackType.EFFECT) # , ex = False
    VOMIT_NOCOOL = Attack("Vomit", "", damage_over_time, AttackType.EFFECT, mult = 1, duration = 3) # , ex = False
    RAINBOW_VOMIT = ComboAttack("Rainbow Vomit", "Confuse and damage your enemies with colorful nonsense!", [RAINBOW, VOMIT], AttackType.EFFECT, accuracy = 75)
    ROBOPUNCH = Attack("RoboPunch", "A strong punch.", damage_fighters, mult = 1.75)
    HOLOSHIELD = Attack("HoloShield", "Boosts your team's defense by a bit.", change_stat, AttackType.BUFF, stat = CharacterStat.DEFENSE, target_count = 0, target_type = TargetType.ALLY, cooldown = 3, mult = 1.75, accuracy = 90)
    MUSIC_BOOST = Attack("Music Boost", "Boost one's defense by a bit.", change_stat, AttackType.BUFF, stat = CharacterStat.DEFENSE, target_count = 1, target_type = TargetType.SELF, mult = 1.5)
    RAVE_DEF = Attack("Rave DEF", "Lowers the enemies defense.", change_stat, AttackType.DEBUFF, target_count = 0, stat = CharacterStat.DEFENSE, cooldown = 3, mult = 0.5) # , ex = False
    RAVE_OFF = Attack("Rave OFF", "Rupture eardrums.", damage_fighters, target_count = 0, cooldown = 3, mult = 0.5) # , ex = False
    RAVE = ComboAttack("Rave", "Blast your enemies' eardrums! (Damages enemies while lowering their defense.)", [RAVE_DEF, RAVE_OFF], accuracy = 75)
    SAMPLE_SPAM = Attack("Sample Spam", "", damage_fighters_range, min_mult = 1, max_mult = 3) # , ex = False
    SOUND_BLAST = Attack("Sound Blast", "", damage_fighters, target_count = 0) # , ex = False
    SAMPLE_BLAST = ComboAttack("Sample Blast", "Blast your enemies with music! Varies in damage.", [SAMPLE_SPAM, SOUND_BLAST])
    GNOMED = Attack("Gnomed", "Confuse everyone by gnoming them!", confuse_targets, AttackType.EFFECT, target_count = 0, cooldown = 3, accuracy = 70)
    NUDGE = Attack("Nudge", "Does either very little or massive damage.", damage_fighters_range, min_mult = 0.1, max_mult = 10, accuracy = 85)
    DRAW_IN = Attack("Draw in", "Either lowers the enemies stats, or increases your friend's stats!", draw_in, AttackType.BUFF, TargetType.ALL, target_count=0, mult = 2, accuracy = 85)
    CONFIDENCE = Attack("Confidence", "Raise your team's attack!", change_stat, AttackType.BUFF, stat = CharacterStat.ATTACK, target_count = 0, target_type = TargetType.ALLY, mult = 1.25, accuracy = 90)
    PEP_TALK = Attack("Pep Talk", "Raise your team's defense!", change_stat, stat = CharacterStat.DEFENSE, target_count = 0, target_type = TargetType.ALLY, mult = 1.25, accuracy = 90)
    RADS_ATTACK = Attack("RADS Attack", "Inflict radiation on your enemies to kill them over time!", damage_over_time, AttackType.EFFECT, mult = 0.5, accuracy = 60)
    AI_MIMIC = Attack("AI Mimic", "Copies an enemy's attack.", ai_mimic, target_count = 1, target_type = "enemies", cooldown = 2)
    SHELL = Attack("Shell", "Fire a tank shell!", damage_fighters_range, min_mult = 1, max_mult = 2, accuracy = 60)
    HEAL_EX = Attack("Heal EX", "Lots of healing.", heal_fighters, AttackType.HEAL, target_count = 0, target_type = TargetType.ALLY, mult = 10, accuracy = 100)
    AUGMENT = Attack("Awesome Augment", "Fire a laser! Fire a laser!", damage_fighters, target_count = 0, mult = 15, cooldown = 5, accuracy = 100) # , ex = False
    TATE_RECALL = Attack("Tate's Recall", "Remember something dreadful.", damage_fighters, target_type = TargetType.SELF, mult = 0.75, cooldown = 9, accuracy = 90) # , ex = False
    TATE_REVERB = Attack("Tate's Reverb", "Make them all remember.", damage_over_time, AttackType.EFFECT, target_count = 0, mult = 0.75, cooldown = 9, duration = 5, accuracy = 90) # , ex = False
    REVERB_RECALL = Attack("Reverb Recall", "Channel your pain over 5 turns. Also damages the user.", damage_sacrifice, AttackType.EFFECT, harm_mult = 0.75, bleed_mult = 0.75, duration = 5, cooldown = 9, accuracy = 90) # , ex = False
    TATE_ECHOES = Attack("Tate's Echoes", "The past haunts you.", change_stat, AttackType.DEBUFF, stat = CharacterStat.ATTACK, target_type = TargetType.SELF, mult = 0.5, cooldown = 11, accuracy = 100) # , ex = False
    TATE_BLAST = Attack("Tate's Blaster", "Make it haunt them, too.", damage_fighters, target_count = 0, mult = 4, cooldown = 11, accuracy = 100) # , ex = False
    # TODO: we really need the ability to select different things for each part of the combo
    ECHO_BLAST = ComboAttack("Echo Blast", "Make them feel the pain of the past, at the cost of your ATK.", [TATE_BLAST, TATE_ECHOES], cooldown = 11, accuracy = 100) # , ex = False
    GENERGY = Attack("Genergy", "Sip some refreshing Genergy.", heal_fighters, AttackType.HEAL, target_count = 1, target_type = TargetType.ALLY, mult = 2.36, accuracy = 100) # , ex = False

    # UCN
    STOMP = Attack("Stomp", "Send an earthquake to the enemies!", damage_fighters, target_count = 0, mult = 0.75) # , ex = False
    POKE = Attack("Poke", "A mega poke.", damage_fighters, mult = 2.5, accuracy = 90) # , ex = False
    SWORD = Attack("Sword", "The edge of a sharp thing.", damage_fighters) # , ex = False
    SWORD_AP = Attack("Sword (DEF Down)", "The edge of a sharp thing, more.", change_stat, AttackType.DEBUFF, stat = CharacterStat.DEFENSE, mult = 0.75) # , ex = False
    SWORD_SLASH = ComboAttack("Sword Slash", "Hit an enemy, and take a chip out of their armor.", [SWORD, SWORD_AP]) # , ex = False
    FLAMETHROWER = Attack("Flamethrower", "Spray all your enemies with burning fuel!", damage_over_time, AttackType.EFFECT, target_count = 0, mult = 0.5, duration = 3, cooldown = 3, accuracy = 70) # , ex = False,
    CHOCOLATE_CAKE = Attack("Chocolate Cake", "Heal a party member with loads to eat!", heal_fighters, target_type = "allies", accuracy = 95) # , ex = False
    CONFUSING_STORY = Attack("Confusing Story", "Tell a puzzling poem.", confuse_targets, AttackType.EFFECT) # , ex = False
    HYPE_UP = Attack("Hype Up", "Get a team member pumped to fight!", change_stat, AttackType.BUFF, stat = CharacterStat.ATTACK, target_type = TargetType.ALLY, mult = 1.5, accuracy = 90) # , ex = False
    PITCHMAN = Attack("Pitchman", "Smooth-talk an enemy's defenses down!", change_stat, AttackType.DEBUFF, mult = 0.75, stat = CharacterStat.DEFENSE, accuracy = 90) # , ex = False
    HUG = Attack("Hug", "Hug an enemy (ouch).", damage_fighters, mult = 1.5, accuracy = 90) # , ex = False
    SPIKE_BOMB = Attack("Spike Bomb", "Release spikes to all enemies!", damage_fighters, target_count = 0, mult = 1.5, cooldown = 3, accuracy = 75) # , ex = False
    SHOT = Attack("Shot", "I'd like to see you outrun bullet.", damage_fighters, mult = 1.5) # , ex = False
    SHOT_AP = Attack("Shot (DEF Down)", "Kevlar destroyed.", change_stat, AttackType.DEBUFF, stat = CharacterStat.DEFENSE, mult = 0.75) # , ex = False
    PISTOL = ComboAttack("Pistol", "A sharp shot to the chest.", [SHOT, SHOT_AP]) # , ex = False
    ALL_OVER_AGAIN = Attack("All Over Again", "Ditto.", ai_mimic) # , ex = False
    HEAVY_PUNCH = Attack("Heavy Punch", "A quick blow.", damage_fighters, mult = 1.75, accuracy = 75) # , ex = False
    SOTH = Attack("Shit On The House", "I'm going to... take a shit on the house.", damage_fighters, target_count = 0, mult = 2, cooldown = 3, accuracy = 65) # , ex = False
    ONE_HUNDRED = Attack("100% Unsatisfied", "Yelp reviews coming in...", change_stat, AttackType.DEBUFF, stat = CharacterStat.ATTACK, target_count = 0, mult = 0.8, accuracy = 95) # , ex = False
    ICE_CREAM = Attack("Ice Cream", "Bing chilling!", heal_fighters, AttackType.HEAL, target_count = 0, target_type = TargetType.ALLY, accuracy = 90, mult = 1.5, cooldown = 3) # , ex = False
    RAINBOW_VOMIT_NOCOOL = ComboAttack("Rainbow Vomit", "Why are you like this?", [RAINBOW_NOCOOL, VOMIT_NOCOOL], accuracy = 75) # , ex = False
    KARATE_CHOP = ComboAttack("Karate Chop", "Hit an enemy and bring their DEF down.", [RAW_CHOP, SWORD_AP]) # , ex = False
    DRONE_STRIKE = Attack("Drone Strike", "O Bomb a.", damage_fighters, target_count = 0, cooldown = 3, mult = 2.5, accuracy = 85) # , ex = False
    COIN_BARRAGE = Attack("Coin Barrage", "Pelt your foes with change!", damage_fighters_range, min_mult = 0.75, max_mult = 2, accuracy = 60) # , ex = False
    CART_SMASH = Attack("Cart Smash", "Ram into someone with a shopping cart.", damage_fighters, mult = 5, accuracy = 95, cooldown = 3) # , ex = False
    BITE = Attack("Bite", "Chomp!", damage_fighters_range, min_mult = 5, max_mult = 10, mult = 5, accuracy = 5) # , ex = False
    SHARKNADO = ComboAttack("Sharknado", "A confusing vortex of sharks.", [BITE, BLEED], cooldown = 5, accuracy = 80) # , ex = False
    LOBBYING = ComboAttack("Lobbying", "Lobby like it's your hobby!", [ENCOURAGE, CS_AP_DOWN]) # , ex = False
    NANOMACHINES = Attack("Nanomachines", "Nanomachines, son.", damage_fighters, target_count = 8, mult = 1.5, accuracy = 95, cooldown = 7) # , ex = False

    @classproperty
    def names(cls) -> list[str]:
        return [a for a in dir(cls) if a.isupper()]

    @classproperty
    def attacks(cls) -> list[Attack]:
        names = cls.names
        return [cls.__dict__[a] for a in names]

    ucn_attacks = (
        STOMP, POKE, SWORD, SWORD_AP, SWORD_SLASH, FLAMETHROWER, CHOCOLATE_CAKE, CONFUSING_STORY, HYPE_UP,
        PITCHMAN, HUG, SPIKE_BOMB, SHOT, SHOT_AP, PISTOL, ALL_OVER_AGAIN, HEAVY_PUNCH, SOTH, ONE_HUNDRED,
        ICE_CREAM, RAINBOW_VOMIT_NOCOOL, KARATE_CHOP, DRONE_STRIKE, COIN_BARRAGE, CART_SMASH, BITE, SHARKNADO,
        LOBBYING, NANOMACHINES
    )

    ex_blacklist = { a.name for a in # Name is hashable, while the attacks aren't
        (RAW_CHOP, CS_AP_DOWN, RAW_KICK, YTP_MAGIC_NOCOOL, RAW_SLASH, BLEED, RAINBOW, VOMIT,
        RAINBOW_NOCOOL, VOMIT_NOCOOL, RAVE_DEF, RAVE_OFF, SAMPLE_SPAM, SOUND_BLAST, AUGMENT,
        TATE_RECALL, TATE_REVERB, REVERB_RECALL, TATE_ECHOES, TATE_BLAST, ECHO_BLAST, GENERGY,
        *ucn_attacks)
    }
    @classproperty
    def ex_attacks(cls) -> list[Attack]:
        return [a for a in cls.attacks if a.name not in cls.ex_blacklist]

    @classmethod
    def get(cls, k: str, default = None) -> Attack | None:
        return cls.__dict__.get(k, default)

class Characters:
    NONE = None

    # Allies
    CS = Character("CS", 188, 10, 25, [Attacks.PUNCH, Attacks.BULLET_SPRAY], portrait=Image("gui/rpg/portraits/cs.png"))
    CS_NG = CS.clone("CS (National Guard)", attack=30, attacks=[Attacks.CHOP, Attacks.BULLET_SPRAY]) # Character("CS (National Guard)", 188, 10, 30, , portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_STRONG = Character("CS (Strong)", 188, 10, 35, [Attacks.KICK, Attacks.BULLET_SPRAY], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_FINAL = Character("CS (Final)", 288, 10, 40, [Attacks.KICK, Attacks.BULLET_SPRAY, Attacks.YTP_MAGIC], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_FINAL2 = Character("CS (Error)", 1880, 10, 250, [Attacks.KICK, Attacks.YTP_HEAL, Attacks.YTP_MAGIC_NOCOOL], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_WEAK = Character("CS (Weak)", 188, 5, 25, [Attacks.PUNCH], protrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_ARCHIVAL = Character("CS (Archival)", 1027, 50, 27, [Attacks.KICK, Attacks.YTP_HEAL], protrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_VS_TATE_PUNCH = Character("CS (VS Tate - Punch)", 288, 10, 40, [Attacks.PUNCH, Attacks.GENERGY, Attacks.YTP_MAGIC], protrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_VS_TATE_KICK = Character("CS (VS Tate - Kick)", 288, 10, 40, [Attacks.KICK, Attacks.GENERGY, Attacks.YTP_MAGIC], protrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_VS_TATE_CHOP = Character("CS (VS Tate - Chop)", 288, 10, 40, [Attacks.CHOP, Attacks.GENERGY, Attacks.YTP_MAGIC], protrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    ARCEUS = Character("Arceus", 160, 15, 35, [Attacks.SLASH, Attacks.LIGHT_CAST], protrait=Image("gui/rpg/portraits/arceus.png"))
    PAKOO = Character("Pakoo", 145, 20, 30, [Attacks.INSIGHT, Attacks.SHOTGUN], protrait=Image("gui/rpg/portraits/pokoo.png"))
    MIKA = Character("Mika", 165, 20, 30, [Attacks.ENCOURAGE, Attacks.HIGH_NOON], protrait=Image("gui/rpg/portraits/mika.png"))
    KITTY = Character("Kitty", 155, 15, 20, [Attacks.SCRATCH, Attacks.ARMOUR], protrait=Image("gui/rpg/portraits/kitty.png"))
    TATE = Character("Tate", 170, 5, 30, [Attacks.DAMAGE_SCREM, Attacks.SNACK_TIME], protrait=Image("gui/rpg/portraits/tate.png"))
    ARIA = Character("Aria", 220, 20, 45, [Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT], protrait=Image("gui/rpg/portraits/aria.png"))
    DIGI = Character("Digi", 150, 20, 30, [Attacks.ROBOPUNCH, Attacks.HOLOSHIELD], protrait=Image("gui/rpg/portraits/digi.png"))
    NOVA = Character("Nova", 170, 5, 30, [Attacks.MUSIC_BOOST, Attacks.RAVE], protrait=Image("gui/rpg/portraits/nova.png"))
    BLANK = Character("Blank", 180, 5, 35, [Attacks.SAMPLE_BLAST, Attacks.GNOMED], protrait=Image("gui/rpg/portraits/blank.png"))
    MIDGE = Character("Midge", 165, 10, 25, [Attacks.NUDGE, Attacks.DRAW_IN], protrait=Image("gui/rpg/portraits/midge.png"))
    DB05 = Character("DB05", 9001, 9001, 50, [Attacks.CONFIDENCE, Attacks.PEP_TALK], protrait=Image("gui/rpg/portraits/db05.png"))
    ANNO = Character("Anno", 200, 20, 40, [Attacks.RADS_ATTACK, Attacks.AI_MIMIC], protrait=Image("gui/rpg/portraits/anno.png"))

    # Allies (UCN)
    BUBBLE = Character("{image=gui/dx_text.png} Bubble", 250, 10, 35, [Attacks.STOMP, Attacks.POKE], display_name = "Bubble")
    GES = Character("{image=gui/dx_text.png} Ges", 170, 20, 35, [Attacks.SWORD_SLASH, Attacks.FLAMETHROWER], display_name = "Ges")
    MICHAEL = Character("Michael", 155, 15, 35, [Attacks.CHOCOLATE_CAKE, Attacks.CONFUSING_STORY])
    BILLY = Character("Billy", 220, 10, 25, [Attacks.HYPE_UP, Attacks.PITCHMAN, Attacks.AUGMENT])
    PHIL = Character("Phil", 160, 20, 40, [Attacks.HYPE_UP, Attacks.PITCHMAN])
    MEAN = Character("Mean", 150, 20, 35, [Attacks.HUG, Attacks.SPIKE_BOMB])
    POMNI = Character("Pomni", 200, 15, 30, [Attacks.RAINBOW_VOMIT_NOCOOL, Attacks.RAINBOW_VOMIT_NOCOOL])
    OBAMA = Character("{image=gui/dx_text.png} Obama", 190, 25, 35, [Attacks.KARATE_CHOP, Attacks.DRONE_STRIKE])
    CASHIER = Character("{image=gui/dx_text.png} Cashier", 188, 14, 33, [Attacks.COIN_BARRAGE, Attacks.CART_SMASH])
    SHARK = Character("{image=gui/dx_text.png} Shark", 190, 10, 40, [Attacks.BITE, Attacks.SHARKNADO])

    # Enemies
    FANBOYA = Character("Fanboy (NVIDIA)", 50, 0, 16, [Attacks.PUNCH], sprite=Image("images/characters/nvidiafanboy.png"), ai = AIType.NEUTRAL, display_name = "Fanboy")
    FANBOYB = Character("Fanboy (AMD)", 50, 0, 16, [Attacks.PUNCH], sprite=Image("images/characters/amdfanboy.png"), ai = AIType.NEUTRAL, display_name = "Fanboy")
    COP = Character("Cop", 150, 15, 30, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/cop.png"), ai = AIType.NEUTRAL)
    COPGUYGODMODE = Character("Copguy (God)", 9001, 9001, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/copguy/copguy.png"), ai = AIType.NEUTRAL, display_name = "Copguy")
    COPGUY = Character("Copguy", 300, 20, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/copguy/copguy.png"), ai = AIType.NEUTRAL)
    GUARD = Character("Guard", 225, 25, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/guard_soldier.png"), ai = AIType.DEFENSIVE)
    SML_TANK = Character("Sherman", 400, 60, 100, [Attacks.SHELL], sprite=Image("images/characters/sherman.png"), ai = AIType.AGGRO)
    MARINE = Character("Marine", 300, 30, 45, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/marine.png"), ai = AIType.SMART)
    BIG_TANK = Character("Abrams",700, 70, 150, [Attacks.SHELL], sprite=Image("images/characters/abrams.png"), ai = AIType.AGGRO)
    COPGUY_EX = Character("Copguy EX", 2222, 30, 50, Attacks.ex_attacks, sprite=Image("images/characters/copguy/copguy.png"), ai = AIType.COPGUY_EX)
    PAKOOE = Character("Pakoo (Error)", 9999, 70, 150, [Attacks.FUN_VALUE], sprite=Image("images/characters/pakoo/pakoo_disappointed.png"), ai = AIType.AGGRO, display_name = "Pakoo")
    COPGUY_EXE = Character("{image=gui/dx_text.png} Copguy.EXE", 666, 66, 66, [Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT, Attacks.SLASH, Attacks.CONFUSING_STORY], sprite=Image("images/characters/copguy/copguyexe.png"), ai = AIType.AGGRO, display_name = "Copguy.EXE")
    K174 = Character("K17-4", 174, 17, 20, [Attacks.PUNCH], sprite=Image("images/characters/k174.png"), ai = AIType.NEUTRAL)
    K199 = Character("K19-9", 199, 19, 30, [Attacks.KICK], sprite=Image("images/characters/k199.png"), ai = AIType.AGGRO)
    K207 = Character("K20-7", 207, 20, 10, [Attacks.PUNCH], sprite=Image("images/characters/k207.png"), ai = AIType.DEFENSIVE)
    TATE_EX = Character("{image=gui/dx_text.png} Tate EX", 9999, 11, 111, [Attacks.DAMAGE_SCREM, Attacks.REVERB_RECALL, Attacks.ECHO_BLAST], sprite=Image("secret/pt/tate_ex.png"), ai = AIType.AGGRO, display_name = "Tate EX")

    # Enemies (UCN)
    WESLEY = Character("{image=gui/dx_text.png} Wesley", 200, 20, 40, [Attacks.PISTOL, Attacks.ALL_OVER_AGAIN], sprite=Image("images/characters/hohsis/wesley.png"), ai = AIType.AGGRO, display_name = "Wesley")
    ED = Character("{image=gui/dx_text.png} Ed", 300, 30, 25, [Attacks.HEAVY_PUNCH, Attacks.SOTH], sprite=Image("images/characters/hohsis/ed.png"), ai = AIType.SMART, display_name = "Ed")
    RICHARD = Character("{image=gui/dx_text.png} Richard", 250, 20, 30, [Attacks.ONE_HUNDRED, Attacks.ICE_CREAM], sprite=Image("images/characters/hohsis/rich.png"), ai = AIType.DEFENSIVE, display_name = "Richard")
    CEO = Character("{image=gui/dx_text.png} CEO of Diabetes", 1000, 50, 75, [Attacks.LOBBYING, Attacks.NANOMACHINES], sprite=Image("images/characters/ceo.png"), ai = AIType.SMART, display_name = "CEO")
    SECRETARY = Character("{image=gui/dx_text.png} Secretary of Diabetes", 1000, 50, 75, [Attacks.LOBBYING, Attacks.NANOMACHINES], sprite=Image("images/characters/secretary.png"), ai = AIType.SMART, display_name = "Secretary")

    allies = (
        CS, CS_NG, CS_STRONG, CS_FINAL, CS_FINAL2, CS_WEAK, CS_ARCHIVAL, CS_VS_TATE_PUNCH, CS_VS_TATE_KICK, CS_VS_TATE_CHOP,
        ARCEUS, PAKOO , MIKA, KITTY , TATE, ARIA, DIGI, NOVA, BLANK , MIDGE , DB05, ANNO, BUBBLE , GES, MICHAEL, BILLY, PHIL,
        MEAN, POMNI, OBAMA, CASHIER, SHARK,
    )
    ally_names = tuple(
        ally.name for ally in allies
    )
    ally_name_set = set(ally_names)

    enemies = (
        FANBOYA, FANBOYB, COP, COPGUYGODMODE, COPGUY, GUARD, SML_TANK, MARINE, BIG_TANK, COPGUY_EX, PAKOOE, COPGUY_EXE,
        K174, K199, K207, TATE_EX, WESLEY, ED, RICHARD, CEO, SECRETARY
    )
    enemy_names = tuple(
        enemy.name for enemy in enemies
    )
    enemy_name_set = set(enemy_names)

    characters = (
        *allies, *enemies
    )
    names = (
        *ally_names, *enemy_names
    )
    name_set = set(names)


    @classproperty
    def fighters(cls) -> list[Character]:
        return [cls.__dict__[f] for f in cls.names]

    @classproperty
    def enemies(cls) -> list[Character]:
        return [cls.get(f) for f in cls.enemy_names]

    @classproperty
    def allies(cls) -> list[Character]:
        return [cls.get(f) for f in cls.ally_names]

    @classmethod
    def get(cls, k: str, default = None) -> Character | None:
        return cls.__dict__.get(k, default)


type ParsedFighter = tuple[str, str | None, int | None, int | None, int | None, int | None]
# Parse a fighter by getting their name, and optional overrides for their ai, hp, def, atk, and acc
def parse_fighter(lexer) -> ParsedFighter:
    variable = lexer.match(r"\$") # Variable Fighter $<x>
    name = lexer.word()

    if variable:
        name = globals().get(name) # TODO: remove use of globals and test that lexer.word() works if $ is at the start.

    name = name.upper()
    ai = hp = defense = attack = accuracy = None
    while not lexer.eol():
        if lexer.keyword("ai"):
            ai = lexer.word().upper()
        elif lexer.keyword("hp"):
            hp = lexer.int()
        elif lexer.keyword("def"):
            defense = lexer.int()
        elif lexer.keyword("atk"):
            attack = lexer.int()
        elif lexer.keyword("acc"):
            accuracy = lexer.int()

    lexer.expect_eol(f"Parsing {name} Failed")
    return (name, ai, hp, defense, attack, accuracy)

type ParsedRpg = tuple[float, int, str, str, str | None, str | None, str | None, bool, list[ParsedFighter] | None, list[ParsedFighter], list[ParsedFighter]]
# Parse an rpg block and get the level/scale, background, music, on_win, on_lose, intro_text, if it is a ucn fight, fighters, ally fighters, and enemy fighters
def parse_rpg(lexer) -> ParsedRpg:
    block = lexer.subblock_lexer()
    level = 1.0
    initial = 0
    background = "images/bg/casino1.png"
    music = "card_castle"
    on_win = on_lose = intro = is_ucn = fighters = None
    allies = []
    enemies = []
    while block.advance():
        if fighters is not None:
            block.expect_noblock("old style rpg was used so don't use allies or enemies block")
        if block.keyword("level") or block.keyword("scale"):
            level = block.float()
            if level == "\"ucn\"":
                is_ucn = True
        if block.keyword("turn") or block.ketword("initial"):
            initial = block.int()
        elif block.keyword("bg"):
            background = block.string()
            if level == "ucn":
                is_ucn = True
        elif block.keyword("music"):
            music = block.string()
            if level == "ucn":
                is_ucn = True
        elif block.keyword("on_win"):
            on_win = block.string()
        elif block.keyword("on_lose"):
            on_lose = block.string()
        elif block.keyword("intro") or block.keyword("intro_text"):
            intro = block.string()
        elif block.keyword("ucn"):
            is_ucn = True
        elif block.keyword("fighters"):
            # Support old style RPG
            fighters = []
            block.expect("fighters")
            subblock = block.subblock_lexer()
            while subblock.advance():
                fighters.append(parse_fighter(subblock))
        elif block.keyword("allies"):
            block.expect_block("allies")
            subblock = block.subblock_lexer()
            while subblock.advance():
                allies.append(parse_fighter(subblock))
        elif block.keyword("enemies"):
            block.expect_block("enemies")
            subblock = block.subblock_lexer()
            while subblock.advance():
                enemies.append(parse_fighter(subblock))

    return level, initial, background, music, on_win, on_lose, intro, is_ucn, fighters, allies, enemies

def execute_rpg(parsed_object: ParsedRpg):
    level, initial, background, music, on_win, on_lose, intro_text, is_ucn, fighters, allies, enemies = parsed_object
    if is_ucn:
        background = ucn_bg
        music = ucn_music
        level = ucn_scale # TODO rename to level


    if fighters is not None:
        fighters = [
            Fighter(Characters.get(name), name in Characters.enemy_name_set, AIType.get(ai), hp, defense, attack, accuracy)
            for (name, ai, hp, defense, attack, accuracy) in fighters
        ]
    else:
        fighters = [
            *(
                Fighter(Characters.get(name), False, level, AIType.get(ai), hp, defense, attack, accuracy)
                for (name, ai, hp, defense, attack, accuracy) in allies
            ),
            *(
                Fighter(Characters.get(name), True, level, AIType.get(ai), hp, defense, attack, accuracy)
                for (name, ai, hp, defense, attack, accuracy) in enemies
            )
        ]

    rpggame.reset() # TODO: is this needed for the screen version of the rpg?
    rpggame.encounter = Encounter(fighters, background, music, on_win, on_lose, intro_text, initial)
    jump("play_rpggame")

def lint_rpg(parsed_object: ParsedRpg):
    level, initial, _, _, on_win, on_lose, _, _, fighters, allies, enemies = parsed_object
    # TODO: We should probably do this at some point.
    if level <= 0:
        print("raise issue!!!")
    elif initial <= 0:
        print("raise issue!!!")
    elif on_win is None:
        print("raise issue!!!")
    elif on_lose is None:
        print("raise issue!")
    elif fighters is not None and allies or enemies:
        print("raise issues!")
    elif fighters:
        print("check fighters etc!")
    elif allies:
        print("check allies etc!")
    elif enemies:
        print("check enemies etc!")

register_statement(
    name = "newrpg",
    parse = parse_rpg,
    lint = lint_rpg,
    execute = execute_rpg,
    block = True)

"""
rpg:
    bg "images/bg/X.png"
    music "audio/Y.ogg"
    on_win "label"
    on_lose "label2"
    intro "text when battle starts"
    level 1
    turn 0
    allies:
        cs hp 180 acc 25 ...
        ...
    enemies:
        cop
        ...

 Also supports old style

 rpg:
    bg "images/bg/X.png"
    music "audio/Y.ogg"
    fighters:
        cs
        cop
        etc...
    on_win "label"
    on_lose "label2"
    intro_text "text when battle starts"
"""

# |---- HOW TO RPG ----|
# 1) Create an encounter by creatings the fighters (Fighter(Character, is_enemy, level, ai, [optionally] stat overrides)) and filling in details.
# 2) For every player character (encounter.allies) get their next action (set fighter.next_action) and targets (set fighter.next_targets)
# 3) Then call encounter.run_attacks()
# 4) If need be refresh people's displayables
# 5) then call encounter.run_effects()
# 6) Handle visuals again
# 7) Handle the queue of damage indicators and messages
# 8) run encounter.cleanup_turn()
# 9) repeat step 2 onwards until encounter.won is not None
