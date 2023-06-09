$ _current_song = ""
$ _current_artist = ""

init:
    transform _music_top_left:
        ease_cubic 1 xanchor 0

python early:
    def parse_music(lexer):
        string = lexer.rest()
        title, author = string.split("-", 2)
        return (title, author)

    def execute_music(parsed_object):
        global _current_song
        global _current_artist
        _current_song = parsed_object[0].strip()
        _current_artist = parsed_object[1].strip()
        renpy.with_statement(determination)
        renpy.show("_music_text", layer = "master", at_list = [_music_top_left])
        renpy.with_statement(easeinleft)

    def lint_music(parsed_object):
        pass

    renpy.register_statement("music",
        parse = parse_music,
        lint = lint_music,
        execute = execute_music)

init python:
    def _music_gen_text(st, at):
        return HBox(Transform(Image("music_note.png"), zoom = 0.2),
            Null(width = 35),
            VBox(
                Text(_current_song, size = 72, outlines = [(5, "#000000", 0, 0)]),
                Text(_current_artist, size = 32, outlines = [(3, "#000000", 0, 0)])
            )
        ), None

    renpy.image("_music_text", DynamicDisplayable(_music_gen_text))
