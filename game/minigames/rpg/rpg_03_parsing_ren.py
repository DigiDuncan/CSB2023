from __future__ import annotations
import renpy

from rpg_01_engine_ren import Fighter, Encounter
from rpg_02_content_ren import variable_characters, AIType, Characters

ucn_bg: str
ucn_music: str
ucn_scale: float

# This is the equivalent of a python early block in a .rpy file.
"""renpy
rpy python annotations
python early in RPG:
"""

"""
CSB2023 RPG parsing
"""

ucn_bg = "images/bg/fnaf_office.png"
ucn_music = "rude_buster.ogg"
ucn_scale = 1.0


type ParsedFighter = tuple[str, bool, str | None, int | None, int | None, int | None, int | None]
# Parse a fighter by getting their name, and optional overrides for their ai, hp, def, atk, and acc
def parse_fighter(lexer) -> ParsedFighter:
    # ! Variable here is scuffed it returns "$" if it matches and `None` if it doesn't.
    # It is technically truthy, but I don't like it ~Dragon
    variable = lexer.match(r"\$") # Variable Fighter $<x>
    name = lexer.word()

    # Their name might be a variable. That has to be resolved at execute time.
    # As the rpg block is parsed at run time.

    if not variable:
        name = name.upper()
    ai = hp = defense = attack = accuracy = None
    while not lexer.eol():
        if lexer.keyword("ai"):
            ai = lexer.word().upper()
        elif lexer.keyword("hp"):
            hp = int(lexer.integer())
        elif lexer.keyword("def"):
            defense = int(lexer.integer())
        elif lexer.keyword("atk"):
            attack = int(lexer.integer())
        elif lexer.keyword("acc"):
            accuracy = int(lexer.integer())

    lexer.expect_eol()
    return (name, variable, ai, hp, defense, attack, accuracy)

type ParsedRpg = tuple[float, int, str, str, str | None, str | None, str | None, bool, list[ParsedFighter] | None, list[ParsedFighter], list[ParsedFighter]]
# Parse an rpg block and get the level/scale, background, music, on_win, on_lose, intro_text, if it is a ucn fight, fighters, ally fighters, and enemy fighters
def parse_rpg(lexer) -> ParsedRpg:
    # print("Started parsing")
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
            if level is None:
                is_ucn = True
                level = None
            else:
                level = float(level)
        if block.keyword("turn") or block.keyword("initial"):
            initial = int(block.integer())
        elif block.keyword("bg"):
            background = block.string()
            if background == "ucn":
                is_ucn = True
                background = None
        elif block.keyword("music"):
            music = block.string()
            if music == "ucn":
                is_ucn = True
                music = None
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
            block.expect_block("expecting fighters block")
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
    # print(level, initial, background, music, on_win, on_lose, intro, is_ucn, fighters, allies, enemies)
    return level, initial, background, music, on_win, on_lose, intro, is_ucn, fighters, allies, enemies

def create_fighter(name, variable, ai, hp, defense, attack, accuracy, level: float = 1.0, is_enemy: bool | None = None):
    if variable:
        if name not in variable_characters:
            return None
        character = variable_characters[name]
        name = character.assigned_name
    else:
        character = Characters.get(name)
        if character is None:
            return None

    # If `is_enemy` is None then we are using the legacy system and have to check the enemy name set
    enemy = name in Characters.enemy_name_set if is_enemy is None else is_enemy
    level = 1.0 if enemy else level
    ai = AIType.get(ai)

    return Fighter(character, enemy, level, ai, hp, defense, attack, accuracy)

def execute_rpg(parsed_object: ParsedRpg):
    level, initial, background, music, on_win, on_lose, intro_text, is_ucn, fighters, allies, enemies = parsed_object

    if is_ucn:
        global ucn_bg, ucn_music, ucn_scale
        background = ucn_bg
        music = ucn_music
        level = ucn_scale # TODO rename to level

    if fighters is not None:
        fighters = [
            create_fighter(name, variable, ai, hp, defense, attack, accuracy, level, None)
            for (name, variable, ai, hp, defense, attack, accuracy) in fighters
        ]
    else:
        fighters = [
            *(
                create_fighter(name, variable, ai, hp, defense, attack, accuracy, level, False)
                for (name, variable, ai, hp, defense, attack, accuracy) in allies
            ),
            *(
                create_fighter(name, variable, ai, hp, defense, attack, accuracy, level, True)
                for (name, variable, ai, hp, defense, attack, accuracy) in enemies
            )
        ]

    # Clear out any None fighters. Generally only happens when the user selects none in UCN
    fighters = [fighter for fighter in fighters if fighter is not None]

    global encounter
    encounter = Encounter(fighters, background, music, on_win, on_lose, intro_text, initial)
    renpy.jump("play_rpggame")

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

renpy.register_statement(
    name = "rpg",
    parse = parse_rpg,
    lint = lint_rpg,
    execute = execute_rpg,
    block = True
)

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
    scale 1
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
