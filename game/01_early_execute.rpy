init python:
    renpy.add_layer("music", above = "master")
    renpy.add_layer("popup", above = "overlay")
    renpy.add_layer("fun_icon", above = "master")

# WARN:
# For some reason the linter thinks that persistent variables with underscores
# are never initialized. It's lying to you; it's fine.

define determination = Dissolve(0.0)
default persistent.seen = set()
default persistent.heard = set()
default persistent.read = set()
default persistent.true_ending = False
default persistent.creative_mode = False
default persistent.seen_splash = False
default persistent.first_time = True

# Chapter unlocks
default persistent.csb2_unlocked = False
default persistent.csb3a_unlocked = False
default persistent.csb3b_unlocked = False

# Register CJK font
define config.font_name_map["cjk"] = "ZCOOLKuaiLe-Regular.ttf"

screen music():
    zorder 100
    layer "music"
    style_prefix "music"

    frame at music_appear:
        image "_music_text"

    timer 5 action Hide('music')

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
            xanchor 0 xpos 23
            yanchor 0 ypos 992
            alpha 0.00
            linear 0.5 alpha 1.00
            time 2.5
            linear 1 alpha 0.00

    transform _fun_value_motion:
        block:
            # back
            linear 0.1 xpos 22
            linear 0.01 ypos 991
            # forward
            linear 0.1 xpos 24
            linear 0.01 ypos 993
            repeat

python early:
    # MUSIC POP UP
    _current_song = ""
    _current_artist = ""
    _played_songs = set()

    def parse_music(lexer):
        string = lexer.rest()
        if string == "end":
            return None
        title, author = string.split("-", 2)
        return (title, author)

    def execute_music(parsed_object):
        global _current_song
        global _current_artist
        if parsed_object is None:
            _current_song = None
            _current_artist = None
            return
        _current_song = parsed_object[0].strip().removeprefix("\"")
        _current_artist = parsed_object[1].strip().removesuffix("\"")
        if (_current_song, _current_artist) not in _played_songs:
            _played_songs.add((_current_song, _current_artist))
            persistent.heard.add(f"{_current_song} - {_current_artist}")
            renpy.with_statement(determination)
            renpy.show_screen("music")
            renpy.with_statement(determination)
        if all([a in persistent.heard for a in music_map.keys()]):
            achievement_manager.unlock("The Brown Album")

    def lint_music(parsed_object):
        if parsed_object is None:
            pass
        elif parsed_object[0] == "" or parsed_object[1] == "":
            renpy.error("Title or author is empty for music popup.")

    renpy.register_statement("music",
        parse = parse_music,
        lint = lint_music,
        execute = execute_music)

init python:
    # MUSIC POPUP
    def _music_gen_text(st, at):
        return HBox(
            Transform(Image("music_note.png"), zoom = 0.2, xoffset = 25),
            Null(width = 35),
            VBox(
                Text(_current_song if _current_song is not None else "", size = 72, outlines = [(5, "#000000", 0, 0)]),
                Text(_current_artist if _current_artist is not None else "", size = 32, outlines = [(3, "#000000", 0, 0)])
            ),
            margin = (35, 25)
        ), None

    renpy.image("_music_text", DynamicDisplayable(_music_gen_text))

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

        return f"{', '.join(items[:-1])}{ox} {joiner} {items[-1]}"

    # FUN VALUES
    renpy.image("_fun_value", "fun_value.png")

    # Fun value handler
    def fun_value(rarity: int, id: str = None) -> bool:
    
        # hide any previous instance of the indicator
        renpy.hide("_fun_value") 

        if not preferences.bounciness_enable:
            return False
        r = ease_linear(rarity, 1, 0, 100, preferences.csbounciness)
        chance = 1 / r
        ret = renpy.random.random() < chance
        if ret:
            achievement_manager.unlock("F.U.N.")
            
            # show the indicator. it'll fade out on its own and be hidden next time this runs
            renpy.show("_fun_value",[_fun_value_fade,_fun_value_motion],"fun_icon")
            renpy.play("audio/sfx_sparkle.wav")
        return ret
