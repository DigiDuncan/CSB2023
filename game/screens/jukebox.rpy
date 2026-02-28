init python:
    for n in persistent.heard:
        if n not in MUSIC_MAP:
            print(f"WARNING: Track '{n}' not in MUSIC_MAP!")

###################################################### SETUP

screen jukebox():
    tag menu

    python:
        music_count = len(MUSIC_MAP.keys())
        unlocked_music_count = len(persistent.heard)

    default current_track = None

    add Color('#323e42', alpha=0.75)

    frame:
        background None
        xsize 1920 ysize 945
        hbox:

###################################################### SIDE MENU

            ####### TAGS
            frame:
                background None
                xsize 600 ysize 64
                xpos 25 ypos 25

                imagebutton:
                    xalign 0.0 yalign 0.5
                    xysize 64, 64

                    idle "/gui/left_off_small.png"
                    hover "/gui/left_on_small.png"

                    if current_jukebox_tag_index-1>=0:
                        action SetVariable("current_jukebox_tag_index", current_jukebox_tag_index-1)

                imagebutton:
                    xalign 1.0 yalign 0.5
                    xysize 64, 64

                    idle "/gui/right_off_small.png"
                    hover "/gui/right_on_small.png"

                    if current_jukebox_tag_index+1<len(TAGS_MAP):
                        action SetVariable("current_jukebox_tag_index", current_jukebox_tag_index+1)

                # since we can't exactly do anything about the index problem let's just hide unseen tags. want to use obfuscator() later but it's not ready yet.

                $ found_match = False
                $ tags_label_text = TAGS_MAP[current_jukebox_tag_index]

                for song in persistent.heard:
                    if TAGS_MAP[current_jukebox_tag_index] in MUSIC_MAP[song]["tags"]:
                        $ found_match = True
                        break

                if found_match or TAGS_MAP[current_jukebox_tag_index] == "All":
                    $ tags_label_text = TAGS_MAP[current_jukebox_tag_index]
                else:
                    $ tags_label_text = "(Locked)"

                text tags_label_text:
                    xalign 0.5 yalign 0.5
                    text_align 0.5

                ####### MUSIC LIST
                viewport:
                    xpos -6 ypos 58
                    xsize 600 ysize 850
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    scrollbars "vertical"
                    vbox:
                        spacing 10
                        xoffset 350
                        for k in MUSIC_MAP:
                            if k in persistent.heard:
                                # display all
                                if current_jukebox_tag_index == 0:
                                    textbutton "{font=music_text}" + MUSIC_MAP[k]["title"]+"\n{size=-12}"+MUSIC_MAP[k]["artist"]:
                                        action [
                                            SetScreenVariable("current_track", k),
                                            SetVariable("jukebox_playing", True),
                                            SelectedIf( SetVariable("current_track", k) ),
                                            Function(renpy.music.set_volume, 0.0, channel="music"),
                                            Play("jukebox", MUSIC_MAP[k]["file"])
                                        ]
                                # only display per tag
                                else:
                                    if TAGS_MAP[current_jukebox_tag_index] in MUSIC_MAP[k]["tags"]:
                                        textbutton "{font=music_text}" + MUSIC_MAP[k]["title"]+"\n{size=-12}"+MUSIC_MAP[k]["artist"]:
                                            action [
                                                SetScreenVariable("current_track", k),
                                                SetVariable("jukebox_playing", True),
                                                SelectedIf( SetVariable("current_track", k) ),
                                                Function(renpy.music.set_volume, 0.0, channel="music"),
                                                Play("jukebox", MUSIC_MAP[k]["file"])
                                            ]

###################################################### MUSIC INFO

            frame:
                background None
                xsize 1320 ysize 1.0
                xalign 1.0 yalign 1.0

                ####### CURRENT SONG DATA
                if not current_track:
                    vbox:
                        xsize 0.8
                        xalign 0.5 yalign 0.5
                        text "Here, you can listen to all the sweet tunes you've discovered throughout CS' adventures!"
                        text "\n([unlocked_music_count]/[music_count] unlocked)"
                else:
                    frame:
                        background None
                        xsize 1.0 ysize 125
                        xalign 0.5 ypos 50

                        text "{font=music_text}{size=69}" + MUSIC_MAP[current_track]["title"] + "\n{font=music_text}{size=45}" + MUSIC_MAP[current_track]["artist"]:
                            text_align 0.5
                            xalign 0.5

                    ####### ALBUM ART
                    frame:
                        background None
                        xsize 1200 ysize 700
                        xalign 0.5 yalign 1.0

                        if jukebox_playing:
                            image "images/jukebox/record.png":
                                xysize(500, 500)
                                xalign 0.8 yalign 0
                                yoffset -100 # idk why this needs this - tate
                                at transform:
                                    rotate 0
                                    linear 5.0 rotate 360.0
                                    repeat
                        else:
                            image "images/jukebox/record.png":
                                xysize(500, 500)
                                xalign 0.8 yalign 0
                                yoffset -100 # idk why this needs this - tate
                                at transform:
                                    rotate 0 # TODO: make it stop at current position when paused?

                        if MUSIC_MAP[current_track]["album_art"] is None:
                            image "images/jukebox/csbi.png":
                                xysize(512, 512)
                                xalign 0.5 yalign 0
                        else:
                            image f"images/jukebox/"+MUSIC_MAP[current_track]["album_art"]:
                                xysize(512, 512)
                                xalign 0.5 yalign 0

                    frame:
                        background None
                        xsize 1200 ysize 175
                        xalign 0.5 yalign 1.0

                        ####### CONTROLS
                        frame:
                            background None
                            xsize 1200 ysize 64
                            xalign 0.5 yalign 0

                            if jukebox_playing:
                                imagebutton:
                                    at transform:
                                        xalign 0.5 yalign 0.5
                                        zoom 0.125
                                    idle "gui/pause.png"
                                    hover "gui/pause.png" # TODO: Actually make an image for this - Arc
                                    action [
                                        PauseAudio("jukebox", True),
                                        SetVariable("jukebox_playing", False)
                                    ]
                            else:
                                imagebutton:
                                    at transform:
                                        xalign 0.5 yalign 0.5
                                        zoom 0.125
                                    idle "gui/play.png"
                                    hover "gui/play.png" # TODO: Actually make an image for this - Arc
                                    action [
                                        PauseAudio("jukebox", False),
                                        SetVariable("jukebox_playing", True)
                                    ]

                        ####### TRIVIA
                        frame:
                            background None
                            xsize 1.0 ysize 111
                            xalign 0.5 yalign 1.0
                            python:
                                try:
                                    jukebox_trivia = MUSIC_MAP[current_track]["trivia"]
                                except:
                                    jukebox_trivia = ""

                            text "{size=-12}[jukebox_trivia]{/size}":
                                text_align 0.5
                                xalign 0.5 yalign 0.5

###################################################### BOTTOM BUTTONS

    textbutton "Back":
        yoffset 950 xoffset 25
        action [
            Stop("jukebox"),
            Function(renpy.music.set_volume, 1.0, 0.5, channel="music"),
            SetVariable("current_track", None),
            SelectedIf(False),
            ShowMenu("subgame")
        ]
    textbutton "Main Menu":
        yoffset 1000 xoffset 25
        action [
            Stop("jukebox"),
            Function(renpy.music.set_volume, 1.0, 0.5, channel="music"),
            SetVariable("current_track", None),
            SelectedIf(False),
            Return()
        ]
