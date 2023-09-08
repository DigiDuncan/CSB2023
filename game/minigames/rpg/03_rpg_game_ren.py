from __future__ import annotations

import renpy
import renpy.random  # noqa
from renpy.display.core import Displayable
from renpy.display.im import Image
from renpy.display.imagelike import Solid
from renpy.text import Text

"""renpy
python early:
"""

from copy import copy
from typing import Callable, Literal

# Functions
def damage_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Damage a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `count: int`: The number of times to hit the targets."""
    mult = options.get("mult", 1)
    count = options.get("count", 1)
    for f in targets:
        if not f.dead:
            for _ in range(count):
                hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
                hit *= 1 - (f.armor_points / 100)
                f.health_points -= hit
                print(f"Dealing {hit} damage to {f.name}.")

def heal_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Heal a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `overheal: bool`: Whether to allow targets to heal over their max health."""
    mult = options.get("mult", 1)
    overheal = options.get("overheal", False)
    for f in targets:
        if not f.dead:
            hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
            hit *= 1 - (f.armor_points / 100)
            f.health_points += hit
            if not overheal:
                f.health_points = min(f.health_points, f.max_health)
        print(f"Healing {hit} damage from {f.name}.")

def damage_over_time(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Set a damage over time for a list of fighters.
    Valid options:
    - `mult: float`: The multiplier on top of `subject`'s ATK to hit the targets with.
    - `turns: int`: The number of turns to hit the targets for."""
    mult = options.get("mult", 1)
    turns = options.get("turns", 1)
    for f in targets:
        f.damage_per_turn.append((subject.attack_points * mult, turns))
        print(f"Added {subject.attack_points * mult} DOT to {f.name} for {turns} turns.")

def random_damage_fighters(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Damage a list of fighters for a value between two multiples..
    Valid options:
    - `min_mult: float`: The minimum multiplier on top of `subject`'s ATK to hit the targets with.
    - `max_mult: float`: The maximum multiplier on top of `subject`'s ATK to hit the targets with."""
    min_mult = options.get("min_mult", 1)
    max_mult = options.get("max_mult", 1)
    mult = max_mult if crit else renpy.random.uniform(min_mult, max_mult)
    for f in targets:
        hit = subject.attack_points * mult * 1.5 if crit else subject.attack_points * mult
        hit *= 1 - (f.armor_points / 100)
        f.health_points -= hit
        print(f"Dealing {hit} damage to {f.name}.")

def confuse_targets(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Confuse a list of targets."""
    for f in targets:
        f.confused = True
        print(f"Confusing {f.name}.")

def change_stat(subject: Fighter, targets: list[Fighter], crit: bool, options: dict):
    """Damage a list of fighters.
    Valid options:
    - `stat: str`: The stat to affect ("hp", "ap", or "atk")
    - `mult: float`: The multiplier on change the stat by."""
    mult = options.get("mult", 1)
    stat = options["stat"]

    for f in targets:
        if stat == "hp":
            f.health_points *= mult
            print(f"Setting {f.name} HP to {f.health_points}.")
        elif stat == "ap":
            old_ap = f.armor_points
            new_ap = int(f.armor_points * mult)
            if new_ap >= 99:
                if f._funni_ap:
                    new_ap = old_ap + 1
                else:
                    new_ap = 99
                    f._funni_ap = True
            f.armor_points = new_ap
            print(f"Setting {f.name} AP to {f.armor_points}.")
        elif stat == "atk":
            f.attack_points *= mult
            print(f"Setting {f.name} ATK to {f.attack_points}.")
        else:
            pass

class AI:
    def __init__(self,
                 heal_chance = 0.50,
                 heal_threshold = 0.50,
                 aggression = 1,
                 crowd_control = 1,
                 tacticity = 1,
                 focus: Literal['strong', 'weak'] = None,
                 preferred_targets: list = None,
                 preference_weight = 2) -> None:
        self.heal_chance = heal_chance # If 0 Never heals, 1 Will ALWAYS attempt to heal below heal_threshold
        self.heal_threshold = heal_threshold # When should I heal
        self.aggression = aggression # Big bad hit things
        self.crowd_control = crowd_control # Favors AOE over Single
        self.tacticity = tacticity # Debuffs and Buffs, aka the Pokemon strat
        self.focus = focus # Target 'strong' or 'weak'
        self.preferred_targets = [] if preferred_targets is None else preferred_targets # I wanna smack this boy in particular >:C
        self.preference_weight = preference_weight # Multiplier how many more times likely to smack this boy

    def run(self, subject: Fighter, encounter: Encounter) -> None:
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
            min = subject.health_points/subject.max_health
            for p in party_status:
                if (p.health_points / p.max_health) < min:
                    min = p.health_points / p.max_health
            scores = []
            for atk in available_attacks:
                score = 1
                if atk.type == "heal":
                    if not min < self.heal_threshold:
                        score = 0
                    else:
                        score = 1
                elif atk.type == "damage" or atk.type == "aoe":
                    score *= self.aggression
                elif atk.type == "buff" or atk.type == "debuff" or atk.type == "confuse":
                    score *= self.tacticity
                if atk.type == "aoe":
                    score *= self.crowd_control
                if atk.type == "heal" and min > self.heal_threshold:
                    score *= self.heal_chance
                elif min > self.heal_threshold:
                    score *= 1 - self.heal_chance
                scores.append(score)
            print("===SCORES===")
            for a, s in list(zip(available_attacks, scores)):
                print(f"{a.name}:", s)
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
                print("???")
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
        what.run(subject, who)
        print(f"[AI] {subject.name} running attack {what.name} on {[t.name for t in who]}...")
        renpy.notify(f"{subject.name} running attack {what.name} on {[t.name for t in who]}...")
        renpy.pause(1.0)

class AIType:
    NEUTRAL = AI()
    AGGRO = AI(aggression = 3, tacticity = 0.5, crowd_control = 0, heal_threshold = 0.25)
    DEFENSIVE = AI(heal_threshold = 0.75, tacticity = 3)
    SMART = AI(tacticity = 2, crowd_control = 2)
    COPGUY_EX = AI(aggression = 3, tacticity = 2, preferred_targets = ["CS"])

# Objects

class Attack:
    def __init__(self, name: str, func: Callable[[Fighter, list[Fighter], dict], None], target_count = 1, target_type: str = "enemies", cooldown: int = 0, used = False, **kwargs):
        self.name = name
        self.func = func
        self.target_count = target_count
        self.target_type = target_type
        self.cooldown = cooldown
        self.options = kwargs

        self._turns_until_available = 0 if not used else self.cooldown

    def run(self, subject: Fighter, fighters: list[Fighter], crit: bool = False):
        self.func(subject, fighters, crit, self.options)
        self._turns_until_available = self.cooldown

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
    def __init__(self, name: str, attacks: list[Attack]):
        self.name = name
        self.attacks = attacks

    def run(self, subject: Fighter, fighters: list[Fighter], crit: bool = False):
        for a in self.attacks:
            if a.available:
                a.run(subject, fighters, crit)

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

class Fighter:
    def __init__(self, name: str, enemy: bool, hp: int, ap: int, atk: int, attacks: list[Attack | ComboAttack], sprite: Displayable, multiplier: float = 1, ai: AI = None):
        self.name = name
        self.enemy = enemy
        self._health_points = int(hp * multiplier)
        self._max_health = int(hp * multiplier)
        self._armor_points = ap
        self._attack_points = int(atk * multiplier)
        self.attacks = [copy(a) for a in attacks]
        self.ai: AI = ai
        self.sprite = sprite

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
        self._attack_points = int(v)

    @property
    def normal(self) -> Attack:
        return self.attacks[0]

    @property
    def special(self) -> Attack:
        return self.attacks[1] if len(self.attacks) >= 2 else None

    @property
    def psi(self) -> Attack | None:
        return self.attacks[2] if len(self.attacks) >= 3 else None

    def attack(self, style: int, targets: list[Fighter]):
        hit = (renpy.random.choice([True, False]) if self.confused else True) and not self.dead
        if hit:
            self.attacks[style].run(self, targets)
        elif self.confused:
            renpy.notify(f"{self.name} is confused!")

    def attack_ai(self, encounter: Encounter):
        if not self.dead:
            self.ai.run(self, encounter)

    def tick(self):
        # DOT
        if self.damage_per_turn:
            for h, t in self.damage_per_turn:
                if t > 0:
                    print(f"{self.name}: Taking {h} DOT damage...")
                    self.health_points -= h
                else:
                    self.damage_per_turn.remove((h, t))
        # Confusion
        if self.confused:
            self.confused = renpy.random.choice([True, False])
            if self.confused:
                print(f"{self.name}: I'm still confused...")
            else:
                print(f"{self.name}: No longer confused!")
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

    @property
    def dead(self) -> bool:
        return self.health_points <= 0

class Encounter:
    def __init__(self, fighters: list[Fighter], background: Displayable, music: str, scale: float, on_win: str, on_lose: str = "start"):
        self.fighters = [copy(f) for f in fighters]
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
        elif len(self.enemies) == 0:
            return True
        else:
            return None

class Attacks:
    PUNCH = Attack("Punch", damage_fighters)
    RAW_CHOP = Attack("Raw Chop", damage_fighters)
    CS_AP_DOWN = Attack("CS AP Down", change_stat, stat = "ap", mult = 0.75)
    CHOP = ComboAttack("Chop", [RAW_CHOP, CS_AP_DOWN])
    RAW_KICK = Attack("Raw Kick", damage_fighters, mult = 3)
    YTP_MAGIC = Attack("YTP Magic", damage_fighters, cooldown = 10, mult = 20, used = True)
    KICK = ComboAttack("Kick", [RAW_KICK, CS_AP_DOWN])
    BULLET_SPRAY = Attack("Bullet Spray", damage_fighters, target_count = 0, target_type = "enemies", cooldown = 3, mult = 1.5)
    RAW_SLASH = Attack("Raw Slash", damage_fighters)
    BLEED = Attack("Bleed", damage_over_time, mult = 0.25)
    SLASH = ComboAttack("Slash", [RAW_SLASH, BLEED])
    LIGHT_CAST = Attack("Light Cast", random_damage_fighters, cooldown = 3, min_mult = 1, max_mult = 1, mult = 3)
    INSIGHT = Attack("Insight", change_stat, stat = "atk", mult = 0.75)
    SHOTGUN = Attack("Shotgun", damage_fighters, target_count = 2, cooldown = 3, mult = 2)
    ENCOURAGE = Attack("Encourage", heal_fighters, target_count = 0, target_type = "allies", mult = 3)
    HIGH_NOON = Attack("High Noon", damage_fighters, target_count = 3, cooldown = 3, mult = 1)
    SCRATCH = Attack("Scratch", damage_fighters)
    ARMOUR = Attack("Armour", change_stat, stat = "ap", target_count = 0, target_type = "allies", cooldown = 3, mult = 2.5)
    DAMAGE_SCREM = Attack("Damage Screm", damage_fighters, target_count = 0, target_type = "enemies", mult = 0.5)
    SCREM = Attack("Screm", heal_fighters, target_count = 0, target_type = "allies", cooldown = 3, mult = 1)
    ELDRITCH_BLAST = Attack("Eldritch Blast", damage_fighters, mult = 1.5)
    RAINBOW = Attack("Rainbow", confuse_targets, cooldown = 3)
    VOMIT = Attack("Vomit", damage_over_time, cooldown = 3, mult = 1, turns = 3)
    RAINBOW_VOMIT = ComboAttack("Rainbow Vomit", [RAINBOW, VOMIT])
    ROBOPUNCH = Attack("RoboPunch", damage_fighters, mult = 1.75)
    HOLOSHIELD = Attack("HoloShield", change_stat, stat = "ap", target_count = 0, target_type = "allies", cooldown = 3, mult = 2)
    MUSIC_BOOST = Attack("Music Boost", change_stat, stat = "ap", target_count = 0, target_type = "allies", mult = 1.5)
    RAVE = Attack("Rave", change_stat, stat = "ap", cooldown = 3, mult = 0.5)
    SAMPLE_SPAM = Attack("Sample Spam", random_damage_fighters, min_mult = 1, max_mult = 3, mult = 1)
    SOUND_BLAST = Attack("Sound Blast", damage_fighters, target_count = 0, target_type = "enemies")
    SAMPLE_BLAST = ComboAttack("Sample Blast", [SAMPLE_SPAM, SOUND_BLAST])
    GNOMED = Attack("Gnomed", confuse_targets, target_count = 0, target_type = "enemies", cooldown = 3)
    NUDGE = Attack("Nudge", random_damage_fighters, min_mult = 0.1, max_mult = 10, mult = 1)
    DRAW_IN = Attack("Draw in", change_stat, stat = "atk", target_count = 0, target_type = "allies", cooldown = 3, mult = 2)  # fuck this
    CONFIDENCE = Attack("Confidence", change_stat, stat = "atk", target_count = 0, target_type = "allies", mult = 1.5)
    PEP_TALK = Attack("Pep Talk", change_stat, stat = "ap", target_count = 0, target_type = "allies", mult = 1.5)
    RADS_ATTACK = Attack("RADS Attack", damage_over_time, mult = 0.5)
    AI_MIMIC = Attack("AI Mimic", confuse_targets, target_count = 0, target_type = "enemies", cooldown = 3, mult = 1)  # copy attack
    SHELL = Attack("Shell", random_damage_fighters, min_mult = 1, max_mult = 2, mult = 1)

class Fighters:
    CS = Fighter("CS", False, 188, 10, 25, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"))
    CS_NG = Fighter("CS", False, 188, 10, 25, [Attacks.CHOP, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"))
    CS_STRONG = Fighter("CS", False, 188, 10, 25, [Attacks.KICK, Attacks.BULLET_SPRAY], Image("images/characters/cs/neutral.png"))
    CS_FINAL = Fighter("CS", False, 188, 10, 25, [Attacks.KICK, Attacks.BULLET_SPRAY, Attacks.YTP_MAGIC], Image("images/characters/cs/neutral.png"))
    CS_WEAK = Fighter("CS", False, 188, 5, 25, [Attacks.PUNCH], Image("images/characters/cs/neutral.png"))
    ARCEUS = Fighter("Arceus", False, 160, 15, 35, [Attacks.SLASH, Attacks.LIGHT_CAST], Image("images/characters/arc/arceus.png"))
    PAKOO = Fighter("Pakoo", False, 145, 20, 30, [Attacks.INSIGHT, Attacks.SHOTGUN], Image("images/characters/pakoo.png"))
    MIKA = Fighter("Mika", False, 165, 20, 30, [Attacks.ENCOURAGE, Attacks.HIGH_NOON], Image("images/characters/mika.png"))
    KITTY = Fighter("Kitty", False, 155, 15, 20, [Attacks.SCRATCH, Attacks.ARMOUR], Image("images/characters/kitty.png"))
    TATE = Fighter("Tate", False, 170, 5, 30, [Attacks.DAMAGE_SCREM, Attacks.SCREM], Image("images/characters/tate.png"))
    ARIA = Fighter("Aria", False, 200, 20, 45, [Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT], Image("images/characters/aria.png"))
    DIGI = Fighter("Digi", False, 170, 20, 30, [Attacks.ROBOPUNCH, Attacks.HOLOSHIELD], Image("images/characters/digi.png"))
    NOVA = Fighter("Nova", False, 170, 5, 30, [Attacks.MUSIC_BOOST, Attacks.RAVE], Image("images/characters/nova.png"))
    BLANK = Fighter("Blank", False, 180, 5, 35, [Attacks.SAMPLE_BLAST, Attacks.GNOMED], Image("images/characters/blank.png"))
    MIDGE = Fighter("Midge", False, 165, 10, 25, [Attacks.NUDGE, Attacks.DRAW_IN], Image("images/characters/midge.png"))
    DB05 = Fighter("Db05", False, 9001, 9001, 50, [Attacks.CONFIDENCE, Attacks.PEP_TALK], Image("images/characters/db.png"))
    ANNO = Fighter("Anno", False, 220, 30, 40, [Attacks.RADS_ATTACK, Attacks.AI_MIMIC], Image("images/characters/anno.png"))

    FANBOYA = Fighter("Fanboy",True, 50, 0, 16, [Attacks.PUNCH], Image("images/characters/nvidiafanboy.png"), ai = AIType.NEUTRAL)
    FANBOYB = Fighter("Fanboy",True, 50, 0, 16, [Attacks.PUNCH], Image("images/characters/amdfanboy.png"), ai = AIType.NEUTRAL)
    COP = Fighter("Cop", True, 150, 15, 30, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/cop.png"), ai = AIType.NEUTRAL)
    COPGUYGODMODE = Fighter("Copguy", True, 9001, 9001, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/copguy.png"), ai = AIType.NEUTRAL)
    COPGUY1 = Fighter("Copguy", True, 300, 20, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/copguy.png"), ai = AIType.NEUTRAL)
    GUARD = Fighter("Guard", True, 250, 25, 40, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/guard_soldier.png"), ai = AIType.DEFENSIVE)
    SML_TANK = Fighter("Sherman", True, 500, 60, 120, [Attacks.SHELL], Image("images/characters/sherman.png"), ai = AIType.AGGRO)
    MARINE = Fighter("Marine", True, 300, 30, 45, [Attacks.PUNCH, Attacks.BULLET_SPRAY], Image("images/characters/marine.png"), ai = AIType.SMART)
    BIG_TANK = Fighter("Abrams", True, 700, 70, 150, [Attacks.SHELL], Image("images/characters/abrams.png"), ai = AIType.AGGRO)
    COPGUY2 = Fighter("Copguy", True, 1000, 30, 50, [Attacks.PUNCH, Attacks.BULLET_SPRAY, Attacks.SLASH, Attacks.LIGHT_CAST, Attacks.INSIGHT,
                                                     Attacks.SHOTGUN, Attacks.ENCOURAGE, Attacks.HIGH_NOON, Attacks.SCRATCH, Attacks.ARMOUR,
                                                     Attacks.DAMAGE_SCREM, Attacks.SCREM, Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT,
                                                     Attacks.ROBOPUNCH, Attacks.HOLOSHIELD, Attacks.MUSIC_BOOST, Attacks.RAVE, Attacks.SAMPLE_BLAST,
                                                     Attacks.GNOMED, Attacks.NUDGE, Attacks.DRAW_IN, Attacks.CONFIDENCE, Attacks.PEP_TALK, Attacks.RADS_ATTACK,
                                                     Attacks.AI_MIMIC, Attacks.SHELL], Image("images/characters/copguy.png"), ai = AIType.COPGUY_EX)
encounter = Encounter([], Image("images/bg/black.png"), "audio/legosfx.mp3", 1, "start", "secret")

# This is the displayable that controls what's happening in the boxes at the bottom of the screen

class StatBlockDisplayable(renpy.Displayable):
    def __init__(self, fighter: Fighter):
        self.text_size = 50
        self.fighter = fighter
        self.fighter_name = Text(self.fighter.name, color = "#FFCC00", size = 50)
        self.health_text = Text("HP: " + str(self.fighter.health_points) + "/" + str(self.fighter.max_health), color = "#FFFFFF", size = self.text_size)
        self.AP_text = Text("AP: " + str(self.fighter.armor_points), color = "#FFFFFF", size = self.text_size)
        self.ATK_text = Text("ATK: " + str(self.fighter.attack_points), color = "#FFFFFF", size = self.text_size)
        self.stat_back = Image("minigames/rpg/statbox.png")
        super().__init__(self)

    def render(self, width, height, st, at):
        x_al = 25
        y_al = 65
        spacing = 10
        self.health_text = Text("HP: " + str(self.fighter.health_points) + "/" + str(self.fighter.max_health), color = "#FFFFFF", size = self.text_size)
        self.AP_text = Text("AP: " + str(self.fighter.armor_points), color = "#FFFFFF", size=self.text_size)
        self.ATK_text = Text("ATK: " + str(self.fighter.attack_points), color = "#FFFFFF", size=self.text_size)
        r = renpy.Render(370, 270)
        r.place(self.stat_back)
        r.place(self.fighter_name, x = 25, y = 5)
        r.place(self.health_text, x = x_al, y = y_al)
        r.place(self.AP_text, x = x_al, y = y_al * 2)
        r.place(self.ATK_text, x = x_al, y = y_al * 3)
        renpy.redraw(self, 0)
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
        super().__init__(self)
    
    def render(self, width, height, st, at):
        r = renpy.Render(640, self.size[1])
        r.place(self.fighter.sprite, x = 0, y = 0)
        # Making the health bar
        # THIS IS GARBAGE FULL OF MAGIC NUMBERS
        self.red_part = Solid("#FF0000", xsize = 1920 // 9, ysize = 1920 // 54)
        self.green_part = Solid("#00FF00", xsize = int((1920 // 9) * ((self.fighter.health_points) / (self.fighter.max_health))), ysize = 1920 // 54)
        r.place(self.red_part, x = (self.size[0] // 2)-((1920 // 9) // 2), y = int(25))
        r.place(self.green_part, x = (self.size[0] // 2)-((1920 // 9) // 2), y = int(25))
        renpy.redraw(self, 0)
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

        self.enemy_displayables: list[Displayable] = []
        self.statblock_displayables: list[Displayable] = []

        for e in self.encounter.enemies:
            self.enemy_displayables.append(EnemyDisplayable(e))

        for a in self.encounter.allies:
            self.statblock_displayables.append(StatBlockDisplayable(a))

    def render(self, width, height, st, at):
        if self.start_time is None:
            self.start_time = st
        r = renpy.Render(1920, 1080)

        # These are the enemies
        for i, e in enumerate(self.enemy_displayables):
            if not e.fighter.dead:
                r.place(e, x = (1920 * (i * 0.33)), y = (1080 - e.size[1]) // 2)

        # This adds in the allies
        for i, s in enumerate(self.statblock_displayables):
            if not s.fighter.dead:
                r.place(s, x = (1920 * (i * 0.25) + 55), y = 810)

        return r

    def event(self, ev, x, y, st):
        import pygame  # noqa
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
            self.win = True
        if self.win is not None:
            return self.win

    def visit(self):
        return self.enemy_displayables + self.statblock_displayables # Assets needed to load

rpggame = RPGGameDisplayable(encounter)

# Custom encounter statement

def parse_rpg(lexer):
    lexer.require(":")
    lexer.expect_eol()
    lexer.expect_block("rpg")

    # block
    l = lexer.subblock_lexer()
    l.advance()
    l.keyword("bg")
    bg = l.string()
    l.advance()
    l.keyword("music")
    music = l.string()
    
    # fighters: subblock
    l.advance()
    l.expect_block("fighters")

    fighters = []
    ll = l.subblock_lexer()
    while ll.advance():
        fighters.append(ll.rest())
        ll.expect_eol()

    l.advance()
    l.keyword("scale")
    scale = l.float()

    # goto
    l.advance()
    l.keyword("on_win")
    label = l.string()
    l.advance()
    l.keyword("on_lose")
    label2 = l.string()

    fighters = [f.upper() for f in fighters]

    return (bg, music, fighters, scale, label, label2)

def execute_rpg(parsed_object):
    b, m, f, s, l, ll = parsed_object
    print(parsed_object)
    global rpggame
    rpggame.encounter = Encounter(
        [getattr(Fighters, fighter) for fighter in f],
        Image(b),
        m,
        float(s),
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
