init -3 python:
    import logging
    from digiformatter import logger as digilogger

    dfhandler = digilogger.DigiFormatterHandler()
    logging.basicConfig(level=logging.NOTSET)

    logger = logging.getLogger("csb")
    logger.setLevel(logging.DEBUG) # Change this to logging.INFO or higher for production
    logger.handlers = []
    logger.propagate = False
    logger.addHandler(dfhandler)

init -1 python:
    from pathlib import Path

    # This is a weird place to define these, but I have to I think.
    FUN_VALUE_UNOBTRUSIVE = 5
    FUN_VALUE_COMMON = 10
    FUN_VALUE_RARE = 25
    FUN_VALUE_MUSIC = 32
    FUN_VALUE_EPIC = 50
    FUN_VALUE_LEGENDARY = 90

    FUN_VALUE_FISH_CHANCE = 0.05

    import json

    # Achievement step counts
    pun_count = 999
    fun_count = 999
    original_ending_count = 27

    ##### ONLY OPEN JSON FILES ONCE #####

    # Bios
    with renpy.open_file("data/bios.json") as f:
        j = json.load(f)
        bio_count = len(j)
        logger.info(f"Loaded {bio_count} bios.")

    # Items
    with renpy.open_file("data/item_collection.json") as f:
        j = json.load(f)
        item_count = len(j)
        logger.info(f"Loaded {item_count} items.")

    ITEM_MAP = j

    # Gallery
    with renpy.open_file("data/gallery.json") as f:
        j = json.load(f)
        gallery_count = len(j)
        logger.info(f"Loaded {gallery_count} gallery items.")

    GALLERY_MAP = j

    # Jukebox
    with renpy.open_file("data/jukebox.json") as f:
        j = json.load(f)
        song_count = len(j["tracks"])
        logger.info(f"Loaded {song_count} songs.")

    MUSIC_MAP = j["tracks"]
    TAGS_MAP = j["tags"]

    # Timeline
    with renpy.open_file("data/timeline.json") as f:
        j = json.load(f)
        timeline_trace_count = 0
        for e in j:
            if j[e]["type"] != "arrow":
                timeline_trace_count = timeline_trace_count + 1
        logger.info(f"Loaded {timeline_trace_count} events.")

    TIMELINE_MAP = j

    # UCN Blacklist
    with renpy.open_file("data/ucn_bg_blacklist.json") as f:
        j = json.load(f)
        logger.info(f"Loaded UCN image blacklist.")

    UCN_BLACKLIST_MAP = j

    # Bookshelf
    with renpy.open_file("data/books.json") as f:
        j = json.load(f)
        logger.info(f"Loaded books.")

    BOOKS_MAP = j

    # Credits
    with renpy.open_file("data/credits.json") as f:
        j = json.load(f)
        logger.info(f"Loaded credits.")

    CREDITS_MAP = j

    # Themes
    theme_j = {}
    theme_folder = Path(renpy.loader.get_path("gui/themes"))
    theme_dirs = os.listdir(theme_folder)
    for d in theme_dirs:
        p = theme_folder / d
        if (p).is_dir():
            with renpy.open_file(str((p / "config.json").absolute()).replace("\\", "/")) as f:
                j = json.load(f)
                theme_j[d] = {
                    "display_name": j["display_name"],
                    "unlock_value": j["unlock_value"],
                    "perf_warning": j["perf_warning"],
                    "sort_order": j["sort_order"]
                }

                logger.info(f"Scanned theme '{d}'.")

    THEME_MAP = theme_j
    theme_count = len(THEME_MAP)
    #print(THEME_MAP)

init python:
    # Add more screen layers
    renpy.add_layer("popup", above = "overlay")
    renpy.add_layer("music", above = "master")
    renpy.add_layer("flashlight", below = "music")
    renpy.add_layer("fun_icon", above = "flashlight")

    # Load and create font groups.
    # The character sets must be loaded in order of priority.
    # Silly triangle first, then JP text, then CN text, then EN fallback
    # This version now has scaling, so the JP text won't be MASSIVE in comparison to the EN text

    # Register other fonts
    config.font_name_map["azsz"] = "AllerDisplay_Std_Rg_0.ttf"
    config.font_name_map["dyslexia"] = "comic.ttf" # Dyslexia mode

    # Theme handling
    config.font_name_map["default"] = gui_theme_map["main_font"]
    config.font_name_map["cn"] = gui_theme_map["cn_font"]
    config.font_name_map["jp"] = gui_theme_map["jp_font"]
    config.font_name_map["ru"] = gui_theme_map["ru_font"]

    # Force multilingual text for music popup, jukebox, credits 
    DYSLEXIA_GROUP = FontGroup().add("FiraCode-Retina.ttf", 0x2206, 0x2206).add("MochiyPopOne-Regular.ttf", 0x2600, 0x9fff).add("comic.ttf", 0x0000, 0xffff)

    config.font_name_map["music_text"] = FontGroup().add("FiraCode-Retina.ttf", 0x2206, 0x2206).add( gui_theme_map["jp_font"] , 0x2600, 0x9fff).add( gui_theme_map["main_font"] , 0x0000, 0xffff)
    config.font_name_map["credits_music"] = FontGroup().add("FiraCode-Retina.ttf", 0x2206, 0x2206).add("CP_Font_1.otf", 0x2600, 0x9fff).add("impact.ttf", 0x0000, 0xffff)

    # Scale all fonts here (overall size first, then line spacing if needed)
    
    config.ftfont_scale["FiraCode-Retina.ttf"] = 0.825 # Triangle
    config.ftfont_scale["ZCOOLKuaiLe-Regular.ttf"] = 0.75 # CP - CSB/CE Themes
    config.ftfont_scale["MochiyPopOne-Regular.ttf"] = 0.75 # JP - CSB/CE Themes
    config.ftfont_scale["BalsamiqSans-Bold.ttf"] = 0.825 # RU - CSB/CE Themes
    config.ftfont_scale["CP_Font_1.otf"] = 0.825 # JP - Credits
    config.ftfont_scale["YuGothL.ttc"] = 0.8 # JP - Tate EX Theme   
    config.ftfont_scale["Source Han Sans CN Light.otf"] = 0.8 # CN - Tate EX Theme
    config.ftfont_scale["Raleway-VariableFont_wght.ttf"] = 0.8 # RU - Tate EX Theme
    config.ftfont_scale["Aller_Std_Lt_0.ttf"] = 0.8 # Tate EX Theme Main
    config.ftfont_scale["AllerDisplay_Std_Rg_0.ttf"] = 1.0 # Tate EX Theme Accent
    config.ftfont_scale["comic.ttf"] = 0.75 # Dyslexia - CSB/CE Themes
    config.ftfont_scale["CenturyGothicPaneuropeanSemiBold.ttf"] = 0.8 # Dyslexia - Tate EX Theme

    config.ftfont_vertical_extent_scale["FiraCode-Retina.ttf"] = 1.0 # Triangle
    config.ftfont_vertical_extent_scale["ZCOOLKuaiLe-Regular.ttf"] = 1.0 # CN - CSB/CE Themes
    config.ftfont_vertical_extent_scale["MochiyPopOne-Regular.ttf"] = 1.0 # JP - CSB/CE Themes
    config.ftfont_vertical_extent_scale["BalsamiqSans-Bold.ttf"] = 1.0 # RU - CSB/CE Themes
    config.ftfont_vertical_extent_scale["CP_Font_1.otf"] = 1.0 # JP - Credits
    config.ftfont_vertical_extent_scale["YuGothL.ttc"] = 1.0 # JP - Tate EX Theme
    config.ftfont_vertical_extent_scale["Source Han Sans CN Light.otf"] = 1.0 # CN - Tate EX Theme
    config.ftfont_vertical_extent_scale["Raleway-VariableFont_wght.ttf"] = 1.0 # RU - Tate EX Theme
    config.ftfont_vertical_extent_scale["Aller_Std_Lt_0.ttf"] = 1.0 # Tate EX Theme Main
    config.ftfont_vertical_extent_scale["AllerDisplay_Std_Rg_0.ttf"] = 1.0 # Tate EX Theme Accent
    config.ftfont_vertical_extent_scale["comic.ttf"] = 0.95 # Dyslexia - CSB/CE Themes
    config.ftfont_vertical_extent_scale["CenturyGothicPaneuropeanSemiBold.ttf"] = 1.2 # Dyslexia - Tate EX Theme

    # Dyslexia mode
    def dyslexia_font(f):
        return _font_transform(f, config.font_name_map["dyslexia"], "00-FFFF")

    config.font_transforms["dyslexia"] = dyslexia_font

# Default values for unlocks, etc
define determination = Dissolve(0.0)
default translate_this_line = ""
default persistent.seen = set()
default persistent.heard = set()
default persistent.collected = set()
default persistent.seen_music_pun = set()
default persistent.read = set()
default persistent.unlocked_achievements = set()
default persistent.fun = set()
default persistent.creative_mode = False
default persistent.show_cs_button = True
default persistent.awawa_mode = False
default persistent.seen_splash = False
default persistent.first_time = True
default persistent.woohoo = 0
default persistent.controller_id = 0
default persistent.true_ending = False
default persistent.got_awawad = False
default persistent.defeated_perfect_tate = False

# Theme handling
default persistent.unlocked_themes = set()

# Achievement progress
default persistent.seen_original_endings = set()
default persistent.seen_all_endings = set()
default persistent.max_pencil_score = 0
default persistent.max_pencil_score_ex = 0
default persistent.train_routes_seen = 0
default persistent.beach_routes_seen = 0
default persistent.timeline_trace_seen = 0

# Chapter unlocks
default persistent.csb2_unlocked = False
default persistent.csb3a_unlocked = False
default persistent.csb3b_unlocked = False

# Game unlocks: CE
default persistent.pre_christmas_theme = "default"
default persistent.carrot_fails = 0
default persistent.saved_christmas = False
default persistent.point_and_clicked = set()

# NO MORE MOUSE CURSOR HOUDINI
define config.mouse_hide_time = None

# Define layering
define config.top_layers = ["music"]
define config.bottom_layers = ["flashlight"]

# Reversi Difficulty
default reversi_difficulty = ReversiAI.GOBLIN

# Music popup
screen music():
    layer "music"
    style_prefix "music"

    frame at music_appear:
        image "_music_text"

    timer 5 action Hide(_layer='music')

transform music_appear:
    on show:
        xanchor 1.0 xpos 0
        easein_cubic 1 xanchor 0.0
    on hide:
        easein_cubic 1 xanchor 1.0

style music_frame is empty
style music_frame:
    background "#0007"
    yoffset 25

init:
    # For music
    transform _music_top_left:
        xanchor 0 xpos 0

    # For fun value
    transform _fun_value_fade:
        on show:
            xanchor 0 xpos 18
            yanchor 0 ypos 980
            alpha 0.00
            ease_cubic 0.5 alpha 1.00
            time 2.5
            ease_expo 1 alpha 0.00

    transform _fun_value_motion:
        block:
            # back
            ease_cubic 0.1 xpos 17
            ease_cubic 0.01 ypos 979
            # forward
            ease_cubic 0.1 xpos 19
            ease_cubic 0.01 ypos 981
            repeat

python early:
    # MUSIC POP UP

    import json

    _current_song = ""
    _current_artist = ""
    _current_internal_id = ""
    _played_songs = set()

    def parse_music(lexer):
        string = lexer.rest()
        if string == "end":
            return None
        return string

    def lint_music(parsed_object):
        ...

    def execute_music(parsed_object):

        global _current_song
        global _current_artist
        global _current_internal_id

        if parsed_object is None:
            _current_song = None
            _current_artist = None
            _current_internal_id = None
            return
        else:
            _current_internal_id = str(parsed_object)
            _current_song = MUSIC_MAP.get(_current_internal_id)["title"]
            _current_artist = MUSIC_MAP.get(_current_internal_id)["artist"]

            # for debugging
            #logger.info(f"Currently held data: {_current_song} by {_current_artist} | Internal ID: {_current_internal_id}")

        if (_current_song, _current_artist) not in _played_songs:
            _played_songs.add((_current_song, _current_artist))
            persistent.heard.add(_current_internal_id)
            renpy.with_statement(determination)
            renpy.show_screen("music")
            renpy.with_statement(determination)
        if all([a in persistent.heard for a in MUSIC_MAP.keys()]):
            achievement_manager.unlock("jukebox")

    renpy.register_statement(name="music",
        parse = parse_music,
        lint = lint_music,
        execute = execute_music)

    # DXCOM

    def parse_dxcom(lexer):
        string = lexer.rest()
        return string

    def execute_dxcom(parsed_object):
        if parsed_object is None:
            return
        renpy.play("sfx/sfx_bubble.ogg", channel = "notification")
        renpy.with_statement(determination)
        renpy.show_screen("dxcom", parsed_object)
        renpy.with_statement(determination)

    def lint_dxcom(parsed_object):
        if parsed_object is None:
            pass

    renpy.register_statement("dxcom",
        parse = parse_dxcom,
        lint = lint_dxcom,
        execute = execute_dxcom)

screen fun_value_indicator(t):
    # TODO: TATE DO THIS FOR ME I'M LAZY
    tag fun_value_indicator
    modal False
    text t:
        align (0.0, 1.0)

init python:
    import re

    # MUSIC POPUP
    def _music_gen_text(st, at):
        return HBox(
            Transform(Image("gui/music_note.png"), zoom = 0.2, xoffset = 25),
            Null(width = 35),
            VBox(
                Text("{font=music_text}" + _current_song if _current_song is not None else "", size = 72, outlines = [(4.5, "#000000", 0, 0)]),
                Text("{font=music_text}" + _current_artist if _current_artist is not None else "", size = 32, outlines = [(2.25, "#000000", 0, 0)])
            ),
            margin = (35, 25)
        ), None

    renpy.image("_music_text", DynamicDisplayable(_music_gen_text))

    # GET CURRENT SONG
    def set_now_playing():

        global _current_song
        global _current_artist
        global _current_internal_id

        current = re.sub(r'(<.*>)', "", str(renpy.music.get_playing("music")), flags=re.IGNORECASE)

        if not current:
            _current_song = None
            _current_artist = None
            renpy.restart_interaction()
        else:
            for t in MUSIC_MAP:
                if current in MUSIC_MAP[t]["file"]:
                    _current_internal_id = t
                    _current_song = MUSIC_MAP[t]["title"]
                    _current_artist = MUSIC_MAP[t]["artist"]

            return _current_internal_id

    # ANIM CODE LITERALLY FROM CHARM
    def clamp(minVal, val, maxVal):
        """Clamp a `val` to be no lower than `minVal`, and no higher than `maxVal`."""
        return max(minVal, min(maxVal, val))

    def find_percent(start: float, end: float, x: float) -> float:
        """Convert a number to its progress through the range start -> end, from 0 to 1.

        https://www.desmos.com/calculator/d2qdk3lceh"""
        if end - start == 0:
            return 1
        y = ((1 / (end - start)) * x) - (start / (end - start))
        return clamp(0, y, 1)

    def lerp(start: float, end: float, i: float) -> float:
        """Convert a number between 0 and 1 to be the progress within a range start -> end."""
        return start + (i * (end - start))

    def ease_linear(minimum: float, maximum: float, start: float, end: float, x: float) -> float:
        """* `minimum: float`: the value returned by f(`x`) = `start`, often a position
        * `maximum: float`: the value returned by f(`x`) = `end`, often a position
        * `start: float`: the beginning of the transition, often a time
        * `end: float`: the end of the transition, often a time
        * `x: float`: the current x, often a time"""
        x = find_percent(start, end, x)
        return lerp(minimum, maximum, x)

    def ease_quad(minimum: float, maximum: float, start: float, end: float, x: float) -> float:
        """https://easings.net/#easeInOutQuad"""
        x = find_percent(start, end, x)
        if x < 0.5:
            zo = 2 * x * x
        else:
            zo = 1 - math.pow(-2 * x + 2, 2) / 2
        return lerp(minimum, maximum, zo)

    def ease_exp(minimum: float, maximum: float, start: float, end: float, x: float) -> float:
        """https://easings.net/#easeInExpo"""
        x = find_percent(start, end, x)
        zo = math.pow(2, 10 * x - 10)
        return lerp(minimum, maximum, zo)

    def easeout_circ(minimum: float, maximum: float, start: float, end: float, x: float) -> float:
        """https://easings.net/#easeOutCirc"""
        x = find_percent(start, end, x)
        zo = math.sqrt(1 - math.pow(x - 1, 2))
        return lerp(minimum, maximum, zo)

    # I think I stole this from SizeBot, don't tell anyone
    def sentence_join(items, *, joiner=None, oxford=False) -> str:
        """Join a list of strings like a sentence."""
        # Do this in case we received something like a generator, that needs to be wrapped in a list
        items = list(items)

        if len(items) == 1:
            return items[0]

        if not items:
            return ""

        if joiner is None:
            joiner = "and"

        ox = ""
        if oxford:
            ox = ","

        return f"{', '.join(items[:-1])}{ox if len(items) >= 3 else ''} {joiner} {items[-1]}"

    # Fun value handler
    def fun_value(rarity: int, id: str = None, *, confusing = False, fish = False) -> bool:

        # hide any previous instance of the indicator
        renpy.hide_screen("fun_value_indicator")

        if not preferences.bounciness_enable:
            return False
        if rarity > preferences.max_fun and rarity < 99:
            return False
        if confusing and not preferences.confusing_joke_enable:
            return False
        if rarity == FUN_VALUE_MUSIC and not preferences.music_joke_enable:
            return False

        if id is not None:
            if rarity == FUN_VALUE_MUSIC:
                persistent.seen_music_pun.add(id)
            else:
                persistent.fun.add(id)

        r = ease_linear(rarity, 1, 0, 100, preferences.csbounciness)
        chance = 1 / r
        ret = renpy.random.random() < chance
        if ret:
            achievement_manager.unlock("fun")
            # Show the indicator. It'll fade out on its own and be hidden next time this runs.
            if rarity == FUN_VALUE_MUSIC:
                # Music indicator
                renpy.show_screen("fun_value_indicator", "music")
            else:
                if renpy.random.random() < FUN_VALUE_FISH_CHANCE or fish:
                    # Fish indicator
                    renpy.show_screen("fun_value_indicator", "fish")
                else:
                    # Normal indicator
                    renpy.show_screen("fun_value_indicator", "normal")
            renpy.play("audio/sfx/sfx_sparkle.ogg", channel = "notification")
        return ret

    def fun_value_found():
        # hide any previous instance of the indicator
        renpy.hide("_fun_value")
        renpy.hide("_fun_value_music")
        renpy.hide("_fun_value_fish")
        renpy.hide("_fun_value_found")

        renpy.show("_fun_value_found",[_fun_value_fade,_fun_value_motion],"fun_icon")
        renpy.play("audio/sfx/sfx_sparkle.ogg", channel = "notification")

    # File listing
    def file_list(dir=""):
        l = renpy.list_files()
        rv = []
        for f in l:
            if re.match(dir,f):
                rv.append(f[(len(dir)):])
        return rv

    # Image scaling

    def get_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h

    def ProportionalScale(img, maxwidth, maxheight):
        currentwidth, currentheight = get_size(img)
        xscale = float(maxwidth) / float(currentwidth)
        yscale = float(maxheight) / float(currentheight)

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return Transform(img, zoom = minscale)

    from typing import Generic, Sequence, Tuple, TypeVar, Union
    from bisect import bisect_left, bisect_right

    T = TypeVar("T")
    K = TypeVar("K")


    # NATALIE WROTE THIS
    class Index(Generic[K, T]):
        """
        Class to provide efficient indexing and slicing operations into a list of objects by certain attribute key.

        This with *only* work if:
        - The list is sorted
        - The list doesn't change

        I have not tested how this will handle duplicate values.
        """

        def __init__(self, items: Sequence[T], keyattr: str):
            self.items = items
            self.keys: Tuple[K] = tuple(getattr(i, keyattr) for i in items)

        def __getitem__(self, key: Union[slice, K]) -> T:
            if not isinstance(key, slice):
                return self.eq(key)

            start_index = key.start
            if start_index is not None:
                start_index = self.gteq_index(start_index)
                if start_index is None:
                    return []

            stop_index = key.stop
            if stop_index is not None:
                stop_index = self.gteq_index(stop_index)

            return self.items[start_index:stop_index:key.step]

        def eq(self, key: K) -> T:
            index = self.eq_index(key)
            if index is None:
                return None
            return self.items[index]

        def lteq(self, key: K) -> T:
            index = self.lteq_index(key)
            if index is None:
                return None
            return self.items[index]

        def lt(self, key: K) -> T:
            index = self.lt_index(key)
            if index is None:
                return None
            return self.items[index]

        def gteq(self, key: K) -> T:
            index = self.gteq_index(key)
            if index is None:
                return None
            return self.items[index]

        def gt(self, key: K) -> T:
            index = self.gt_index(key)
            if index is None:
                return None
            return self.items[index]

        def eq_index(self, key: K) -> int:
            index = self.gteq_index(key)
            if index is None:
                return None
            if self.keys[index] != key:
                return None
            return index

        def lteq_index(self, key: K) -> int:
            index = bisect_right(self.keys, key) - 1
            if index == -1:
                return None
            return index

        def lt_index(self, key: K) -> int:
            index = bisect_left(self.keys, key) - 1
            if index == -1:
                return None
            return index

        def gt_index(self, key: K) -> int:
            index = bisect_right(self.keys, key)
            if index == len(self.keys):
                return None
            return index

        def gteq_index(self, key: K) -> int:
            index = bisect_left(self.keys, key)
            if index == len(self.keys):
                return None
            return index

default mouse_xy = (0, 0)

init python:
    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()
