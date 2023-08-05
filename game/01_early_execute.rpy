init python:
    renpy.add_layer("music", above = "master")
    renpy.add_layer("popup", above = "overlay")

define determination = Dissolve(0.0)
default persistent.seen = set()
default persistent.heard = set()
default persistent.true_ending = False

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
    transform _music_top_left:
        xanchor 0 xpos 0

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

    def lint_music(parsed_object):
        if parsed_object is None:
            pass
        elif parsed_object[0] == "" or parsed_object[1] == "":
            renpy.error("Title or author is empty for music popup.")

    renpy.register_statement("music",
        parse = parse_music,
        lint = lint_music,
        execute = execute_music)

default fun_values_seen = set()

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

    # FUN VALUES
    def fun_value(rarity: int, id: str = None) -> bool:
        if not preferences.bounciness_enable:
            return False
        chance = ease_linear(1 / rarity, 1, 0, 100, preferences.csbounciness)
        ret = renpy.random.random() < chance
        if ret and id is not None:
            fun_values_seen.add(id)
        elif not ret and id is not None:
            fun_values_seen.remove(id)
        return ret

    def event_happened(id: str) -> bool:
        return id in fun_values_seen
