from __future__ import annotations

import renpy
from renpy.display.core import Displayable
from renpy import random

# This is the equivalent of a python early block in a .rpy file.
"""renpy
rpy python annotations
python early:
"""
from dataclasses import dataclass
from queue import Queue
from typing import Callable, Any
from collections.abc import Sequence
from enum import StrEnum


# TODO:
# - Effect messages, they can be done in the effect functions, but this excludes when they decay due to duration
# - Linking with the screen / displayables
# - Reimplimenting all the content in the game
# - all the todos below

# |---- RPG ENGINE ----|

# -- CONSTANTS --

CRIT_CHANCE = 5.0 / 100.0
DAMAGE_INDICATOR_TIME = 1.0

# -- STR EUMS --

class CharacterStat(StrEnum):
    HIT_POINTS = "hp"
    ATTACK = "attack"
    DEFENSE = "defense"
    ACCURACY = "accuracy"

class AttackType(StrEnum):
    ATTACK = "attack"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"
    AOE = "aoe"
    EFFECT = "effect" # previously confuse + DOT

class IndicatorType(StrEnum):
    HP = "hp"
    DEF = "def"
    ATK = "atk"
    ACC = "acc"
    CONFUSION = "confusion"

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

class Attack:
    """
    An Attack defines what
    a fighter can do on their turn.
    """
    def __init__(
            self,
            name: str,
            description: str,
            typ: AttackType,
            func: Callable[..., Any], # I'm being lazy because typing these is kind of impossible rn
            targets: TargetType = TargetType.ENEMY,
            target_count: int = 1,
            cooldown: int = 0,
            accuracy: int = 80,
            start_used: bool = False,
            **kwds: Any
        ):
        self.name: str = name
        self.description: str = description
        self.type: AttackType = typ # typ of attack for AI

        self.func: Callable[..., Any] = func # the function which applies the effects of the attack
        self.targets: TargetType = targets # what group of fighters to attack
        self.target_count: int = target_count # how many enemies to target
        self.cooldown: int = cooldown # how many turns to wait on the cool down
        self.accuracy: int = accuracy # percent change of hitting witht the attack
        self.start_used: bool = start_used # whether to start counting down from the beginning of the fight

        self.options: dict[str, Any] = kwds # additionally arguments for Attack.func

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
            typ: AttackType,
            attacks: Sequence[Attack],
            targets: TargetType | None = None,
            cooldown: int | None = None,
            accuracy: int | None = None,
            start_used: bool | None = None,
            shared_targets: bool = False, # TODO: use to allow for mixed targetting
            ):
        self.name: str = name
        self.description: str = description
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

        print(f"{subject.name}: Choosing an attack...")

        available_attacks = tuple(a for a in subject.attacks if a.available)

        if len(available_attacks) == 0: # No attacks to chose?
            return
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
            available_attacks = [a for a in available_attacks if a.type == "heal"]
            if len(available_attacks) == 0:
                available_attacks = all_attacks
            if self.name == "COPGUY_EX":
                pass # TODO: add special exception for copguy_ex
                # available_attacks = [Attacks.HEAL_EX]
        else:
            available_attacks = [a for a in available_attacks if a.type != "heal"]

        scores = []
        # Weight attack likelyhood.
        for atk in available_attacks:
            score = 1.0
            if atk.type == AttackType.ATTACK or atk.type == AttackType.AOE:
                score *= (self.aggression * atk.options.get("mult", 1.0))
            elif atk.type == AttackType.BUFF or atk.type == AttackType.DEBUFF or atk.type == AttackType.EFFECT:
                score *= self.tacticity
            if atk.type == AttackType.AOE:
                score *= self.crowd_control
            if heal_party:
                score *= atk.options.get("mult", 1)  # weight towards better heals
            scores.append(score)

        # Choose an attack.
        print(available_attacks, scores)
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

    def __init__(self, name: str, base_hp: int, base_def: int, base_atk: int, attacks: Sequence[Attack | ComboAttack], base_acc: int = 100, sprite: Displayable | None = None, display_name: str | None = None):
        self.name: str = name
        self.display_name: str = display_name or name

        self.base_hp: int = base_hp # how much hp will the fighter start with, and what is their max hp
        self.base_def: int = base_def # how much defense will the fighter start with
        self.base_atk: int = base_atk # how much attack will the fighter start with
        self.base_acc: int = base_acc # how accurate will the fighter start with

        self.attacks: Sequence[Attack | ComboAttack] = attacks # What attacks can the character use
        self.sprite: Displayable | None = sprite # What image should represent the character


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
        self.ai: AI | None = ai # What AI does the fighter use. If none the encouter defers to the player

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
        self.attack.func(encounter, fighter, targets, **self.attack.options)

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
        self.global_effects: list[Effect] = [] # TODO: better handle global effects because this just slowly fills up

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
        if amount:
            print("Displaying {amount}x{type} on {target}")
        else:
            print("Displaying {type} on {target}")

    def get_next_indicator(self) -> Indicator | None:
        if self.indicator_queue.empty:
            return
        return self.indicator_queue.get()

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
            print("How did we get here??? (A non-existant fighter has lost an effect)")
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
            case CharacterStat.DEFENSE:
                old = fighter.defense
                new = int(old + amount)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defense = new
                self.display_indicator(fighter, IndicatorType.DEF, change)
            case CharacterStat.ATTACK:
                old = fighter.attack
                new = max(5, int(old + amount))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
            case CharacterStat.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old + amount)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)

    def scale_fighter(self, fighter: Fighter, stat: CharacterStat, mult: float, permanent: bool = True):
        match stat:
            case CharacterStat.HIT_POINTS:
                old = fighter.hit_points
                new = int(old * mult)
                fighter.hit_points = new
                self.display_indicator(fighter, IndicatorType.HP, new - old)
            case CharacterStat.DEFENSE:
                old = fighter.defense
                new = int(old * mult)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defense = new
                self.display_indicator(fighter, IndicatorType.DEF, change)
            case CharacterStat.ATTACK:
                old = fighter.attack
                new = max(5, int(old * mult))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
            case CharacterStat.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old * mult)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)

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
            score = fighter.ai.preference_weight if target.character.name in fighter.ai.preferred_targets else 1.0
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
            self.upcoming_attacks.append((attack, targets))

        # ! NOTE ! Because all attacks happen after the AI have chosen they behave differently in previous engine
        for fighter, (attack, targets) in zip(self.turn_order, self.upcoming_attacks):
            if attack is None:
                continue
            hit = random.random <= (attack.attack.accuracy / 100.0 * fighter.accuracy / 100.0) and not fighter.dead

            if hit:
                attack.use(self, fighter, targets) # Actually use the fighter's attack so call `damage_fighters`
            else:
                renpy.notify(f"{fighter.character.display_name} missed!")

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
                    print(f"{fighter.name}: {attack.name} now available!")
                else:
                    print(f"{fighter.name}: {attack.name} available in {attack.turns_until_available} turns!")

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
        print("Cannot change HIT POINTS as a status effect")
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


def damage_over_time(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult: float = 1.0,  duration: int = 1):
    """
    Apply damage over time to fighters

    Args:
        mult (float, optional): The multiplier on top of attacker's ATK. Defaults to 1.0.
        duration (int, optional): The number of turns to apply damage. Defaults to 1.
    """
    for target in targets:
        encounter.apply_effect(Effects.BLEED, target, duration, update_override={"damage": fighter.attack * mult})


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


def confuse_targets(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
    """
    Apply the Confusion effect to target fighters
    """
    for target in targets:
        if target.dead:
            continue
        encounter.apply_effect(Effects.CONFUSION, target)

class AITypes:
    NEUTRAL = AI("Neutral")
    AGGRO = AI("Aggro", aggression = 3, tacticity = 0.5, crowd_control = 0.1, heal_threshold = 0.25, heal_chance = 0.25)
    DEFENSIVE = AI("Defensive", heal_threshold = 0.75, tacticity = 3, heal_chance = 0.60)
    SMART = AI("Smart", tacticity = 2, crowd_control = 2, heal_chance = 0.60)
    COPGUY_EX = AI("EX", aggression = 3, tacticity = 2, preferred_targets = ["CS"], heal_chance = 0.70)

class Effects:
    CONFUSION = Effect("Confusion", "Confuse and befuddle!", None, False, 0, apply_func=apply_status_effect, apply_options={"stat": CharacterStat.ACCURACY, "amount": 0.5, "scale": True}, decay_func=decay_chance)
    BLEED = Effect("Bleed", "Bleed them dry!", None, False, 0, update_func=update_damage_over_time)

class Attacks:
    PUNCH = Attack("Punch", "A simple punch.", AttackType.ATTACK, damage_fighters)
    RAW_CHOP = Attack("Raw Chop", "Hiya!", AttackType.ATTACK, damage_fighters) # , ex = False