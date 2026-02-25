"""
RPG content for CSB2023 RPG Engine (not actual fights/scenes only AI, Effects, Attacks, Characters)
"""
from __future__ import annotations
import random
import renpy

from renpy.display.image import Image

from rpg_01_engine_ren import Encounter, Fighter, Character, CharacterStat, apply_def, update_def, \
    resolved_def, attack_def, AttackType, stat_attack_def, AI, \
    Attack, ComboAttack, TargetType, FighterAttack, classproperty

"""renpy
rpy python annotations
python early in RPG:
"""

# |---- RPG Content ----|

# -- Effect Functions --
@apply_def
def apply_status_effect(encounter: Encounter, source: Fighter, target: Fighter, stat: CharacterStat, amount: float, scale: bool = False):
    """
    Temporarily change the stats of a fighter.

    Options:
        stat (CharacterStat): The chacter stat to change out of Defence, Attack, Accuracy
        amount (float): The amount to change the stat by (negative or positive)
        scale (bool, optional): Whether the amount is a scale factor or a flat amount. Defaults to False.
    """
    if stat == CharacterStat.HIT_POINTS:
        encounter.send_debug("Cannot change HIT POINTS as a status effect", "apply_status_effect", fighter = source, target = target, stat = stat, amount = amount, scale = scale)
        return

    if scale:
        encounter.scale_fighter(target, stat, amount, permanent=False)
    else:
        encounter.modify_fighter(target, stat, amount, permanent=False)

@update_def
def update_damage_over_time(encounter: Encounter, source: Fighter, target: Fighter, mult: float = 1.0, ignore_armour: bool = False, flat: bool = False):
    """
    Deal a set amount of damage every turn for a few turns

    Options:
        damage (float): Amount of damage to do each turn
        ignore_armour (bool, optional): whether the DOT should ignore the armour of the fighter. Defaults to False.
    """
    encounter.damage_fighter(target, mult if flat else source.attack * mult, roll_crit=False, ignore_armour=ignore_armour)

@resolved_def
def resolved_chance(encounter: Encounter, source: Fighter, target: Fighter, chance: float = 0.5) -> bool:
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
def damage_over_time(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], mult: float = 1.0, duration: int = 1):
    """
    Apply damage over time to fighters

    Args:
        mult (float, optional): The multiplier on top of attacker's ATK. Defaults to 1.0.
        duration (int, optional): The number of turns to apply damage. Defaults to 1.
    """
    for target in targets:
        encounter.apply_effect(Effects.BLEED, fighter, target, duration, update_mult=mult)

@attack_def(AttackType.DAMAGE)
def damage_fighters_range(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], min_mult: float = 0.0, max_mult: float = 1.0):
    """
    Damage fighters by a randomly scaled amount

    Args:
        mult_min (float, optional): minimum damage multiplier. Defaults to 0.0.
        mult_max (float, optional): maximum damage multiplier. Defaults to 1.0.
    """
    for target in targets:
        mult = random.uniform(min_mult, max_mult)
        encounter.damage_fighter(target, fighter.attack * mult)

@attack_def(AttackType.DAMAGE | AttackType.EFFECT | AttackType.SACRIFICE)
def damage_sacrifice(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], harm_mult: float = 1.0, bleed_mult: float = 1.0, duration: int = 1):
    encounter.damage_fighter(fighter, fighter.attack * harm_mult)
    for target in targets:
        encounter.apply_effect(Effects.BLEED, fighter, target, duration, update_mult=bleed_mult)


@attack_def(AttackType.BUFF)
def defend_targets(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
    """
    Increase the targets defence for a single turn
    """
    for target in targets:
        if target.dead:
            continue
        encounter.apply_effect(Effects.DEFEND, fighter, target)

@attack_def(AttackType.DEBUFF | AttackType.EFFECT)
def confuse_targets(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
    """
    Apply the Confusion effect to target fighters
    """
    for target in targets:
        if target.dead:
            continue
        encounter.apply_effect(Effects.CONFUSION, fighter, target)

@attack_def(AttackType.EFFECT)
def blind_fighters(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...], duration: int = 1):
    for target in targets:
        if target.dead:
            continue
        encounter.apply_effect(Effects.BLIND, fighter, target, duration)

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
    attack_type = random.randint(1, 4)
    match attack_type:
        case 1: # ap up, allies
            encounter.send_message("[Draw In] DEF Up", None)
            allies = True
            stat = CharacterStat.DEFENSE
        case 2: # ap down, enemies
            encounter.send_message("[Draw In] DEF Down", None)
            allies = False
            stat = CharacterStat.DEFENSE
            mult = 1.0 / mult
        case 3: # atk up, allies
            encounter.send_message("[Draw In] ATK Up", None)
            allies = True
            stat = CharacterStat.ATTACK
        case 4: # atk down, enemies
            encounter.send_message("[Draw In] ATK Down", None)
            allies = False
            stat = CharacterStat.ATTACK
            mult = 1.0 / mult
        case _: # impossible case
            encounter.send_message("[Draw In] Impossible Result", None)
            return

    for target in targets:
        if (allies and fighter.enemy == target.enemy) or (not allies and fighter.enemy != target.enemy):
            encounter.scale_fighter(target, stat, mult, permanent=True)

@attack_def(AttackType.DAMAGE | AttackType.HEAL | AttackType.BUFF | AttackType.DEBUFF | AttackType.EFFECT) # What could it beee??
def ai_mimic(encounter: Encounter, fighter: Fighter, targets: tuple[Fighter, ...]):
    if targets[0].name == "Copguy EX":
        aa = [a for a in Attacks.ex_attacks if a.type & AttackType.AOE or a.type & AttackType.DAMAGE]
        attack = random.choice(aa)
    else:
        attack = targets[0].character.attacks[0]
    if attack.name == "AI Mimic":
        attack = Attacks.PUNCH
    encounter.send_message(f"[AI Mimic] running {attack.name}...", None)
    attack.func(encounter, fighter, targets)

class AIType:
    NEUTRAL = AI("Neutral")
    AGGRO = AI("Aggro", aggression = 3, tacticity = 0.5, crowd_control = 0.1, heal_threshold = 0.25, heal_chance = 0.25)
    DEFENSIVE = AI("Defensive", heal_threshold = 0.75, tacticity = 3, heal_chance = 0.60)
    SMART = AI("Smart", tacticity = 2, crowd_control = 2, heal_chance = 0.60)
    COPGUY_EX = AI("EX", aggression = 3, tacticity = 2, preferred_targets = ["CS"], heal_chance = 0.70)
    SKITTISH = AI("Skittish", aggression = 1, tacticity = 0.75, crowd_control = 0.5, heal_threshold = 0.85, heal_chance = 0.5)

    @classmethod
    def get(cls, ai: str, default: AI | None = None) -> AI | None:
        cls.__dict__.get(ai, default)


class Effects:
    # Intent: Take damage over x turns.
    BLEED = Effect(
        name="Bleed",
        description="Bleed them dry!",
        positive=False,
        icon="/gui/rpg/status/bleed.png",
        duration=0,
        apply="{target} started bleeding!",
        update=update_damage_over_time("{target} is taking bleed damage!"),
        resolved="{target}'s bleeding has stopped!"
    )
    # Intent: Make fighter very inaccurate
    BLIND = Effect(
        name="Blindness",
        description="Blinded by the lights!",
        positive=False,
        icon="/gui/rpg/status/blindness.png",
        duration=0,
        apply=apply_status_effect(stat=CharacterStat.ACCURACY, amount=0.25, scale=True),
        update="{target} can't see!",
        resolved="{target} can see again!"
    )
    # Intent: We should update this... make fighter both less accurate AND likely to hit the wrong target, including themself!
    CONFUSION = Effect(
        name="Confusion",
        description="Confuse and befuddle!",
        positive=False,
        icon="/gui/rpg/status/confusion.png",
        duration=0,
        apply=apply_status_effect(stat=CharacterStat.ACCURACY, amount=0.5, scale=True),
        update="{target} is confused!",
        resolved=resolved_chance("{target} is no longer confused!", chance=0.5)
    )
    # Intent: Make fighter less vulnerable to damage, but unable to attack this turn.
    DEFEND = Effect(
        name="Defending",
        description="Not today!",
        positive=True,
        icon="/gui/rpg/status/defending.png",
        duration=1,
        apply=apply_status_effect(stat=CharacterStat.DEFENSE, amount=1.5, scale=True),
        update="{target} is defending!"
    )
    # Intent: Make fighter extra vulnerable while asleep and skip their next turn.
    SLEEP = Effect(
        name="Sleep",
        description="Wake up!",
        positive=False,
        icon="/gui/rpg/status/sleep.png",
        duration=1,
        apply=apply_status_effect(stat=CharacterStat.DEFENSE, amount=0.5, scale=True),
        update="{target} fell asleep!",
        resolved="{target} woke up!"
    )
    # Intent: Make fighter unable to do anything at all for x turns.
    STUN = Effect(
        name="Stun",
        description="Get it together!",
        positive=False,
        icon="/gui/rpg/status/stun.png",
        duration=0,
        apply=apply_status_effect(stat=CharacterStat.DEFENSE, amount=1.0, scale=True),
        update="{target} can't move!",
        resolved="{target} has recovered!"
    )


class Attacks:


    ### Effects / Defense

    DEFEND = Attack("Defend", "Dragon doesn't know how to write these", defend_targets(), targets=TargetType.SELF, accuracy=100)
    BLEED = Attack("Bleed", "Bleed them dry!", damage_over_time(mult = 0.25)) # , ex = False
    BLIND = Attack("Blindness", "Blinded by the lights!", apply_status_effect(stat=CharacterStat.ACCURACY, amount=0.25, scale=True) ) # , ex = False

    ### Combo components
    RAW_CHOP = Attack("Raw Chop", "Hiya!", damage_fighters()) # , ex = False
    CS_AP_DOWN = Attack("CS DEF Down", "Bring DEF of an enemy down.", change_stat(stat = CharacterStat.DEFENSE, mult = 0.75)) # , ex = False
    RAW_KICK = Attack("Raw Kick", "It's fuckin raw!", damage_fighters(mult = 2)) # , ex = False
    RAW_SLASH = Attack("Raw Slash", "It's fuckin raw!", damage_fighters()) # , ex = False
    RAINBOW = Attack("Rainbow", "", confuse_targets(), cooldown = 3) # , ex = False
    VOMIT = Attack("Vomit", "", damage_over_time(duration = 3), cooldown = 3) # , ex = False
    RAINBOW_NOCOOL = Attack("Rainbow", "", confuse_targets()) # , ex = False
    VOMIT_NOCOOL = Attack("Vomit", "", damage_over_time(duration = 3)) # , ex = False
    RAVE_DEF = Attack("Rave DEF", "Lowers the enemies defense.", change_stat(stat = CharacterStat.DEFENSE, mult = 0.5), target_count = 0, cooldown = 3) # , ex = False
    RAVE_OFF = Attack("Rave OFF", "Rupture eardrums.", damage_fighters(mult = 0.5), target_count = 0, cooldown = 3) # , ex = False
    SAMPLE_SPAM = Attack("Sample Spam", "", damage_fighters_range(min_mult = 1, max_mult = 3)) # , ex = False
    SOUND_BLAST = Attack("Sound Blast", "", damage_fighters(), target_count = 0) # , ex = False
    TATE_RECALL = Attack("Tate's Recall", "Remember something dreadful.", damage_fighters(mult = 0.75), targets = TargetType.SELF, cooldown = 9, accuracy = 90) # , ex = False
    TATE_REVERB = Attack("Tate's Reverb", "Make them all remember.", damage_over_time(mult = 0.75, duration = 5), target_count = 0, cooldown = 9, accuracy = 90) # , ex = False
    TATE_ECHOES = Attack("Tate's Echoes", "The past haunts you.", change_stat(stat = CharacterStat.ATTACK, mult = 0.5), targets = TargetType.SELF, cooldown = 11, accuracy = 100) # , ex = False
    TATE_BLAST = Attack("Tate's Blaster", "Make it haunt them, too.", damage_fighters(mult = 4), target_count = 0, cooldown = 11, accuracy = 100) # , ex = False
    LIGHT_CAST_DMG = Attack("Light Cast DMG", "A strong blast of light that varies in damage.", damage_fighters_range(min_mult = 1, max_mult = 3), cooldown = 3)
    LIGHT_CAST_EFF = Attack("Light Cast EFF", "A strong blast of light that varies in damage.", blind_fighters, cooldown = 3)

    ### Usable attacks
    PUNCH = Attack("Punch", "A simple punch.", damage_fighters())
    CHOP = ComboAttack("Chop", "Hit an enemy and bring their DEF down.", [RAW_CHOP, CS_AP_DOWN])
    YTP_MAGIC = Attack("YTP Magic", "Channel the power of YTP!", damage_fighters(mult = 20), cooldown = 10, accuracy = 100, start_used = True)
    YTP_MAGIC_NOCOOL = Attack("YTP Magic", "Let no one stand in your way.", damage_fighters(mult = 20), accuracy = 100) # , ex = False
    YTP_HEAL = Attack("Attack.HEAL", "No matter the cost.", heal_fighters(mult = 3), target_count = 0, targets = TargetType.ALLY, cooldown = 1, accuracy = 100)
    FUN_VALUE = Attack("Fun Value", "A Dev's favorite attack.", damage_fighters(mult = 10), accuracy = 100,)
    KICK = ComboAttack("Kick", "A stronger attack, and lowers DEF.", [RAW_KICK, CS_AP_DOWN])
    BULLET_SPRAY = Attack("Bullet Spray", "Shred all enemies with your LMG!", damage_fighters(mult = 1.5), target_count = 0, cooldown = 3, accuracy = 70)
    SLASH = ComboAttack("Slash", "A cutting attack that bleeds out your enemies.", [RAW_SLASH, BLEED], accuracy = 85)
    LIGHT_CAST = ComboAttack("Light Cast", "A strong blast of light that varies in damage.", [LIGHT_CAST_DMG, LIGHT_CAST_EFF])
    INSIGHT = Attack("Insight", "Lowers enemy's attack by a little.", change_stat(stat = CharacterStat.ATTACK, mult = 0.75), accuracy = 90)
    SHOTGUN = Attack("Shotgun", "Blast your enemies twice with a powerful shotgun blast!", damage_fighters(mult = 2), target_count = 2, cooldown = 3, accuracy = 70)
    ENCOURAGE = Attack("Encourage", "Heal one member with morale!", heal_fighters(), targets = TargetType.ALLY, accuracy = 95)
    HIGH_NOON = Attack("High Noon", "Quickly blast 3 targets, or 3 shots on 1!", damage_fighters(mult = 0.75), target_count = 3, cooldown = 3, accuracy = 60)
    SCRATCH = Attack("Scratch", "A basic scratch attack.", damage_fighters(), accuracy = 75)
    ARMOUR = Attack("Armour", "Boost one's defense!", change_stat(stat = CharacterStat.DEFENSE, mult = 2.5), target_count = 1, targets = TargetType.ALLY, cooldown = 3, accuracy = 90)
    DAMAGE_SCREM = Attack("Damage Screm", "Yell as loud as possible to deafen your enemies!", damage_fighters(mult = 0.5), target_count = 0, accuracy = 75)
    SNACK_TIME = Attack("Snack Time", "Heal your team with the power of snacks!", heal_fighters(), target_count = 0, targets = TargetType.ALLY, cooldown = 3, accuracy = 95)
    ELDRITCH_BLAST = Attack("Eldritch Blast", "An unholy blast that does quite a bit of damage to an enemy.", damage_fighters(mult = 1.5))
    RAINBOW_VOMIT = ComboAttack("Rainbow Vomit", "Confuse and damage your enemies with colorful nonsense!", [RAINBOW, VOMIT], accuracy = 75)
    ROBOPUNCH = Attack("RoboPunch", "A strong punch.", damage_fighters(mult = 1.75))
    HOLOSHIELD = Attack("HoloShield", "Boosts your team's defense by a bit.", change_stat(stat = CharacterStat.DEFENSE, mult = 1.75), target_count = 0, targets = TargetType.ALLY, cooldown = 3, accuracy = 90)
    MUSIC_BOOST = Attack("Music Boost", "Boost one's defense by a bit.", change_stat(stat = CharacterStat.DEFENSE, mult = 1.5), target_count = 1, targets = TargetType.SELF)
    RAVE = ComboAttack("Rave", "Blast your enemies' eardrums! (Damages enemies while lowering their defense.)", [RAVE_DEF, RAVE_OFF], accuracy = 75)
    SAMPLE_BLAST = ComboAttack("Sample Blast", "Blast your enemies with music! Varies in damage.", [SAMPLE_SPAM, SOUND_BLAST])
    GNOMED = Attack("Gnomed", "Confuse everyone by gnoming them!", confuse_targets(), target_count = 0, cooldown = 3, accuracy = 70)
    NUDGE = Attack("Nudge", "Does either very little or massive damage.", damage_fighters_range(min_mult = 0.1, max_mult = 10), accuracy = 85)
    DRAW_IN = Attack("Draw in", "Either lowers the enemies stats, or increases your friend's stats!", draw_in(mult = 2), TargetType.ALL, target_count=0, accuracy = 85)
    CONFIDENCE = Attack("Confidence", "Raise your team's attack!", change_stat(stat = CharacterStat.ATTACK, mult = 1.25), target_count = 0, targets = TargetType.ALLY, accuracy = 90)
    PEP_TALK = Attack("Pep Talk", "Raise your team's defense!", change_stat(stat = CharacterStat.DEFENSE, mult = 1.25), target_count = 0, targets = TargetType.ALLY, accuracy = 90)
    RADS_ATTACK = Attack("RADS Attack", "Inflict radiation on your enemies to kill them over time!", damage_over_time(mult = 0.5), accuracy = 60)
    AI_MIMIC = Attack("AI Mimic", "Copies an enemy's attack.", ai_mimic(), cooldown = 2)
    SHELL = Attack("Shell", "Fire a tank shell!", damage_fighters_range(min_mult = 1, max_mult = 2), accuracy = 60)
    HEAL_EX = Attack("Heal EX", "Lots of healing.", heal_fighters(mult = 10), target_count = 0, targets = TargetType.ALLY, accuracy = 100)
    AUGMENT = Attack("Awesome Augment", "Fire a laser! Fire a laser!", damage_fighters(mult = 15), target_count = 0, cooldown = 5, accuracy = 100) # , ex = False
    REVERB_RECALL = Attack("Reverb Recall", "Channel your pain over 5 turns. Also damages the user.", damage_sacrifice(harm_mult = 0.75, bleed_mult = 0.75, duration = 5), cooldown = 9, accuracy = 90) # , ex = False
    # TODO: we really need the ability to select different things for each part of the combo
    ECHO_BLAST = ComboAttack("Echo Blast", "Make them feel the pain of the past, at the cost of your ATK.", [TATE_BLAST, TATE_ECHOES], cooldown = 11, accuracy = 100) # , ex = False
    GENERGY = Attack("Genergy", "Sip some refreshing Genergy.", heal_fighters(mult = 2.36), targets = TargetType.ALLY, accuracy = 100) # , ex = False

    # UCN
    STOMP = Attack("Stomp", "Send an earthquake to the enemies!", damage_fighters(mult = 0.75), target_count = 0) # , ex = False
    POKE = Attack("Poke", "A mega poke.", damage_fighters(mult = 2.5), accuracy = 90) # , ex = False
    SWORD = Attack("Sword", "The edge of a sharp thing.", damage_fighters()) # , ex = False
    SWORD_AP = Attack("Sword (DEF Down)", "The edge of a sharp thing, more.", change_stat(stat = CharacterStat.DEFENSE, mult = 0.75)) # , ex = False
    SWORD_SLASH = ComboAttack("Sword Slash", "Hit an enemy, and take a chip out of their armor.", [SWORD, SWORD_AP]) # , ex = False
    FLAMETHROWER = Attack("Flamethrower", "Spray all your enemies with burning fuel!", damage_over_time(mult = 0.5, duration = 3), target_count = 0, cooldown = 3, accuracy = 70) # , ex = False,
    CHOCOLATE_CAKE = Attack("Chocolate Cake", "Heal a party member with loads to eat!", heal_fighters(), targets = TargetType.ALLY, accuracy = 95) # , ex = False
    CONFUSING_STORY = Attack("Confusing Story", "Tell a puzzling poem.", confuse_targets()) # , ex = False
    HYPE_UP = Attack("Hype Up", "Get a team member pumped to fight!", change_stat(stat = CharacterStat.ATTACK, mult=1.5), targets = TargetType.ALLY, accuracy = 90) # , ex = False
    PITCHMAN = Attack("Pitchman", "Smooth-talk an enemy's defenses down!", change_stat(stat = CharacterStat.DEFENSE, mult = 0.75), accuracy = 90) # , ex = False
    HUG = Attack("Hug", "Hug an enemy (ouch).", damage_fighters(mult = 1.5), accuracy = 90) # , ex = False
    SPIKE_BOMB = Attack("Spike Bomb", "Release spikes to all enemies!", damage_fighters(mult = 1.5), target_count = 0, cooldown = 3, accuracy = 75) # , ex = False
    SHOT = Attack("Shot", "I'd like to see you outrun bullet.", damage_fighters(mult = 1.5)) # , ex = False
    SHOT_AP = Attack("Shot (DEF Down)", "Kevlar destroyed.", change_stat(stat = CharacterStat.DEFENSE, mult = 0.75)) # , ex = False
    PISTOL = ComboAttack("Pistol", "A sharp shot to the chest.", [SHOT, SHOT_AP]) # , ex = False
    ALL_OVER_AGAIN = Attack("All Over Again", "Ditto.", ai_mimic()) # , ex = False
    HEAVY_PUNCH = Attack("Heavy Punch", "A quick blow.", damage_fighters(mult = 1.75), accuracy = 75) # , ex = False
    SOTH = Attack("Shit On The House", "I'm going to... take a shit on the house.", damage_fighters(mult = 2), target_count = 0, cooldown = 3, accuracy = 65) # , ex = False
    ONE_HUNDRED = Attack("100% Unsatisfied", "Yelp reviews coming in...", change_stat(stat = CharacterStat.ATTACK, mult = 0.8), target_count = 0, accuracy = 95) # , ex = False
    ICE_CREAM = Attack("Ice Cream", "Bing chilling!", heal_fighters(mult = 1.5), target_count = 0, targets = TargetType.ALLY, accuracy = 90, cooldown = 3) # , ex = False
    RAINBOW_VOMIT_NOCOOL = ComboAttack("Rainbow Vomit", "Why are you like this?", [RAINBOW_NOCOOL, VOMIT_NOCOOL], accuracy = 75) # , ex = False
    KARATE_CHOP = ComboAttack("Karate Chop", "Hit an enemy and bring their DEF down.", [RAW_CHOP, SWORD_AP]) # , ex = False
    DRONE_STRIKE = Attack("Drone Strike", "O Bomb a.", damage_fighters(mult = 2.5), target_count = 0, cooldown = 3, accuracy = 85) # , ex = False
    COIN_BARRAGE = Attack("Coin Barrage", "Pelt your foes with change!", damage_fighters_range(min_mult = 0.75, max_mult = 2), accuracy = 60) # , ex = False
    CART_SMASH = Attack("Cart Smash", "Ram into someone with a shopping cart.", damage_fighters(mult = 5), accuracy = 95, cooldown = 3) # , ex = False
    BITE = Attack("Bite", "Chomp!", damage_fighters_range(min_mult = 5, max_mult = 10), accuracy = 5) # , ex = False
    SHARKNADO = ComboAttack("Sharknado", "A confusing vortex of sharks.", [BITE, BLEED], cooldown = 5, accuracy = 80) # , ex = False
    LOBBYING = ComboAttack("Lobbying", "Lobby like it's your hobby!", [ENCOURAGE, CS_AP_DOWN]) # , ex = False
    NANOMACHINES = Attack("Nanomachines", "Nanomachines, son.", damage_fighters(mult = 1.5), target_count = 8, accuracy = 95, cooldown = 7) # , ex = False

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
    def get(cls, k: str, default: Attack | None = None) -> Attack | None:
        return cls.__dict__.get(k, default)

# Special actions used by the Encounter and the Ai.
# They can't be used until the actions are defined. This is technically
# not needed in renpy since everything is global, but I'm trying to avoid
# stink.
Encounter.DEFEND_ACTION = FighterAttack(Attacks.DEFEND)
Encounter.HEAL_EX = FighterAttack(Attacks.HEAL_EX)

class Characters:
    NONE = None

    # Allies
    CS = Character("CS", 188, 10, 25, [Attacks.PUNCH, Attacks.BULLET_SPRAY], portrait=Image("gui/rpg/portraits/cs.png"), sprite=Image("images/characters/cs/base/angry.png"), ai = AIType.NEUTRAL)
    CS_NG = CS.clone("CS (National Guard)", attack=30, attacks=[Attacks.CHOP, Attacks.BULLET_SPRAY]) # Character("CS (National Guard)", 188, 10, 30, , portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS")
    CS_STRONG = Character("CS (Strong)", 188, 10, 35, [Attacks.KICK, Attacks.BULLET_SPRAY], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    CS_FINAL = Character("CS (Final)", 288, 10, 40, [Attacks.KICK, Attacks.BULLET_SPRAY, Attacks.YTP_MAGIC], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    CS_FINAL2 = Character("CS (Error)", 1880, 10, 250, [Attacks.KICK, Attacks.YTP_HEAL, Attacks.YTP_MAGIC_NOCOOL], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    CS_WEAK = Character("CS (Weak)", 188, 5, 25, [Attacks.PUNCH], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    CS_ARCHIVAL = Character("CS (Archival)", 1027, 50, 27, [Attacks.KICK, Attacks.YTP_HEAL], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    CS_VS_TATE_PUNCH = Character("{image=gui/inline_text/dx_text.png} CS (VS Tate - Punch)", 288, 10, 40, [Attacks.PUNCH, Attacks.GENERGY, Attacks.YTP_MAGIC], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    CS_VS_TATE_KICK = Character("{image=gui/inline_text/dx_text.png} CS (VS Tate - Kick)", 288, 10, 40, [Attacks.KICK, Attacks.GENERGY, Attacks.YTP_MAGIC], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    CS_VS_TATE_CHOP = Character("{image=gui/inline_text/dx_text.png} CS (VS Tate - Chop)", 288, 10, 40, [Attacks.CHOP, Attacks.GENERGY, Attacks.YTP_MAGIC], portrait=Image("gui/rpg/portraits/cs.png"), display_name = "CS", ai = AIType.NEUTRAL, sprite=Image("images/characters/cs/base/angry.png"))
    ARCEUS = Character("Arceus", 160, 15, 35, [Attacks.SLASH, Attacks.LIGHT_CAST], portrait=Image("gui/rpg/portraits/arceus.png"), sprite=Image("images/characters/arc/angry.png"), ai = AIType.SMART)
    PAKOO = Character("Pakoo", 145, 20, 30, [Attacks.INSIGHT, Attacks.SHOTGUN], portrait=Image("gui/rpg/portraits/pakoo.png"), sprite=Image("images/characters/pakoo/pakoo_disappointed.png"), ai = AIType.SMART)
    MIKA = Character("Mika", 165, 20, 30, [Attacks.ENCOURAGE, Attacks.HIGH_NOON], portrait=Image("gui/rpg/portraits/mika.png"), sprite=Image("images/characters/mika.png"), ai = AIType.AGGRO)
    KITTY = Character("Kitty", 155, 15, 20, [Attacks.SCRATCH, Attacks.ARMOUR], portrait=Image("gui/rpg/portraits/kitty.png"), sprite=Image("images/characters/kitty.png"), ai = AIType.SKITTISH)
    TATE = Character("Tate", 170, 5, 30, [Attacks.DAMAGE_SCREM, Attacks.SNACK_TIME], portrait=Image("gui/rpg/portraits/tate.png"), sprite=Image("images/characters/tate/tateserious.png"), ai = AIType.SKITTISH)
    ARIA = Character("Aria", 220, 20, 45, [Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT], portrait=Image("gui/rpg/portraits/aria.png"), sprite=Image("images/characters/aria.png"), ai = AIType.SMART)
    DIGI = Character("Digi", 150, 20, 30, [Attacks.ROBOPUNCH, Attacks.HOLOSHIELD], portrait=Image("gui/rpg/portraits/digi.png"), sprite=Image("images/characters/digi/angry.png"),ai = AIType.AGGRO)
    NOVA = Character("Nova", 170, 5, 30, [Attacks.MUSIC_BOOST, Attacks.RAVE], portrait=Image("gui/rpg/portraits/nova.png"), sprite=Image("images/characters/nova.png"), ai = AIType.AGGRO)
    BLANK = Character("Blank", 180, 5, 35, [Attacks.SAMPLE_BLAST, Attacks.GNOMED], portrait=Image("gui/rpg/portraits/blank.png"), sprite=Image("images/characters/blank.png"), ai = AIType.DEFENSIVE)
    MIDGE = Character("Midge", 165, 10, 25, [Attacks.NUDGE, Attacks.DRAW_IN], portrait=Image("gui/rpg/portraits/midge.png"), sprite=Image("images/characters/midge.png"), ai = AIType.DEFENSIVE)
    DB05 = Character("DB05", 9001, 9001, 50, [Attacks.CONFIDENCE, Attacks.PEP_TALK], portrait=Image("gui/rpg/portraits/db05.png"), sprite=Image("images/characters/db.png"), ai = AIType.SKITTISH)
    ANNO = Character("Anno", 200, 20, 40, [Attacks.RADS_ATTACK, Attacks.AI_MIMIC], portrait=Image("gui/rpg/portraits/anno.png"), sprite=Image("images/characters/anno/anno.png"), ai = AIType.SMART)

    # Allies (UCN)
    BUBBLE = Character("{image=gui/inline_text/dx_text.png} Bubble", 250, 10, 35, [Attacks.STOMP, Attacks.POKE], display_name = "Bubble", portrait=Image("gui/rpg/portraits/bubble.png"), sprite=Image("images/characters/bubble.png"), ai = AIType.AGGRO)
    GES = Character("{image=gui/inline_text/dx_text.png} Ges", 170, 20, 35, [Attacks.SWORD_SLASH, Attacks.FLAMETHROWER], display_name = "Ges", portrait=Image("gui/rpg/portraits/ges.png"), sprite=Image("images/characters/ges.png"), ai = AIType.SMART)
    MICHAEL = Character("Michael", 155, 15, 35, [Attacks.CHOCOLATE_CAKE, Attacks.CONFUSING_STORY], portrait=Image("gui/rpg/portraits/michael.png"), sprite=Image("images/characters/michael.png"), ai = AIType.DEFENSIVE)
    BILLY = Character("Billy", 220, 10, 25, [Attacks.HYPE_UP, Attacks.PITCHMAN, Attacks.AUGMENT], portrait=Image("gui/rpg/portraits/billy.png"), sprite=Image("images/characters/billy/BillyMaysWithLaser.png"), ai = AIType.SMART)
    PHIL = Character("Phil", 160, 20, 40, [Attacks.HYPE_UP, Attacks.PITCHMAN], portrait=Image("gui/rpg/portraits/phil.png"), sprite=Image("images/characters/phil.png"), ai = AIType.AGGRO)
    MEAN = Character("Mean", 150, 20, 35, [Attacks.HUG, Attacks.SPIKE_BOMB], portrait=Image("gui/rpg/portraits/mean.png"), sprite=Image("images/characters/mean/meanangry.png"), ai = AIType.AGGRO)
    POMNI = Character("Pomni", 200, 15, 30, [Attacks.RAINBOW_VOMIT_NOCOOL, Attacks.RAINBOW_VOMIT_NOCOOL], portrait=Image("gui/rpg/portraits/pomni.png"), sprite=Image("images/characters/pomni/pomni_concern.png"), ai = AIType.SKITTISH)
    OBAMA = Character("{image=gui/inline_text/dx_text.png} Obama", 190, 25, 35, [Attacks.KARATE_CHOP, Attacks.DRONE_STRIKE], portrait=Image("gui/rpg/portraits/obama.png"), sprite=Image("images/characters/obama/obama.png"), ai = AIType.SMART)
    CASHIER = Character("{image=gui/inline_text/dx_text.png} Cashier", 188, 14, 33, [Attacks.COIN_BARRAGE, Attacks.CART_SMASH], portrait=Image("gui/rpg/portraits/cashier.png"), sprite=Image("images/characters/cashier.png"), ai = AIType.NEUTRAL)
    SHARK = Character("{image=gui/inline_text/dx_text.png} Shark", 190, 10, 40, [Attacks.BITE, Attacks.SHARKNADO], portrait=Image("gui/rpg/portraits/shark.png"), sprite=Image("images/characters/blahaj_shark.png"), ai = AIType.AGGRO)

    # Enemies
    FANBOYA = Character("Fanboy (NVIDIA)", 50, 0, 16, [Attacks.PUNCH], sprite=Image("images/characters/nvidiafanboy.png"), ai = AIType.NEUTRAL, display_name = "Fanboy", portrait=Image("gui/rpg/portraits/fanboy_nvidia.png"))
    FANBOYB = Character("Fanboy (AMD)", 50, 0, 16, [Attacks.PUNCH], sprite=Image("images/characters/amdfanboy.png"), ai = AIType.NEUTRAL, display_name = "Fanboy", portrait=Image("gui/rpg/portraits/fanboy_amd.png"))
    COP = Character("Cop", 150, 15, 30, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/cop.png"), ai = AIType.NEUTRAL, portrait=Image("gui/rpg/portraits/cop.png"))
    COPGUYGODMODE = Character("Copguy (God)", 9001, 9001, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/copguy/copguy.png"), ai = AIType.NEUTRAL, display_name = "Copguy", portrait=Image("gui/rpg/portraits/copguy.png"))
    COPGUY = Character("Copguy", 300, 20, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/copguy/copguy.png"), ai = AIType.NEUTRAL, portrait=Image("gui/rpg/portraits/copguy.png"))
    GUARD = Character("Guard", 225, 25, 35, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/guard_soldier.png"), ai = AIType.DEFENSIVE, portrait=Image("gui/rpg/portraits/guard.png"))
    SML_TANK = Character("Sherman", 400, 60, 100, [Attacks.SHELL], sprite=Image("images/characters/sherman.png"), ai = AIType.AGGRO, portrait=Image("gui/rpg/portraits/sherman.png"))
    MARINE = Character("Marine", 300, 30, 45, [Attacks.PUNCH, Attacks.BULLET_SPRAY], sprite=Image("images/characters/marine.png"), ai = AIType.SMART, portrait=Image("gui/rpg/portraits/marine.png"))
    BIG_TANK = Character("Abrams",700, 70, 150, [Attacks.SHELL], sprite=Image("images/characters/abrams.png"), ai = AIType.AGGRO, portrait=Image("gui/rpg/portraits/abrams.png"))
    COPGUY_EX = Character("Copguy EX", 2222, 30, 50, Attacks.ex_attacks, sprite=Image("images/characters/copguy/copguy.png"), ai = AIType.COPGUY_EX, portrait=Image("gui/rpg/portraits/copguy_ex.png"), anim_sprite="copguy_ex")
    PAKOOE = Character("Pakoo (Error)", 9999, 70, 150, [Attacks.FUN_VALUE], sprite=Image("images/characters/pakoo/pakoo_disappointed.png"), ai = AIType.AGGRO, display_name = "Pakoo", portrait=Image("gui/rpg/portraits/pakoo.png"))
    COPGUY_EXE = Character("{image=gui/inline_text/dx_text.png} Copguy.EXE", 666, 66, 66, [Attacks.ELDRITCH_BLAST, Attacks.RAINBOW_VOMIT, Attacks.SLASH, Attacks.CONFUSING_STORY], sprite=Image("images/characters/copguy/copguyexe.png"), ai = AIType.AGGRO, display_name = "Copguy.EXE", portrait=Image("gui/rpg/portraits/copguy_exe.png"))
    K174 = Character("K17-4", 174, 17, 20, [Attacks.PUNCH], sprite=Image("images/characters/pakoo/k174.png"), ai = AIType.NEUTRAL, portrait=Image("gui/rpg/portraits/k174.png"))
    K199 = Character("K19-9", 199, 19, 30, [Attacks.KICK], sprite=Image("images/characters/pakoo/k199.png"), ai = AIType.AGGRO, portrait=Image("gui/rpg/portraits/k199.png"))
    K207 = Character("K20-7", 207, 20, 10, [Attacks.PUNCH], sprite=Image("images/characters/pakoo/k207.png"), ai = AIType.DEFENSIVE, portrait=Image("gui/rpg/portraits/k207.png"))
    TATE_EX = Character("{image=gui/inline_text/dx_text.png} Tate EX", 9999, 11, 111, [Attacks.DAMAGE_SCREM, Attacks.REVERB_RECALL, Attacks.ECHO_BLAST], sprite=Image("secret/pt/tate_ex.png"), ai = AIType.AGGRO, display_name = "Tate EX", portrait=Image("gui/rpg/portraits/tate_ex.png"), anim_sprite="tate_ex")

    # Enemies (UCN)
    WESLEY = Character("{image=gui/inline_text/dx_text.png} Wesley", 200, 20, 40, [Attacks.PISTOL, Attacks.ALL_OVER_AGAIN], sprite=Image("images/characters/hohsis/wesley.png"), ai = AIType.AGGRO, display_name = "Wesley", portrait=Image("gui/rpg/portraits/wesley.png"))
    ED = Character("{image=gui/inline_text/dx_text.png} Ed", 300, 30, 25, [Attacks.HEAVY_PUNCH, Attacks.SOTH], sprite=Image("images/characters/hohsis/ed.png"), ai = AIType.SMART, display_name = "Ed", portrait=Image("gui/rpg/portraits/ed.png"))
    RICHARD = Character("{image=gui/inline_text/dx_text.png} Richard", 250, 20, 30, [Attacks.ONE_HUNDRED, Attacks.ICE_CREAM], sprite=Image("images/characters/hohsis/rich.png"), ai = AIType.DEFENSIVE, display_name = "Richard", portrait=Image("gui/rpg/portraits/rich.png"))
    CEO = Character("{image=gui/inline_text/dx_text.png} CEO of Diabetes", 1000, 50, 75, [Attacks.LOBBYING, Attacks.NANOMACHINES], sprite=Image("images/characters/ceo.png"), ai = AIType.SMART, display_name = "CEO", portrait=Image("gui/rpg/portraits/diabetes_ceo.png"))
    SECRETARY = Character("{image=gui/inline_text/dx_text.png} Secretary of Diabetes", 1000, 50, 75, [Attacks.LOBBYING, Attacks.NANOMACHINES], sprite=Image("images/characters/secretary.png"), ai = AIType.SMART, display_name = "Secretary", portrait=Image("gui/rpg/portraits/diabetes_secretary.png"))

    allies = (
        CS, CS_NG, CS_STRONG, CS_FINAL, CS_FINAL2, CS_WEAK, CS_ARCHIVAL, CS_VS_TATE_PUNCH, CS_VS_TATE_KICK, CS_VS_TATE_CHOP,
        ARCEUS, PAKOO , MIKA, KITTY , TATE, ARIA, DIGI, NOVA, BLANK , MIDGE , DB05, ANNO, BUBBLE , GES, MICHAEL, BILLY, PHIL,
        MEAN, POMNI, OBAMA, CASHIER, SHARK,
    )

    @classproperty
    def allies_names_set(self):
        # We use the assigned name because that is what the blocks withing the rpy scripts use.
        return set(ally.assigned_name for ally in self.allies)

    enemies = (
        FANBOYA, FANBOYB, COP, COPGUYGODMODE, COPGUY, GUARD, SML_TANK, MARINE, BIG_TANK, COPGUY_EX, PAKOOE, COPGUY_EXE,
        K174, K199, K207, TATE_EX, WESLEY, ED, RICHARD, CEO, SECRETARY
    )

    @classproperty
    def enemy_name_set(self):
        # We use the assigned name because that is what the blocks withing the rpy scripts use.
        return set(enemy.assigned_name for enemy in self.enemies)

    characters = (
        *allies, *enemies
    )

    @classmethod
    def get(cls, k: str, default: Character | None = None) -> Character | None:
        return cls.__dict__.get(k, default)

    @classmethod
    def random(cls) -> Character:
        return random.choice(cls.characters)

variable_characters: dict[str, Character] = {}

def set_var_character(char: str, assigned_name: str):
    character = Characters.get(assigned_name)
    if char is None or char == "NONE" or character is None:
        return
    variable_characters[char] = character
