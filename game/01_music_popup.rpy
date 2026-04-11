# Music popup
screen music(song = "", artist = ""):
    layer "music"
    style_prefix "music"

    frame at music_appear:
        hbox:
            add "gui/music_note.png":
                zoom 0.2
                xoffset 25
            null width 35
            vbox:
                $ song_text = "{font=music_text}" + song if song is not None else ""
                $ artist_text = "{font=music_text}" + artist if artist is not None else ""
                text song_text:
                    size 72
                    outlines [(4.5, "#000000", 0, 0)]
                text artist_text:
                    size 32
                    outlines [(2.25, "#000000", 0, 0)]

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

python early:
    _played_songs = set()

    def parse_music(lexer):
        string = lexer.rest()
        if string == "end":
            return None
        elif ":" in string:
            return [s.strip("\"") for s in string.rsplit(":")]
        return string

    def lint_music(parsed_object):
        ...

    def execute_music(parsed_object):
        global _played_songs

        current_internal_id = None
        current_song = None
        current_artist = None

        if parsed_object is None:
            return
        if isinstance(parsed_object, str):
            current_internal_id = str(parsed_object)
            current_song = MUSIC_MAP.get(current_internal_id)["title"]
            current_artist = MUSIC_MAP.get(current_internal_id)["artist"]
        else:
            current_song = parsed_object[0]
            current_artist = parsed_object[1]

        if (current_song, current_artist) not in _played_songs:
            _played_songs.add((current_song, current_artist))
            if current_internal_id:
                persistent.heard.add(current_internal_id)
            renpy.with_statement(determination)
            renpy.show_screen("music", current_song, current_artist)
            renpy.with_statement(determination)
        if all([a in persistent.heard for a in MUSIC_MAP.keys()]):
            achievement_manager.unlock("jukebox")

    renpy.register_statement(name="music",
        parse = parse_music,
        lint = lint_music,
        execute = execute_music)
