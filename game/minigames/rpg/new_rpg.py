from __future__ import annotations

import renpy
from renpy.display.core import Displayable
from renpy import random

# This is the equivalent of a python early block in a .rpy file.
"""renpy
rpy python annotations
python early:
"""
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

# -- STR EUMS --

class ChacterStats(StrEnum):
    HIT_POINTS = "hp"
    ATTACK = "attack"
    DEFENCE = "defence"
    ACCURACY = "accuracy"

class ActionType(StrEnum):
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

class Action:
    """
    An Action (previously Attack) defines what
    a fighter can do on their turn.
    """
    def __init__(
            self,
            name: str,
            description: str,
            typ: ActionType,
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
        self.type: ActionType = typ # typ of attack for AI

        self.func: Callable[..., Any] = func # the function which applies the effects of the action
        self.targets: TargetType = targets # what group of fighters to attack
        self.target_count: int = target_count # how many enemies to target
        self.cooldown: int = cooldown # how many turns to wait on the cool down
        self.accuracy: int = accuracy # percent change of hitting witht the attack
        self.start_used: bool = start_used # whether to start counting down from the beginning of the fight

        self.options: dict[str, Any] = kwds # additionally arguments for Action.func

    def __str__(self) -> str:
        return f"<Attack {self.name}>"

    def __repr__(self) -> str:
        return self.__str__()

class ComboAction:
    """
    A ComboAction (previously ComboAttack) has multiple actions
    that work together.

    TODO: add ability to choose different targets for different actions
    """

    def __init__(
            self,
            name: str,
            description: str,
            typ: ActionType,
            actions: Sequence[Action],
            targets: TargetType | None = None,
            cooldown: int | None = None,
            accuracy: int | None = None,
            start_used: bool | None = None,
            shared_targets: bool = False, # TODO: use to allow for mixed targetting
            ):
        self.name: str = name
        self.description: str = description
        self.type: ActionType = typ

        self.actions = actions # What actions to run through

        # Same as normal Attack
        self.targets: TargetType = self.actions[0].targets if targets is None else targets
        self.cooldown: int = self.actions[0].cooldown if cooldown is None else cooldown
        self.accuracy: int = self.actions[0].accuracy if accuracy is None else accuracy
        self.start_used: bool = self.actions[0].start_used if start_used is None else start_used

        # Empty options dict
        self.options: dict[str, Any] = {}

    def func(self, encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], **kwds):
        for action in self.actions:
            action.func(encounter, fighter, targets, **action.options)

    def __str__(self) -> str:
        return f"<ComboAttack {self.name} ({self.attacks})>"

    def __repr__(self) -> str:
        return self.__str__()

class Effect:
    """
    An Effect happens over multiple turns and
    is controlled by the encounter. Actions
    and Fighters can spawn effects, and
    encounters can have passive background
    effects.
    """

    def __init__(
            self,
            name: str,
            description: str,
            icon: Displayable,
            positive: bool,
            duration: int = 0,
            apply_func: Callable[..., Any] | None = None,
            update_func: Callable[..., Any] | None = None,
            decay_func: Callable[..., bool] | None = None,
            apply_options: dict[str, Any] = {},
            update_options: dict[str, Any] = {},
            decay_options: dict[str, Any] = {}
            ):
        self.name: str = name
        self.description: str = description
        self.icon: Displayable = icon # Icon to show
        self.positive: bool = positive # whether the effect is considered helpful for 'cleanse' effects
        self.duration: int = duration # How many turns does the effect last? If 0 then forever.

        self.apply = apply_func # What happens when the effect is applied
        self.update = update_func # What happens every turn the effect is applied
        self.decay = decay_func # Should the effect end other than the duration ending

        self.apply_options = apply_options # Additional arguments when applying the effect
        self.update_options = update_options # Additonal arguments when updating the effect
        self.decay_options = decay_options # Additional arguments when decaying the effect

class AI:
    """
    The logic that decides what a fighter will
    do each turn. Uses the information provided
    by the encounter to decide on an Action.
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

    def choose_action(self, encounter: Encounter, subject: Fighter) -> FighterAction | None:
        party = encounter.enemies if subject.enemy else encounter.allies
        enemies = encounter.allies if subject.enemy else encounter.enemies

        # Sort enemies by weak-first
        enemies = sorted(enemies, key = lambda x: (x.hit_points * (1.0 - (x.defence / 100.0))))

        print(f"{subject.name}: Choosing an attack...")

        available_attacks = tuple(a for a in subject.actions if a.available)

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
            if atk.type == ActionType.ATTACK or atk.type == ActionType.AOE:
                score *= (self.aggression * atk.options.get("mult", 1.0))
            elif atk.type == ActionType.BUFF or atk.type == ActionType.DEBUFF or atk.type == ActionType.EFFECT:
                score *= self.tacticity
            if atk.type == ActionType.AOE:
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

    def __init__(self, name: str, base_hp: int, base_def: int, base_atk: int, base_acc: int, attacks: Sequence[Action | ComboAction], sprite: Displayable, display_name: str | None = None):
        self.name: str = name
        self.display_name: str = display_name or name

        self.base_hp: int = base_hp # how much hp will the fighter start with, and what is their max hp
        self.base_def: int = base_def # how much defence will the fighter start with
        self.base_atk: int = base_atk # how much attack will the fighter start with
        self.base_acc: int = base_acc # how accurate will the fighter start with

        self.attacks: Sequence[Action | ComboAction] = attacks # What attacks can the character use
        self.sprite: Displayable = sprite # What image should represent the character

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
            opponent: bool,
            level: float = 1.0,
            ai: AI | None = None,
            hp_override: int | None = None,
            def_override: int | None = None,
            atk_override: int | None = None,
            acc_override: int | None = None
        ): # TODO: consider -- would it be worth to add a sprite override and a display_name override? (and a max_hp override)

        self.character: Character = character # The stat basis for the character
        self.opponent: bool = opponent # What team is the fighter on
        self.level: float = level # What level is the fighter? Was originally the scale passed in the encounter
        self.ai: AI | None = ai # What AI does the fighter use. If none the encouter defers to the player

        self.max_hp: int = int(character.base_hp * level) # Maximum hitpoints of a character
        self.hit_points: int = int(level * (character.base_hp if hp_override is None else hp_override))

        self.base_def: int = int(level * (character.base_def if def_override is None else def_override)) # percect of incoming damage reduced
        self.defence: int = self.base_def
        self.base_atk: int = int(level * (character.base_atk if atk_override is None else atk_override)) # Base amount of damage fighter does
        self.attack: int = self.base_atk
        self.base_acc: int = int(level * (character.base_acc if acc_override is None else acc_override)) # Percent change for fighter to hit (usually 100%)
        self.accuracy: int = self.base_acc

        # The actions this fighter can do, and when they can use them next
        self.actions: tuple[FighterAction, ...] = tuple(FighterAction(action) for action in self.character.attacks)
        self.next_action: FighterAction | None = None
        self.next_targets: tuple[Fighter, ...] = ()

        self.effects: list[FighterEffect] = []

    def reset_effects(self):
        self.defence = self.base_def
        self.attack = self.base_atk
        self.accuracy = self.base_acc

    @property
    def dead(self) -> bool:
        return self.hit_points <= 0


class FighterAction:
    """
    The tracker for when an action can used
    by the figher that owns it
    """

    def __init__(self, action: Action):
        self.action: Action = action

        self.used: bool = action.start_used
        self.turns_until_available: int = 0 if not action.start_used else action.cooldown

    def use(self, encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]) -> None:
        self.turns_until_available = self.action.cooldown
        self.action.func(encounter, fighter, targets, **self.action.options)

    @property
    def name(self) -> str:
        return self.action.name

    @property
    def type(self) -> ActionType:
        return self.action.type

    @property
    def options(self) -> dict[str, Any]:
        return self.action.options

    @property
    def available(self) -> bool:
        return self.turns_until_available == 0


class FighterEffect:
    """
    The tracker for when an effect has been used
    each fighter has their own list of FighterEffects
    """
    def __init__(self, effect: Effect, fighter: Fighter, start_turn: int, duration_override: int | None = None):
        self.effect: Effect = effect
        self.fighter: Fighter = fighter
        self.start_turn: int = start_turn
        self.duration = effect.duration if duration_override is None else duration_override

    def apply(self, encounter: Encounter) -> None:
        if self.effect.apply is None:
            return
        self.effect.apply(encounter, self.fighter, **self.effect.apply_options)

    def update(self, encounter: Encounter) -> None:
        if self.effect.update is None:
            return
        self.effect.update(encounter, self.fighter, **self.effect.update_options)

    def decay(self, encounter: Encounter) -> bool:
        if self.duration != 0 and self.start_turn + self.duration <= encounter.turn:
            return True
        if self.effect.decay is None:
            return False
        return self.effect.decay(encounter, self.fighter, **self.effect.decay_options)


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

        self.global_effects: list[Effect] = [] # TODO: better handle global effects because this just slowly fills up

    @property
    def allies(self) -> tuple[Fighter, ...]:
        return tuple(fighter for fighter in self.fighters if not fighter.opponent)

    @property
    def enemies(self) -> tuple[Fighter, ...]:
        return tuple(fighter for fighter in self.fighters if fighter.opponent)

    @property
    def turn_order(self) -> tuple[Fighter, ...]:
        return self.allies + self.enemies

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

    def display_indicator(self, target: Displayable, type: IndicatorType, amount: int = 0): # TODO: hook up real indicators
        if amount:
            print("Displaying {amount}x{type} on {target}")
        else:
            print("Displaying {type} on {target}")

    def damage_fighter(self, fighter: Fighter, damage: float, roll_crit: bool | None = None, ignore_armour: bool = False):
        # We only let the player's fighter roll crit by default. If roll_crit is None then we decide based on that.
        roll_crit = not fighter.opponent if roll_crit is None else roll_crit
        if roll_crit and random.random <= CRIT_CHANCE:
            damage = damage * 1.5

        if not ignore_armour:
            fraction = fighter.defence / 100.0
            damage = damage * (1.0/16.0)**(fraction*fraction) # this makes it so 0 defence is 100%, 50 is 50%, but 100 isn't 0%

        fighter.hit_points -= int(damage)

        self.display_indicator(fighter, IndicatorType.HP, int(-damage))

    def heal_fighter(self, fighter: Fighter, amount: float, overheal: bool = False):
        fighter.hit_points += int(amount)
        if not overheal:
            fighter.hit_points = min(fighter.hit_points, fighter.max_hp)
        self.display_indicator(fighter, IndicatorType.HP, int(amount))

    def apply_effect(self, effect: Effect, fighter: Fighter | None = None, duration_override: int | None = None, silent: bool = False):
        if fighter is None: # apply to all fighters
            self.global_effects = effect
            for fighter in self.fighters:
                self.apply_effect(effect, fighter, duration_override)
            return

        fighter.effects.append(FighterEffect(effect, fighter, self.turn, duration_override))

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

    def modify_fighter(self, fighter: Fighter, stat: ChacterStats, amount: float, permanent: bool = True):
        match stat:
            case ChacterStats.HIT_POINTS:
                old = fighter.hit_points
                new = int(old + amount)
                fighter.hit_points = new
                self.display_indicator(fighter, IndicatorType.HP, new - old)
            case ChacterStats.DEFENCE:
                old = fighter.defence
                new = int(old + amount)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defence = new
                self.display_indicator(fighter, IndicatorType.DEF,change)
            case ChacterStats.ATTACK:
                old = fighter.attack
                new = max(5, int(old + amount))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
            case ChacterStats.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old + amount)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)

    def scale_fighter(self, fighter: Fighter, stat: ChacterStats, mult: float, permanent: bool = True):
        match stat:
            case ChacterStats.HIT_POINTS:
                old = fighter.hit_points
                new = int(old * mult)
                fighter.hit_points = new
                self.display_indicator(fighter, IndicatorType.HP, new - old)
            case ChacterStats.DEFENCE:
                old = fighter.defence
                new = int(old * mult)
                change = new - old
                if permanent:
                    fighter.base_def = fighter.base_def + change
                fighter.defence = new
                self.display_indicator(fighter, IndicatorType.DEF, change)
            case ChacterStats.ATTACK:
                old = fighter.attack
                new = max(5, int(old * mult))
                change = new - old
                if permanent:
                    fighter.base_atk = max(5, int(fighter.base_atk + change))
                fighter.attack = new
                self.display_indicator(fighter, IndicatorType.ATK, change)
            case ChacterStats.ACCURACY:
                old = fighter.accuracy
                new = max(0, min(100, int(old * mult)))
                change = new - old
                if permanent:
                    fighter.base_acc = max(0, min(100, fighter.base_acc + change))
                fighter.accuracy = new
                self.display_indicator(fighter, IndicatorType.ACC, change)

    def choose_fighters(self, fighter: Fighter, action: Action) -> tuple[Fighter, ...]:
        if fighter.ai is None:
            return ()

        # Return self when action type is SELF, this may never happen depending on the AI
        if action.targets == TargetType.SELF:
            return (fighter, )


        match action.targets:
            case TargetType.ALLY:
                possible_targets = self.enemies if fighter.opponent else self.allies
            case TargetType.All:
                possible_targets = self.fighters
            case _:
                possible_targets = self.allies if fighter.opponent else self.enemies

        # Shortcut and return all the possible targets when the count is 0
        if action.target_count == 0:
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

        return tuple(random.choices(possible_targets, weights)[0] for _ in range(action.target_count))

    # These are seperate so that we can see the consequences of the player applying the defend effect etc
    def run_actions(self):
        # run once every actor has chosen their next action
        # Do the action of every fighter and tick their attacks
        for fighter in self.turn_order:
            action = fighter.next_action
            targets = fighter.next_targets
            if action is None:
                if fighter.ai is None:
                    # player has not picked an action for this fighter so they just defend.
                    continue # TODO: give fighter defend action once it is created
                else:
                    if fighter.dead: # Dead AI fighters don't get to act
                        continue
                    # fighter has not picked action and has an AI
                    action = fighter.ai.choose_action(self, fighter)
                    if action is None:
                        continue # Still no action
                    targets = self.choose_fighters(fighter, action)

            hit = random.random <= (action.action.accuracy / 100.0 * fighter.accuracy / 100.0) and not fighter.dead

            if hit:
                action.use(self, fighter, targets)
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
            fighter.next_action = None
            fighter.next_targets = ()
            # cool downs
            for action in fighter.actions:
                if action.available:
                    continue
                action.turns_until_available -= 1
                if action.turns_until_available == 0:
                    print(f"{fighter.name}: {action.name} now available!")
                else:
                    print(f"{fighter.name}: {action.name} available in {action.turns_until_available} turns!")

            if fighter.dead:
                self.fighters.remove(fighter)
                fighter.effects = ()
        self.turn += 1

    def __str__(self) -> str:
        return f"<Encounter {self.allies} vs {self.enemies}>"

    def __repr__(self) -> str:
        return self.__str__()

# |---- RPG Content ----|

# -- Action Functions --
def damage_fighters(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult: float = 1.0, count: int = 1):
    """
    Damage the target fighters

    Options:
        mult (float, optional): The multiplier on top of attacker's ATK. Defaults to 1.0.
        count (int, optional): number of times to apply damage. Defaults to 1.
    """
    for target in targets:
        if target.dead:
            continue
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


class Actions:
    PUNCH = Action("Punch", "A simple punch.", damage_fighters)
    RAW_CHOP = Action("Raw Chop", "Hiya!", damage_fighters) # , ex = False
