init python:
    for n in persistent.heard:
        if n not in MUSIC_MAP:
            logger.warn(f"Track '{n}' not in MUSIC_MAP!")

###################################################### SETUP

screen jukebox():
    tag menu

    on "replace":
        action [
            PauseAudio("music", True),
            PauseAudio("music2", True),
            PauseAudio("music3", True),
            PauseAudio("music4", True),
            PauseAudio("music5", True),
            PauseAudio("sound", True),
            PauseAudio("sound2", True),
            PauseAudio("voice", True),
        ]
  
    python:
        music_count = len(MUSIC_MAP.keys())
        unlocked_music_count = len(persistent.heard)

        manual_sort_modes = [ "All", "By Title", "By Artist" ]
        full_mode_list = manual_sort_modes + TAGS_MAP
        tags_count = len(full_mode_list)

    default current_track = None
    default jukebox_playing = False
    default current_jukebox_tag_index = 0

    add gui_theme_map["screen_transparency_layer"]

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

                ### LEFT BUTTON
                if current_jukebox_tag_index-1>=0:
                    imagebutton:
                        xalign 0.0 yalign 0.5
                        xysize 64, 64

                        idle "/gui/left_off_small.png"
                        hover "/gui/left_on_small.png"

                        action SetScreenVariable("current_jukebox_tag_index", current_jukebox_tag_index-1)

                ### RIGHT BUTTON
                if current_jukebox_tag_index+1<tags_count:
                    imagebutton:
                        xalign 1.0 yalign 0.5
                        xysize 64, 64

                        idle "/gui/right_off_small.png"
                        hover "/gui/right_on_small.png"

                        action SetScreenVariable("current_jukebox_tag_index", current_jukebox_tag_index+1)

                # Since we can't exactly do anything about the index problem let's just hide unseen tags for now.
                # I want to use obfuscator() later but it's not ready yet.

                $ tags_label_text = full_mode_list[current_jukebox_tag_index]

                text tags_label_text:
                    xalign 0.5 yalign 0.5
                    text_align 0.5

                ####### TRACK LIST
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

                        ### BEGIN SORTING
                        python:
                            sorted_list = []

                            for track in MUSIC_MAP:
                                if track in persistent.heard:

                                    ### Display everything in the default order, which is mostly chronological
                                    if current_jukebox_tag_index == 0:
                                        sorted_list.append(MUSIC_MAP[track])
                                    ### Sort by title
                                    elif current_jukebox_tag_index == 1:
                                        sorted_list.append(MUSIC_MAP[track])
                                        sorted_list.sort(key = lambda song: song["title"].lower())
                                    ### Sort by artist, then title
                                    elif current_jukebox_tag_index == 2:
                                        sorted_list.append(MUSIC_MAP[track])
                                        sorted_list.sort(key = lambda song:( song["artist"].lower(), song["title"].lower() ))
                                    ### Sort by tag
                                    else:
                                        if full_mode_list[current_jukebox_tag_index] in MUSIC_MAP[track]["tags"]:
                                            sorted_list.append(MUSIC_MAP[track])

                        ### Finally display them
                        for track in sorted_list:
                            textbutton "{font=music_text}" + track["title"] + "\n{size=-12}" + track["artist"]:
                                action [
                                    SetScreenVariable("current_track", track),
                                    SetScreenVariable("jukebox_playing", True),
                                    SelectedIf( SetScreenVariable("current_track", track) ),
                                    Play("jukebox", track["file"])
                                ]

###################################################### SELECTION INFO

            frame:
                background None
                xsize 1320 ysize 1.0
                xalign 1.0 yalign 1.0

                ####### CURRENT SONG DATA
                if not current_track:
                    vbox:
                        xsize 0.8
                        xalign 0.5 yalign 0.6
                        text "Here, you can listen to all the sweet tunes you've discovered throughout CS' adventures!"
                        text "\n([unlocked_music_count]/[music_count] unlocked)"
                else:
                    frame:
                        background None
                        xsize 1.0 ysize 125
                        xalign 0.5 ypos 50

                        text "{font=music_text}{size=69}" + current_track["title"] + "\n{font=music_text}{size=45}" + current_track["artist"]:
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

                        if current_track["album_art"] is None:
                            image "images/jukebox/csbi.png":
                                xysize(512, 512)
                                xalign 0.5 yalign 0
                        else:
                            image f"images/jukebox/"+current_track["album_art"]:
                                xysize(512, 512)
                                xalign 0.5 yalign 0

                    frame:
                        background None
                        xsize 1200 ysize 175
                        xalign 0.5 yalign 1.0

                        vbox:
                            ####### CONTROLS
                            frame:
                                background None
                                xsize 1200
                                xalign 0.5 yalign 0
                                padding (20,20,20,20)

                                vbox:
                                    spacing 20
                                    xsize 0.5
                                    xalign 0.5

                                    # Add progress bar
                                    python:
                                        current_pos = AudioPositionValue(channel='jukebox', update_interval=0.1)

                                    bar:
                                        xalign 0.5
                                        style "slider"
                                        value current_pos
                                        
                                    # Pause button
                                    if jukebox_playing:
                                        imagebutton:
                                            at transform:
                                                xalign 0.5 yalign 0.5
                                                zoom 0.125
                                            idle "gui/pause.png"
                                            hover "gui/pause.png" # TODO: Actually make an image for this - Arc
                                            action [
                                                PauseAudio("jukebox", True),
                                                SetScreenVariable("jukebox_playing", False)
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
                                                SetScreenVariable("jukebox_playing", True)
                                            ]

                            ####### TRIVIA
                            frame:
                                background None
                                xsize 0.9 ysize 115
                                xalign 0.5 yalign 0
                                python:
                                    try:
                                        jukebox_trivia = current_track["trivia"]
                                    except:
                                        jukebox_trivia = ""

                                text "{size=-12}[jukebox_trivia]{/size}":
                                    xalign 0.5 yalign 0
                                    text_align 0.5

###################################################### BOTTOM BUTTON

    textbutton "Back":
        yoffset 1000 xoffset 25
        action [
            Stop("jukebox"),
            PauseAudio("music", False),
            PauseAudio("music2", False),
            PauseAudio("music3", False),
            PauseAudio("music4", False),
            PauseAudio("music5", False),
            PauseAudio("sound", False),
            PauseAudio("sound2", False),
            PauseAudio("voice", False),
            SelectedIf(False),
            ShowMenu("subgame")
        ]
