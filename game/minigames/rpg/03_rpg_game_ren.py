from __future__ import annotations

import renpy
import renpy.random  # type: ignore
import renpy.music  # type: ignore
from renpy.display.core import Displayable
from renpy.display.im import Image
from renpy.display.imagelike import Solid
from renpy.text import Text

# This is the equivalent of a python early block in a .rpy file.
"""renpy
python early:
"""

from copy import deepcopy
from typing import Callable, Literal, Optional
import math

DamageType = Literal["hp", "confusion", "ap", "atk", "none"]
Answer = tuple[int, DamageType]
AnswerList = list[Answer]

DAMAGE_INDICATOR_TIME = 1.0

# https://stackoverflow.com/questions/5189699/how-to-make-a-class-property
class classproperty(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner):
        return self.f(owner)

# Functions
def damage_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    """Damage a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `count: int`: The number of times to hit the targets."""
    mult = options.get("mult", 1)
    count = options.get("count", 1)
    answer = []
    for f in targets:
        if not f.dead:
            for _ in range(count):
                hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
                hit *= 1 - (f.armor_points / 100)
                f.health_points -= hit
                answer.append((int(-hit), "hp"))
                print(f"Dealing {hit} damage to {f.name}.")
        else:
            answer.append((0, "none"))
    return answer

def heal_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    """Heal a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `overheal: bool`: Whether to allow targets to heal over their max health."""
    mult = options.get("mult", 1)
    overheal = options.get("overheal", False)
    answer = []
    for f in targets:
        if not f.dead:
            hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
            f.health_points += hit
            answer.append((int(hit), "hp"))
            if not overheal:
                f.health_points = min(f.health_points, f.max_health)
            print(f"Healing {hit} damage from {f.name}.")
        else:
            answer.append((0, "none"))
    return answer

def damage_over_time(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    """Set a damage over time for a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `turns: int`: The number of turns to hit the targets for."""
    mult = options.get("mult", 1)
    turns = options.get("turns", 1)
    for f in targets:
        f.damage_per_turn.append((subject.attack_points * mult, turns))
        print(f"Added {subject.attack_points * mult} DOT to {f.name} for {turns} turns.")
    return [(0, "none")]

def random_damage_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    """Damage a list of fighters for a value between two multiples..
    Valid options:
    - `min_mult: float`: The minimum multiplier on top of `subject`'s ATK to hit the targets with.
    - `max_mult: float`: The maximum multiplier on top of `subject`'s ATK to hit the targets with."""
    min_mult = options.get("min_mult", 1)
    max_mult = options.get("max_mult", 1)
    mult = max_mult if crit else renpy.random.uniform(min_mult, max_mult)
    answer = []
    for f in targets:
        hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
        hit *= 1 - (f.armor_points / 100)
        f.health_points -= hit
        answer.append((int(-hit), "hp"))
        print(f"Dealing {hit} damage to {f.name}.")
    return answer

def confuse_targets(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    """Confuse a list of targets."""
    answer = []
    for f in targets:
        f.confused = True
        answer.append((1, "confusion"))
        print(f"Confusing {f.name}.")
    return answer

def change_stat(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    """Damage a list of fighters.
    Valid options:
    - `stat: str`: The stat to affect ("hp", "ap", or "atk")
    - `mult: float`: The multiplier on change the stat by."""
    mult = options.get("mult", 1)
    stat = options["stat"]
    answer = []
    for f in targets:
        if stat == "hp":
            old_hp = f.health_points
            f.health_points *= mult
            answer.append((int(f.health_points - old_hp), "hp"))
            print(f"Setting {f.name} HP to {f.health_points}.")
        elif stat == "ap":
            old_ap = f.armor_points
            new_ap = int(f.armor_points * mult)
            if new_ap >= 90:
                if f._funni_ap:
                    if old_ap == 90:
                        new_ap = 95
                    elif old_ap == 95:
                        new_ap = 99
                    elif old_ap == 99:
                        new_ap = 100
                    else:
                        new_ap = old_ap + 1
                else:
                    new_ap = 90
                    f._funni_ap = True
            f.armor_points = new_ap
            answer.append((int(f.armor_points - old_ap), "ap"))
            print(f"Setting {f.name} AP to {f.armor_points}.")
        elif stat == "atk":
            old_atk = f.attack_points
            f.attack_points *= mult
            f.attack_points = max(5, f.attack_points)
            answer.append((int(f.attack_points - old_atk), "atk"))
            print(f"Setting {f.name} ATK to {f.attack_points}.")
        else:
            pass
    return answer

def draw_in(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    mult = options.get("mult", 1)
    answer = []
    attack_type = renpy.random.randint(1, 4)
    # ap up, allies
    if attack_type == 1:
        print("[Draw In] AP Up")
        for f in targets:
            if (f.enemy ^ subject.enemy):
                answer.append((0, "none"))
            else:
                old_ap = f.armor_points
                f.armor_points *= mult
                diff = f.armor_points - old_ap
                answer.append((diff, "ap"))
    # ap down, enemies
    elif attack_type == 2:
        print("[Draw In] AP Down")
        for f in targets:
            if not (f.enemy ^ subject.enemy):
                answer.append((0, "none"))
            else:
                old_ap = f.armor_points
                f.armor_points /= mult
                diff = f.armor_points - old_ap
                answer.append((diff, "ap"))
    # atk up, allies
    elif attack_type == 3:
        print("[Draw In] ATK Up")
        for f in targets:
            if (f.enemy ^ subject.enemy):
                answer.append((0, "none"))
            else:
                old_ap = f.attack_points
                f.attack_points *= mult
                diff = f.attack_points - old_ap
                answer.append((diff, "atk"))
    # ap down, enemies
    elif attack_type == 4:
        print("[Draw In] ATK Down")
        for f in targets:
            if not (f.enemy ^ subject.enemy):
                answer.append((0, "none"))
            else:
                old_ap = f.attack_points
                f.attack_points /= mult
                diff = f.attack_points - old_ap
                answer.append((diff, "atk"))
    return answer

def ai_mimic(subject: Fighter, targets: list[Fighter], crit: bool, options: dict) -> AnswerList:
    if targets[0].name == "Copguy EX":
        aa = [a for a in Attacks.ex_attacks if a.type in ['damage', 'aoe']]
        attack = renpy.random.choice(aa)
    else:
        attack = targets[0].normal
    if attack.name == "AI Mimic":
        attack = Attacks.PUNCH
    print(f"[AI Mimic] running {attack.name}...")
    return attack.run(subject, targets, crit)

class AI:
    def __init__(self,
                 name: str,
                 heal_chance = 0.33,
                 heal_threshold = 0.50,
                 aggression = 1,
                 crowd_control = 1,
                 tacticity = 1,
                 focus: Literal['strong', 'weak'] = None,
                 preferred_targets: list = None,
                 preference_weight = 2) -> None:
        self.name = name
        self.heal_chance = heal_chance  # Skew towards healing attacks
        self.heal_threshold = heal_threshold  # When should I heal
        self.aggression = aggression  # Big bad hit things
        self.crowd_control = crowd_control  # Favors AOE over Single
        self.tacticity = tacticity  # Debuffs and Buffs, aka the Pokemon strat
        self.focus = focus  # Target 'strong' or 'weak'
        self.preferred_targets = [] if preferred_targets is None else preferred_targets  # I wanna smack this boy in particular >:C
        self.preference_weight = preference_weight  # Multiplier how many more times likely to smack this boy

    def run(self, subject: Fighter, encounter: Encounter) -> tuple[list[Fighter], AnswerList]:
        party_status = encounter.enemies if subject.enemy else encounter.allies
        enemy_status = encounter.allies if subject.enemy else encounter.enemies
        # Sort enemies by weak-first
        enemy_status.sort(key = lambda x: (x.health_points * (1 - (x.armor_points / 100))))
        what: Attack = None
        who: list[Fighter] = []
        # i_dont_know = "3rd Base"
        available_attacks = [a for a in subject.attacks if a.available]
        # No attacks to chose?
        if len(available_attacks) == 0:
            return
        # Only one attack to chose.
        elif len(available_attacks) == 1:
            what = available_attacks[0]
        # Choose an attack.
        else:
            # Find minimum party health percentage
            min = subject.health_points/subject.max_health
            for p in party_status:
                if (p.health_points / p.max_health) < min:
                    min = p.health_points / p.max_health

            # Roll a die if we should heal or not.
            if min <= self.heal_threshold:
                heal_time = renpy.random.random() < self.heal_chance
            else:
                heal_time = False
            scores = []

            # If we should heal, make sure we only have healing attacks available.
            if heal_time:
                _old = deepcopy(available_attacks)
                available_attacks = [a for a in available_attacks if a.type == "heal"]
                if len(available_attacks) == 0:
                    available_attacks = _old
                if self.name == "COPGUY_EX":
                    available_attacks = [Attacks.HEAL_EX]
            else:
                available_attacks = [a for a in available_attacks if a.type != "heal"]

            # Weight attack likelyhood.
            for atk in available_attacks:
                score = 1.0
                if atk.type == "damage" or atk.type == "aoe":
                    score *= (self.aggression * atk.options.get("mult", 1))
                elif atk.type == "buff" or atk.type == "debuff" or atk.type == "confuse":
                    score *= self.tacticity
                if atk.type == "aoe":
                    score *= self.crowd_control
                if heal_time:
                    score *= atk.options.get("mult", 1)  # weight towards better heals
                scores.append(score)

            # Choose an attack.
            what = renpy.random.choices(available_attacks, weights = scores)[0]

        # What should be determined before this

        # If it's auto targeting
        if what.target_count == 0:
            target_type = {"enemies": "allies", "allies": "enemies", "all": "all"}[what.target_type]
            who = getattr(encounter, target_type)

        # If the targeting computer is switched off, Luke, are you okay?
        else:
            if what.target_type == "enemies":
                who_staging = encounter.allies if subject.enemy else encounter.enemies
            elif what.target_type == "allies":
                who_staging = encounter.enemies if subject.enemy else encounter.allies
            elif what.target_type == "all":
                who_staging = encounter.fighters
            else:
                who_staging = encounter.allies if subject.enemy else encounter.enemies

            # Choose fighters (weighted)
            weights = []
            for n, f in enumerate(who_staging):
                score = (self.preference_weight if f.name in self.preferred_targets else 1)
                strength = n / len(who_staging)
                if self.focus == "strong":
                    score *= strength
                elif self.focus == "weak":
                    score *= (1 - strength)
                weights.append(score)
            for _ in range(what.target_count):
                who.append(renpy.random.choices(who_staging, weights = weights)[0])
        
        # Run the attack
        answer = what.run(subject, who)
        print(f"[AI: {self.name}] {subject.name} used {what.name} on {sentence_join([t.name for t in who])}...")  # type: ignore
        renpy.notify(f"{subject.display_name} used {what.name} on {sentence_join([t.display_name for t in who])}...")  # type: ignore
        renpy.pause(1.0)
        return who, answer

class AIType:
    NEUTRAL = AI("Neutral")
    AGGRO = AI("Aggro", aggression = 3, tacticity = 0.5, crowd_control = 0, heal_threshold = 0.25, heal_chance = 0.25)
    DEFENSIVE = AI("Defensive", heal_threshold = 0.75, tacticity = 3, heal_chance = 0.60)
    SMART = AI("Smart", tacticity = 2, crowd_control = 2, heal_chance = 0.60)
    COPGUY_EX = AI("EX", aggression = 3, tacticity = 2, preferred_targets = ["CS"], heal_chance = 0.70)

# Objects

class Attack:
    def __init__(self, name: str, description: str, func: Callable[[Fighter, list[Fighter], dict], AnswerList], target_count = 1, target_type: str = "enemies", cooldown: int = 0, used = False, ex = True, **kwargs):
        self.name = name
        self.description = description
        self.func = func
        self.target_count = target_count
        self.target_type = target_type
        self.cooldown = cooldown
        self.ex = ex
        self.options = kwargs

        self.used = used
        self._turns_until_available = 0 if not used else self.cooldown

    def run(self, subject: Fighter, fighters: list[Fighter], crit: bool = False) -> AnswerList:
        self._turns_until_available = self.cooldown
        return self.func(subject, fighters, crit, self.options)

    @property
    def available(self) -> bool:
        return self._turns_until_available == 0

    @property
    def type(self) -> str:
        if self.func == heal_fighters:
            return "heal"
        elif self.func == change_stat and self.options.get("mult", 1) > 1:
            return "buff"
        elif self.func == change_stat:
            return "debuff"
        elif self.target_count == 0 and self.target_type == "enemies":
            return "aoe"
        elif self.func == confuse_targets:
            return "confuse"
        else:
            return "damage"

class ComboAttack:
    def __init__(self, name: str, descripton: str, attacks: list[Attack], ex = True):
        self.name = name
        self.description = descripton
        self.attacks = attacks
        self.ex = ex
        self.used = attacks[0].used

    def run(self, subject: Fighter, fighters: list[Fighter], crit: bool = False) -> AnswerList:
        answer = []
        for a in self.attacks:
            if a.available:
                answer += a.run(subject, fighters, crit)
            else:
                answer.append((0, "none"))
        return answer

    @property
    def _turns_until_available(self) -> int:
        return self.attacks[0]._turns_until_available

    @_turns_until_available.setter
    def _turns_until_available(self, v: int):
        for a in self.attacks:
            a._turns_until_available = v

    @property
    def target_count(self) -> int:
        return self.attacks[0].target_count

    @property
    def target_type(self) -> int:
        return self.attacks[0].target_type

    @property
    def available(self) -> bool:
        return all([a.available for a in self.attacks])

    @property
    def type(self) -> str:
        types = [a.type for a in self.attacks]
        for t in ["heal", "buff", "debuff", "aoe", "confuse"]:
            if t in types:
                return t
        return "damage"

    @property
    def options(self) -> dict:
        return self.attacks[0].options

class Fighter:
    def __init__(self, name: str, enemy: bool, hp: int, ap: int, atk: int, attacks: list[Attack | ComboAttack], sprite: Displayable, multiplier: float = 1, ai: AI = None, display_name: str = None):
        self.name = name
        self.enemy = enemy
        self._health_points = int(hp * multiplier)
        self._max_health = int(hp * multiplier)
        self._armor_points = ap
        self._attack_points = int(atk * multiplier)
        self.attacks = [deepcopy(a) for a in attacks]
        self.ai: AI = ai
        self.sprite = sprite

        self.display_name = name if display_name is None else display_name

        self._funni_ap = False

        self.damage_per_turn: list[tuple] = []
        self.confused: bool = False

    @property
    def health_points(self) -> int:
        return int(self._health_points)

    @health_points.setter
    def health_points(self, v):
        self._health_points = int(v)

    @property
    def max_health(self) -> int:
        return int(self._max_health)

    @max_health.setter
    def max_health(self, v):
        self._max_health = int(v)

    @property
    def armor_points(self) -> int:
        return int(self._armor_points)

    @armor_points.setter
    def armor_points(self, v):
        self._armor_points = int(v)

    @property
    def attack_points(self) -> int:
        return int(self._attack_points)

    @attack_points.setter
    def attack_points(self, v):
        self._attack_points = int(max(1, v))

    @property
    def normal(self) -> Attack:
        return self.attacks[0]

    @property
    def special(self) -> Attack:
        return self.attacks[1] if len(self.attacks) >= 2 else None

    @property
    def psi(self) -> Attack | None:
        return self.attacks[2] if len(self.attacks) >= 3 else None

    def attack(self, style: int, targets: list[Fighter]) -> AnswerList:
        hit = (renpy.random.choice([True, False]) if self.confused else True) and not self.dead
        if hit:
            return self.attacks[style].run(self, targets)
        elif self.confused:
            renpy.notify(f"{self.display_name} is confused!")
            return [(0, "none")]

    def attack_ai(self, encounter: Encounter) -> tuple(list["Fighter"], AnswerList):
        if not self.dead:
            return self.ai.run(self, encounter)
        return ([], [])

    def tick(self) -> AnswerList:
        answer = []
        # DOT
        if self.damage_per_turn:
            for h, t in self.damage_per_turn:
                if t > 0:
                    print(f"{self.name}: Taking {h} DOT damage...")
                    self.health_points -= h
                    answer.append((int(-h), "hp"))
                else:
                    self.damage_per_turn.remove((h, t))
        # Confusion
        if self.confused:
            self.confused = renpy.random.choice([True, False])
            if self.confused:
                print(f"{self.name}: I'm still confused...")
                answer.append((1, "confusion"))
            else:
                print(f"{self.name}: No longer confused!")
                answer.append((0, "confusion"))
        # Cooldowns
        for a in self.attacks:
            report = False
            if a._turns_until_available != 0:
                report = True
            a._turns_until_available -= 1
            a._turns_until_available = max(0, a._turns_until_available)
            if report:
                if a._turns_until_available == 0:
                    print(f"{self.name}: {a.name} now available!")
                else:
                    print(f"{self.name}: {a.name} available in {a._turns_until_available} turns!")
        return answer

    @property
    def dead(self) -> bool:
        return self.health_points <= 0

class Encounter:
    def __init__(self, fighters: list[Fighter], background: Displayable, music: str, scale: float, on_win: str, on_lose: str = "start"):
        self.fighters = [deepcopy(f) for f in fighters if f is not None]
        self.background = background
        self.music = music
        self.scale = scale
        self.on_win = on_win
        self.on_lose = on_lose

        for a in self.allies:
            a.health_points *= scale
            a.max_health *= scale
            a.attack_points *= scale

    @property
    def allies(self) -> list[Fighter]:
        return [f for f in self.fighters if not f.enemy]

    @property
    def enemies(self) -> list[Fighter]:
        return [f for f in self.fighters if f.enemy]

    @property
    def all(self) -> list[Fighter]:
        return self.fighters

    @property
    def turn_order(self) -> list[Fighter]:
        return self.allies + self.enemies

    @property
    def won(self) -> bool | None:
        if len(self.allies) == 0:
            return False
        elif len(self.allies) == 1 and self.allies[0].name == "DB05":
            return False
        elif len(self.enemies) == 0:
            return True
        else:
            return None

    def reset_cooldowns(self):
        for f in self.fighters:
            for a in f.attacks:
                a._turns_until_available = 0 if not a.used else a.cooldown

class Attacks:
    PUNCH = Attack("Punch", "A simple punch.", damage_fighters)
    RAW_CHOP = Attack("Raw Chop", "Hiya!", damage_fighters, ex = False)
    CS_AP_DOWN = Attack("CS AP Down", "Bring AP of an enemy down.", change_stat, stat = "ap", mult = 0.75, ex = False)
    CHOP = ComboAttack("Chop", "Hit an enemy and bring their AP down.", [RAW_CHOP, CS_AP_DOWN])
    RAW_KICK = Attack("Raw Kick", "It's fuckin raw!", damage_fighters, mult = 2, ex = False)
    YTP_MAGIC = Attack("YTP Magic", "Channel the power of YTP!", damage_fighters, cooldown = 10, mult = 20, used = True)
    YTP_MAGIC_NOCOOL = Attack("YTP Magic", "Let no one stand in your way.", damage_fighters, mult = 20, ex = False)
    YTP_HEAL = Attack("Attack.HEAL", "No matter the cost.", heal_fighters, target_count = 0, target_type = "allies", cooldown = 1, mult = 3)
    FUN_VALUE = Attack("Fun Value", "A Dev's favorite attack.", damage_fighters, mult = 10)
    KICK = ComboAttack("Kick", "A stronger attack, and lowers AP.", [RAW_KICK, CS_AP_DOWN])
    BULLET_SPRAY = Attack("Bullet Spray", "Shred all enemies with your LMG!", damage_fighters, target_count = 0, target_type = "enemies", cooldown = 3, mult = 1.5)
    RAW_SLASH = Attack("Raw Slash", "It's fuckin raw!", damage_fighters, ex = False)
    BLEED = Attack("Bleed", "Bleed them dry!", damage_over_time, mult = 0.25, ex = False)
    SLASH = ComboAttack("Slash", "A cutting attack that bleeds out your enemies.", [RAW_SLASH, BLEED])
    LIGHT_CAST = Attack("Light Cast", "A strong blast of light that varies in damage.", random_damage_fighters, cooldown = 3, min_mult = 1, max_mult = 3)
    INSIGHT = Attack("Insight", "Lowers enemy's attack by a little.", change_stat, stat = "atk", mult = 0.75)
    SHOTGUN = Attack("Shotgun", "Blast your enemies twice with a powerful shotgun blast!", damage_fighters, target_count = 2, cooldown = 3, mult = 2)
    ENCOURAGE = Attack("Encourage", "Heal one member with morale!", heal_fighters, target_count = 1, target_type = "allies", mult = 1)
    HIGH_NOON = Attack("High Noon", "Quickly blast 3 targets, or 3 shots on 1!", damage_fighters, target_count = 3, cooldown = 3, mult = 0.75)
    SCRATCH = Attack("Scratch", "A basic scratch attack.", damage_fighters)
    ARMOUR = Attack("Armour", "Boost one's defense!", change_stat, stat = "ap", target_count = 1, target_type = "allies", cooldown = 3, mult = 2.5)
    DAMAGE_SCREM = Attack("Damage Screm", "Yell as loud as possible to deafen your enemies!", damage_fighters, target_count = 0, target_type = "enemies", mult = 0.5)
    SNACK_TIME = Attack("Snack Time", "Heal your team with the power of snacks!", heal_fighters, target_count = 0, target_type = "allies", cooldown = 3, mult = 1)
    ELDRITCH_BLAST = Attack("Eldritch Blast", "An unholy blast that does quite a bit of damage to an enemy.", damage_fighters, mult = 1.5)
    RAINBOW = Attack("Rainbow", "", confuse_targets, cooldown = 3, ex = False)
    VOMIT = Attack("Vomit", "", damage_over_time, cooldown = 3, mult = 1, turns = 3, ex = False)
    RAINBOW_NOCOOL = Attack("Rainbow", "", confuse_targets, ex = False)
    VOMIT_NOCOOL = Attack("Vomit", "", damage_over_time, mult = 1, turns = 3, ex = False)
    RAINBOW_VOMIT = ComboAttack("Rainbow Vomit", "Confuse and damage your enemies with colorful nonsense!", [RAINBOW, VOMIT])
    ROBOPUNCH = Attack("RoboPunch", "A strong punch.", damage_fighters, mult = 1.75)
    HOLOSHIELD = Attack("HoloShield", "Boosts your team's defense by a bit.", change_stat, stat = "ap", target_count = 0, target_type = "allies", cooldown = 3, mult = 1.75)
    MUSIC_BOOST = Attack("Music Boost", "Boost one's defense by a bit.", change_stat, stat = "ap", target_count = 1, target_type = "allies", mult = 1.5)
    RAVE_DEF = Attack("Rave DEF", "Lowers the enemies defense.", change_stat, target_count = 0, target_type = "enemies", stat = "ap", cooldown = 3, mult = 0.5, ex = False)
    RAVE_OFF = Attack("Rave OFF", "Rupture eardrums.", damage_fighters, target_count = 0, target_type = "enemies", cooldown = 3, mult = 0.5, ex = False)
    RAVE = ComboAttack("Rave", "Blast your enemies' eardrums! (Damages enemies while lowering their defense.)", [RAVE_DEF, RAVE_OFF])
    SAMPLE_SPAM = Attack("Sample Spam", "", random_damage_fighters, min_mult = 1, max_mult = 3, mult = 1, ex = False)
    SOUND_BLAST = Attack("Sound Blast", "", damage_fighters, target_count = 0, target_type = "enemies", ex = False)
    SAMPLE_BLAST = ComboAttack("Sample Blast", "Blast your enemies with music! Varies in damage.", [SAMPLE_SPAM, SOUND_BLAST])
    GNOMED = Attack("Gnomed", "Confuse everyone by gnoming them!", confuse_targets, target_count = 0, target_type = "enemies", cooldown = 3)
    NUDGE = Attack("Nudge", "Does either very little or massive damage.", random_damage_fighters, min_mult = 0.1, max_mult = 10, mult = 1)
    DRAW_IN = Attack("Draw in", "Either lowers the enemies stats, or increases your friend's stats!", draw_in, mult = 2)
    CONFIDENCE = Attack("Confidence", "Raise your team's attack!", change_stat, stat = "atk", target_count = 0, target_type = "allies", mult = 1.25)
    PEP_TALK = Attack("Pep Talk", "Raise your team's defense!", change_stat, stat = "ap", target_count = 0, target_type = "allies", mult = 1.25)
    RADS_ATTACK = Attack("RADS Attack", "Inflict radiation on your enemies to kill them over time!", damage_over_time, mult = 0.5)
    AI_MIMIC = Attack("AI Mimic", "Copies an enemy's attack.", ai_mimic, target_count = 1, target_type = "enemies", cooldown = 2)
    SHELL = Attack("Shell", "Fire a tank shell!", random_damage_fighters, min_mult = 1, max_mult = 2)
    HEAL_EX = Attack("Heal EX", "Lots of healing.", heal_fighters, target_count = 0, target_type = "allies", mult = 10)

    # UCN
    STOMP = Attack("Stomp", "Send an earthquake to the enemies!", damage_fighters, target_count = 0, target_type = "enemies", ex = False, mult = 0.75)
    POKE = Attack("Poke", "A mega poke.", damage_fighters, target_count = 1, target_type = "enemies", ex = False, mult = 2.5)
    SWORD = Attack("Sword", "The edge of a sharp thing.", damage_fighters, target_count = 1, target_type = "enemies", ex = False)
    SWORD_AP = Attack("Sword (AP Down)", "The edge of a sharp thing, more.", change_stat, stat = "ap", target_count = 1, target_type = "enemies", mult = 0.75, ex = False)
    SWORD_SLASH = ComboAttack("Sword Slash", "Hit an enemy, and take a chip out of their armor.", [SWORD, SWORD_AP], ex = False)
    FLAMETHROWER = Attack("Flamethrower", "Spray all your enemies with burning fuel!", damage_over_time, target_count = 0, target_type = "enemies", ex = False, mult = 0.5, turns = 3, cooldown = 3)
    CHOCOLATE_CAKE = Attack("Chocolate Cake", "Heal a party member with loads to eat!", heal_fighters, target_type = "allies", ex = False)
    CONFUSING_STORY = Attack("Confusing Story", "Tell a puzzling poem.", confuse_targets, ex = False)
    HYPE_UP = Attack("Hype Up", "Get a team member pumped to fight!", change_stat, target_type = "allies", ex = False, mult = 1.5, stat = "atk")
    PITCHMAN = Attack("Pitchman", "Smooth-talk an enemy's defenses down!", change_stat, target_type = "enemies", ex = False, mult = 0.75, stat = "ap")
    HUG = Attack("Hug", "Hug an enemy (ouch).", damage_fighters, target_count = 1, target_type = "enemies", ex = False, mult = 1.5)
    SPIKE_BOMB = Attack("Spike Bomb", "Release spikes to all enemies!", damage_fighters, target_count = 0, target_type = "enemies", ex = False, mult = 1.5, cooldown = 3)
    SHOT = Attack("Shot", "I'd like to see you outrun bullet.", damage_fighters, target_count = 1, target_type = "enemies", ex = False, mult = 1.5)
    SHOT_AP = Attack("Shot (AP Down)", "Kevlar destroyed.", change_stat, stat = "ap", target_count = 1, target_type = "enemies", mult = 0.75, ex = False)
    PISTOL = ComboAttack("Pistol", "A sharp shot to the chest.", [SHOT, SHOT_AP], ex = False)
    ALL_OVER_AGAIN = Attack("All Over Again", "Ditto.", ai_mimic)
    HEAVY_PUNCH = Attack("Heavy Punch", "A quick blow.", damage_fighters, target_count = 1, target_type = "enemies", ex = False, mult = 1.75)
    SOTH = Attack("Shit On The House", "I'm going to... take a shit on the house.", damage_fighters, target_count = 0, target_type = "enemies", ex = False, mult = 2, cooldown = 3)
    ONE_HUNDRED = Attack("100% Unsatisfied", "Yelp reviews coming in...", change_stat, stat = "atk", target_count = 0, target_type = "enemies", mult = 0.8, ex = False)
    ICE_CREAM = Attack("Ice Cream", "Bing chilling!", heal_fighters, target_count = 0, target_type = "allies", ex = False, mult = 1.5, cooldown = 3)
    RAINBOW_VOMIT_NOCOOL = ComboAttack("Rainbow Vomit", "Why are you like this?", [RAINBOW_NOCOOL, VOMIT_NOCOOL], ex = False)

    @classproperty
    def names(cls) -> list[str]:
        return [a for a in dir(cls) if a.isupper()]

    @classproperty
    def attacks(cls) -> list[Attack]:
        return [cls.__dict__[a] for a in cls.names]

    @classproperty
    def ex_attacks(cls) -> list[Attack]:
        return [a for a in cls.attacks if a.ex is True]

    @classmethod
    def get(cls, k: str, default = None) -> Attack | None:
        return cls.__dict__.get(k, default)

class Fighters:
    NONE = None

    # Allies
    CS = Fighter("CS", False, 188, 10, 25, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"), display_name = "CS")
    CS_NG = Fighter("CS (National Guard)", False, 188, 10, 30, [Attacks.CHOP, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"), display_name = "CS")
    CS_STRONG = Fighter("CS (Strong)", False, 188, 10, 35, [Attacks.KICK, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"), display_name = "CS")
    CS_FINAL = Fighter("CS (Final)", False, 288, 10, 40, [Attacks.KICK, Attacks.BULLET_SPRAY, Attacks.YTP_MAGIC], Image("images/characters/cs/neutral.png"), display_name = "CS")
    CS_FINAL2 = Fighter("CS (Error)", False, 1880, 10, 250, [Attacks.KICK, Attacks.YTP_HEAL, Attacks.YTP_MAGIC_NOCOOL], Image("images/characters/cs/neutral.png"), display_name = "CS")
    CS_WEAK = Fighter("CS (Weak)", False, 188, 5, 25, [Attacks.PUNCH], Image("images/characters/cs/neutral.png"), display_name = "CS")
    CS_ARCHIVAL = Fighter("CS (Archival)", False, 1027, 50, 27, [Attacks.KICK, Attacks.YTP_HEAL], Image("images/characters/cs/neutral.png"), display_name = "CS")
    ARCEUS = Fighter("Arceus", False, 160, 15, 35, [Attacks.SLASH, Attacks.LIGHT_CAST], Image("images/characters/arc/arceus.png"))
    PAKOO = Fighter("Pakoo", False, 145, 20, 30, [Attacks.INSIGHT, Attacks.SHOTGUN], Image("images/characters/pakoo/pakoo.png"))
    MIKA = Fighter("Mika", False, 165, 20, 30, [Attacks.ENCOURAGE, Attacks.HIGH_NOON], Image("images/characters/mika.png"))
    KITTY = Fighter("Kitty", False, 155, 15, 20, [Attacks.SCRATCH, Attacks.ARMOUR], Image("images/characters/kitty.png"))
    TATE = Fighter("Tate", False, 170, 5, 30, [Attacks.DAMAGE_SCREM, Attacks.SNACK_TIME], Image("images/characters/tate/tatehappy.png"))
    ARIA = Fighter("Aria", False, 220, 20, 45, [Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT], Image("images/characters/aria.png"))
    DIGI = Fighter("Digi", False, 150, 20, 30, [Attacks.ROBOPUNCH, Attacks.HOLOSHIELD], Image("images/characters/digi.png"))
    NOVA = Fighter("Nova", False, 170, 5, 30, [Attacks.MUSIC_BOOST, Attacks.RAVE], Image("images/characters/nova.png"))
    BLANK = Fighter("Blank", False, 180, 5, 35, [Attacks.SAMPLE_BLAST, Attacks.GNOMED], Image("images/characters/blank.png"))
    MIDGE = Fighter("Midge", False, 165, 10, 25, [Attacks.NUDGE, Attacks.DRAW_IN], Image("images/characters/midge.png"))
    DB05 = Fighter("DB05", False, 9001, 9001, 50, [Attacks.CONFIDENCE, Attacks.PEP_TALK], Image("images/characters/db.png"))
    ANNO = Fighter("Anno", False, 200, 20, 40, [Attacks.RADS_ATTACK, Attacks.AI_MIMIC], Image("images/characters/anno/anno.png"))

    # Allies (UCN)
    BUBBLE = Fighter("Bubble", False, 250, 10, 35, [Attacks.STOMP, Attacks.POKE], Image("secret/bubble.png"))
    GES = Fighter("Ges", False, 170, 20, 35, [Attacks.SWORD_SLASH, Attacks.FLAMETHROWER], Image("images/characters/ges.png"))
    MICHAEL = Fighter("Michael", False, 155, 15, 35, [Attacks.CHOCOLATE_CAKE, Attacks.CONFUSING_STORY], Image("images/characters/michael.png"))
    BILLY = Fighter("Billy", False, 220, 10, 25, [Attacks.HYPE_UP, Attacks.PITCHMAN], Image("images/characters/billy.png"))
    PHIL = Fighter("Phil", False, 160, 20, 40, [Attacks.HYPE_UP, Attacks.PITCHMAN], Image("images/characters/phil.png"))
    MEAN = Fighter("Mean", False, 150, 20, 35, [Attacks.HUG, Attacks.SPIKE_BOMB], Image("images/characters/mean.png"))
    POMNI = Fighter("Pomni", False, 200, 15, 30, [Attacks.RAINBOW_VOMIT_NOCOOL, Attacks.RAINBOW_VOMIT_NOCOOL], Image("images/secret/pomni.png"))

    # Enemies
    FANBOYA = Fighter("Fanboy (NVIDIA)", True, 50, 0, 16, [Attacks.PUNCH], Image("images/characters/nvidiafanboy.png"), ai = AIType.NEUTRAL, display_name = "Fanboy")
    FANBOYB = Fighter("Fanboy (AMD)", True, 50, 0, 16, [Attacks.PUNCH], Image("images/characters/amdfanboy.png"), ai = AIType.NEUTRAL, display_name = "Fanboy")
    COP = Fighter("Cop", True, 150, 15, 30, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/cop.png"), ai = AIType.NEUTRAL)
    COPGUYGODMODE = Fighter("Copguy (God)", True, 9001, 9001, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/copguy.png"), ai = AIType.NEUTRAL, display_name = "Copguy")
    COPGUY = Fighter("Copguy", True, 300, 20, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/copguy.png"), ai = AIType.NEUTRAL)
    GUARD = Fighter("Guard", True, 225, 25, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/guard_soldier.png"), ai = AIType.DEFENSIVE)
    SML_TANK = Fighter("Sherman", True, 400, 60, 100, [Attacks.SHELL], Image("images/characters/sherman.png"), ai = AIType.AGGRO)
    MARINE = Fighter("Marine", True, 300, 30, 45, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/marine.png"), ai = AIType.SMART)
    BIG_TANK = Fighter("Abrams", True, 700, 70, 150, [Attacks.SHELL], Image("images/characters/abrams.png"), ai = AIType.AGGRO)
    COPGUY_EX = Fighter("Copguy EX", True, 2222, 30, 50, Attacks.ex_attacks, Image("images/characters/copguy.png"), ai = AIType.COPGUY_EX)
    PAKOOE = Fighter("Pakoo (Error)", True, 9999, 70, 150, [Attacks.FUN_VALUE], Image("images/characters/pakoo/pakoo_disappointed.png"), ai = AIType.AGGRO, display_name = "Pakoo")
    K174 = Fighter("K17-4", True, 174, 17, 20, [Attacks.PUNCH], Image("images/characters/k174.png"), ai = AIType.NEUTRAL)
    K199 = Fighter("K19-9", True, 199, 19, 30, [Attacks.KICK], Image("images/characters/k199.png"), ai = AIType.AGGRO)
    K207 = Fighter("K20-7", True, 207, 20, 10, [Attacks.PUNCH], Image("images/characters/k207.png"), ai = AIType.DEFENSIVE)

    # Enemies (UCN)
    WESLEY = Fighter("Wesley", True, 200, 20, 40, [Attacks.PISTOL, Attacks.ALL_OVER_AGAIN], Image("images/characters/wesley.png"), ai = AIType.AGGRO)
    ED = Fighter("Ed", True, 300, 30, 25, [Attacks.HEAVY_PUNCH, Attacks.SOTH], Image("images/characters/ed.png"), ai = AIType.SMART)
    RICHARD = Fighter("Richard", True, 250, 20, 30, [Attacks.ONE_HUNDRED, Attacks.ICE_CREAM], Image("images/characters/rich.png"), ai = AIType.DEFENSIVE)

    @classproperty
    def names(cls) -> list[str]:
        return [f for f in dir(cls) if f.isupper()]

    @classproperty
    def enemy_names(cls) -> list[str]:
        return [f for f in dir(cls) if f.isupper() and f != "NONE" and cls.__dict__[f].enemy]

    @classproperty
    def ally_names(cls) -> list[str]:
        return [f for f in dir(cls) if f.isupper() and f != "NONE" and not cls.__dict__[f].enemy]

    @classproperty
    def fighters(cls) -> list[Fighter]:
        return [cls.__dict__[f] for f in cls.names]

    @classproperty
    def enemies(cls) -> list[Fighter]:
        return [cls.get(f) for f in cls.enemy_names]

    @classproperty
    def allies(cls) -> list[Fighter]:
        return [cls.get(f) for f in cls.ally_names]

    @classmethod
    def get(cls, k: str, default = None) -> Fighter | None:
        return cls.__dict__.get(k, default)


# Dummy encounter to avoid errors
encounter = Encounter([], Image("images/bg/black.png"), "audio/legosfx.mp3", 1, "start", "secret")

# Indicator types
IndicatorType = Literal["heal", "damage", "stat_up", "stat_down", "confused", "unconfused", "none"]

# Damage indicator data storage
class DamageIndicator:
    def __init__(self, answer: Answer, play_sound = True):
        self.value = answer[0]
        self.type = answer[1]
        self.play_sound = play_sound
        self.time_on_screen = 0.0

    @property
    def indicator_type(self) -> IndicatorType:
        if self.type == "none":
            return "none"
        elif self.type == "hp":
            if self.value >= 0:
                return "heal"
            else:
                return "damage"
        elif self.type == "ap" or self.type == "atk":
            if self.value >= 0:
                return "stat_up"
            else:
                return "stat_down"
        elif self.type == "confusion":
            if self.value == 0:
                return "unconfused"
            else:
                return "confused"
        else:
            return "none"

    @property
    def color(self) -> tuple[int, int, int]:
        if self.type == "ap":
            return (0x00, 0x00, 0xFF)
        elif self.type == "atk":
            return (0xFF, 0xFF, 0x00)
        elif self.indicator_type == "unconfused":
            return (0xFF, 0x00, 0xFF)
        elif self.indicator_type == "confused":
            return (0xFF, 0x00, 0xFF)
        elif self.indicator_type == "damage":
            return (0xFF, 0x00, 0x00)
        elif self.indicator_type == "heal":
            return (0x00, 0xFF, 0x00)
        else:
            # This shouldn't happen
            return (0xFF, 0xFF, 0xFF)

    @property
    def text(self) -> str:
        if self.type == "ap":
            return str(self.value) + " AP"
        elif self.type == "atk":
            return str(self.value) + " ATK"
        elif self.indicator_type == "unconfused":
            return "Unconfused!"
        elif self.indicator_type == "confused":
            return "Confused!"
        elif self.indicator_type == "damage":
            return str(abs(self.value))
        elif self.indicator_type == "heal":
            return str(abs(self.value))
        else:
            # This shouldn't happen
            return ""

    def play(self):
        if self.indicator_type == "heal":
            renpy.sound.play("audio/ut/snd_power.wav", channel = "sfx")
            self.play_sound = False
        elif self.indicator_type == "damage":
            renpy.sound.play("audio/ut/snd_damage.wav", channel = "sfx")
            self.play_sound = False
        elif self.indicator_type == "stat_up":
            renpy.sound.play("audio/ut/snd_b.wav", channel = "sfx")
            self.play_sound = False
        elif self.indicator_type == "stat_down":
            renpy.sound.play("audio/ut/snd_bluh.wav", channel = "sfx")
            self.play_sound = False
        elif self.indicator_type == "confused" or self.indicator_type == "unconfused":
            renpy.sound.play("audio/ut/snd_chime.wav", channel = "sfx")
            self.play_sound = False

# This is the displayable that controls what's happening in the boxes at the bottom of the screen
class StatBlockDisplayable(renpy.Displayable):
    def __init__(self, fighter: Fighter):
        self.text_size = 50
        self.fighter = fighter
        self.fighter_name = Text(self.fighter.display_name, color = "#FC8900", size = 50)
        self.health_text = Text("HP: " + str(self.fighter.health_points) + "/" + str(self.fighter.max_health), color = "#FFFFFF", size = self.text_size)
        self.AP_text = Text("AP: " + str(self.fighter.armor_points), color = "#FFFFFF", size = self.text_size)
        self.ATK_text = Text("ATK: " + str(self.fighter.attack_points), color = "#FFFFFF", size = self.text_size)
        self.stat_back = Image("minigames/rpg/statbox.png")
        self.damage_indicators: list[DamageIndicator] = []
        self.size = renpy.image_size(self.stat_back)
        self.damage_indicator_x = int(self.size[0]/2)
        self.damage_indicator_y = int(self.size[1] * 0.01)
        self.damage_size = 50
        self.last_tick = None
        super().__init__(self)

    def show_damage_indicator(self, ans: Answer):
        self.damage_indicators.append(DamageIndicator(ans))

    def render(self, width, height, st, at):
        if self.last_tick is None:
            self.last_tick = st
        dt = st - self.last_tick
        x_al = 25
        y_al = 65
        self.health_text = Text("HP: " + str(self.fighter.health_points) + "/" + str(self.fighter.max_health), color = "#FFFFFF", size = self.text_size)
        self.AP_text = Text("AP: " + str(self.fighter.armor_points), color = "#FFFFFF", size=self.text_size)
        self.ATK_text = Text("ATK: " + str(self.fighter.attack_points), color = "#FFFFFF", size=self.text_size)
        r = renpy.Render(370, 270)
        r.place(self.stat_back)
        r.place(self.fighter_name, x = 25, y = 5)
        r.place(self.health_text, x = x_al, y = y_al)
        r.place(self.AP_text, x = x_al, y = y_al * 2)
        r.place(self.ATK_text, x = x_al, y = y_al * 3)

        for di in self.damage_indicators:
            # Now make the thing
            alpha = ease_linear(255, 0, DAMAGE_INDICATOR_TIME / 2, DAMAGE_INDICATOR_TIME, di.time_on_screen)  # type: ignore
            damage_text_object = Text(di.text, color = di.color + (alpha,), size = self.damage_size)
            # Define position and alpha
            motion = ease_quad(self.damage_indicator_y, self.damage_indicator_y - 50 ,0, DAMAGE_INDICATOR_TIME / 2, di.time_on_screen)  # type: ignore
            r.place(damage_text_object, x = int(self.damage_indicator_x), y = int(motion))
            # Play sounds
            if di.play_sound:
                di.play()

        # Remove expired damage indicators and increase time on screen
        for di in self.damage_indicators:
            di.time_on_screen += dt
            if di.time_on_screen > DAMAGE_INDICATOR_TIME:
                self.damage_indicators.remove(di)

        renpy.redraw(self, 0)
        self.last_tick = st
        return r

    def event(self, ev, x, y, st):
        pass

    def visit(self):
        return [self.health_text, self.AP_text, self.ATK_text, self.stat_back, self.fighter_name]

# These are the enemy displayables. They display the enemy and the enemies health
class EnemyDisplayable(renpy.Displayable):
    def __init__(self, fighter: Fighter):
        self.fighter = fighter
        self.red_part = Solid("#FF0000", xsize = 0, ysize = 0)
        self.green_part = Solid("#00FF00", xsize = 0, ysize = 0)
        self.size = renpy.image_size(self.fighter.sprite)
        self.damage_indicators: list[DamageIndicator] = []
        self.damage_indicator_x = self.size[0] / 2
        self.damage_indicator_y = self.size[1] * 0.01
        self.damage_size = 50
        self.last_tick = None
        self.opacity = 100
        super().__init__(self)

    def show_damage_indicator(self, ans: Answer):
        self.damage_indicators.append(DamageIndicator(ans))

    def render(self, width, height, st, at):
        if self.last_tick is None:
            self.last_tick = st
        dt = st - self.last_tick
        r = renpy.Render(640, self.size[1])
        if self.fighter.name != "Copguy EX":
            if self.damage_indicators:
                if self.damage_indicators[0].indicator_type == "damage":
                    if not math.cos(20*self.damage_indicators[0].time_on_screen)<0:
                        r.place(self.fighter.sprite, x=0, y=0)
                else:
                    r.place(self.fighter.sprite, x=0, y=0)
            else:
                r.place(self.fighter.sprite, x=0, y=0)
        # Making the health bar
        # THIS IS GARBAGE FULL OF MAGIC NUMBERS -- DD
        self.red_part = Solid("#FF0000", xsize = 1920 // 9, ysize = 1920 // 54)
        self.green_part = Solid("#00FF00", xsize = int((1920 // 9) * ((self.fighter.health_points) / (self.fighter.max_health))), ysize = 1920 // 54)
        r.place(self.red_part, x = (self.size[0] // 2) - ((1920 // 9) // 2), y = int(25))
        r.place(self.green_part, x = (self.size[0] // 2) - ((1920 // 9) // 2), y = int(25))

        for di in self.damage_indicators:
            # Now make the thing
            alpha = ease_linear(255, 0, DAMAGE_INDICATOR_TIME / 2, DAMAGE_INDICATOR_TIME, di.time_on_screen)  # type: ignore
            damage_text_object = Text(di.text, color = di.color + (alpha,), size = self.damage_size)
            # Define position and alpha
            motion = ease_quad(self.damage_indicator_y, self.damage_indicator_y - 50 ,0, DAMAGE_INDICATOR_TIME / 2, di.time_on_screen)  # type: ignore
            r.place(damage_text_object, x = int(self.damage_indicator_x), y = int(motion))
            # Play sounds
            if di.play_sound:
                di.play()

        # Remove expired damage indicators
        for di in self.damage_indicators:
            di.time_on_screen += dt
            if di.time_on_screen > DAMAGE_INDICATOR_TIME:
                self.damage_indicators.remove(di)
                # Ensures that the sprite is showing again
                self.opacity = 100

        renpy.redraw(self, 0)
        self.last_tick = st
        return r

    def visit(self):
        return [self.fighter.sprite, self.red_part, self.green_part]

class RPGGameDisplayable(renpy.Displayable):
    def __init__(self, encounter: Encounter):
        self.encounter = encounter
        super().__init__(self)
        self.start_time = None
        self.win = None

        self.enemy_displayables: list[Displayable] = []
        self.statblock_displayables: list[Displayable] = []

        self.reset()

    def reset(self):
        self.start_time = None
        self.win = None

        self.enemy_displayables: list[EnemyDisplayable] = []
        self.statblock_displayables: list[StatBlockDisplayable] = []

        for e in self.encounter.enemies:
            self.enemy_displayables.append(EnemyDisplayable(e))

        for a in self.encounter.allies:
            self.statblock_displayables.append(StatBlockDisplayable(a))

    def render(self, width, height, st, at):
        if self.start_time is None:
            self.start_time = st
        r = renpy.Render(1920, 1080)

        # These are the enemies
        ed = self.enemy_displayables
        if len(ed) == 1:
            ed = [None, ed[0], None]
        elif len(ed) == 2:
            ed = [ed[0], None, ed[1]]
        for i, e in enumerate(ed):
            if e is not None and not e.fighter.dead:
                r.place(e, x = (1920 * (i * 0.33)), y = (1080 - e.size[1]) // 2)

        # This adds in the allies
        for i, s in enumerate(self.statblock_displayables):
            if not s.fighter.dead:
                r.place(s, x = (1920 * (i * 0.25) + 55), y = 810)

        return r

    def event(self, ev, x, y, st):
        import pygame  # type: ignore
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END and preferences.developer_mode:
            for e in self.encounter.enemies:
                e.health_points = 0

    def visit(self):
        return self.enemy_displayables + self.statblock_displayables # Assets needed to load

    def get_displayable_by_fighter(self, fighter: Fighter) -> Optional[EnemyDisplayable | StatBlockDisplayable]:
        valid_displayables = [d for d in self.enemy_displayables + self.statblock_displayables if d.fighter == fighter]
        if valid_displayables:
            return valid_displayables[0]
        return None

rpggame = RPGGameDisplayable(encounter)

# Custom encounter statement

def parse_rpg(lexer):
    lexer.require(":")
    lexer.expect_eol()
    lexer.expect_block("rpg")

    # block
    l = lexer.subblock_lexer()
    while l.advance():
        if l.keyword("bg"):
            bg = l.string()
        elif l.keyword("music"):
            music = l.string()

        # fighters: subblock
        elif l.keyword("fighters"):
            l.expect_block("fighters")
            fighters = []
            ll = l.subblock_lexer()
            while ll.advance():
                fighters.append(ll.rest())
                ll.expect_eol()
        elif l.keyword("scale"):
            scale = l.rest()
    # goto
        elif l.keyword("on_win"):
            label = l.string()
        elif l.keyword("on_lose"):
            label2 = l.string()
    return (bg, music, fighters, scale, label, label2)

def execute_rpg(parsed_object):
    b, m, f, s, l, ll = parsed_object
    global rpggame
    rpggame.encounter = Encounter(
        [getattr(Fighters, globals().get(fighter.replace("$", "")).upper())
         if fighter.startswith("$")
         else getattr(Fighters, fighter.upper()) for fighter in f],
        Image(ucn_bg) if b == "ucn" else Image(b),  # type: ignore
        ucn_music if m == "ucn" else m,  # type: ignore
        ucn_scale if s == "\"ucn\"" else float(s),  # type: ignore
        l,
        ll
    )
    rpggame.reset()
    renpy.jump("play_rpggame")

def lint_rpg(parsed_object):
    # I should probably do this at some point.
    pass


"""
rpg:
    bg "images/bg/X.png"
    music "audio/Y.mp3"
    fighters:
        cs
        cop
        etc...
    on_win "label"
    on_lose "label2"
"""
renpy.register_statement(
    name="rpg",
    parse = parse_rpg,
    lint = lint_rpg,
    execute = execute_rpg,
    block = True)
