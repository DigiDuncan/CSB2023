$ _current_song = ""
$ _current_artist = ""

define determination = Dissolve(0.0)

screen music():
    zorder 100
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
    def parse_music(lexer):
        string = lexer.rest()
        title, author = string.split("-", 2)
        return (title, author)

    def execute_music(parsed_object):
        global _current_song
        global _current_artist
        _current_song = parsed_object[0].strip().removeprefix("\"")
        _current_artist = parsed_object[1].strip().removesuffix("\"")
        renpy.with_statement(determination)
        renpy.show_screen("music")

    def lint_music(parsed_object):
        if title == "" or author == "":
            renpy.error("Title or author is empty for music popup.")

    renpy.register_statement("music",
        parse = parse_music,
        lint = lint_music,
        execute = execute_music)

init python:
    def _music_gen_text(st, at):
        return HBox(
            Transform(Image("music_note.png"), zoom = 0.2, xoffset = 25),
            Null(width = 35),
            VBox(
                Text(_current_song, size = 72, outlines = [(5, "#000000", 0, 0)]),
                Text(_current_artist, size = 32, outlines = [(3, "#000000", 0, 0)])
            ),
            margin = (35, 25)
        ), None

    renpy.image("_music_text", DynamicDisplayable(_music_gen_text))
