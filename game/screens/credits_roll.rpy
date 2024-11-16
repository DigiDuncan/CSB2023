init python:
    import re
    import json

    with renpy.open_file("data/credits.json") as json_file:
        credits_file = json.load(json_file)

    with renpy.open_file("data/jukebox.json") as json_file:
        jukebox_file = json.load(json_file)

    global credits_map
    global music_map

    credits_map = credits_file
    # sort jukebox by artist this time
    #music_map = sorted(jukebox_file["tracks"], key=lambda a: jukebox_file["tracks"][a]["artist"])
    music_map = jukebox_file["tracks"]

screen credits_roll(route="All", bgm="goodbye_summer_hello_winter.ogg"):

    modal True
    zorder 1

    on "show" action Play("music", bgm, loop=False, if_changed=True)

    for b in music_map:
        if music_map[b]["file"] == bgm and b not in persistent.heard:
            $ persistent.heard.add(b)
            break

    # by default, show the full game's credits. this will allow us to write credits per-route at a later date.
    # chosen route MUST match jukebox JSON tagging

    add color("#000000")

    # TODO: this will not be a scrollable frame forever, just until i make sure formatting is correct
    frame:
        background None

        viewport:
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            scrollbars "vertical"

            fixed:
                #background None
                xsize 1920
                xalign 0.5
                ypos 0

                ##### BEGIN CONTENTS #####
                image "gui/credits/csbiiidx_small.png":
                    xalign 0.5

                frame:
                    background None
                    xalign 0.5
                    ypos 300

                    vbox:
                        xsize 1600
                        xalign 0.5

                        for category in credits_map[route]:
                            frame:
                                background None
                                xsize 1600

                                vbox:
                                    xsize 1600

                                    # big categories get printed in the center, if they exist.
                                    # categories with underscores are strictly for organization and should not be printed.
                                    if category[0] == "_":
                                        $ cat_text = "\n"
                                    else:
                                        $ cat_text = category

                                    frame:
                                        background None
                                        xsize 1600
                                        ysize 150
                                        xalign 0.5
                                        text cat_text:
                                            xalign 0.5
                                            yalign 0.5
                                            size 64
                                            font "impact.ttf"
                                    
                                    for subcategory in credits_map[route][category]:

                                        # Handling for everything EXCEPT special thanks and music
                                        # These are nested for a reason
                                        if category != "Special Thanks":
                                            if category != "Music":
                                                hbox:
                                                    xsize 1600
                                                    
                                                    $ sub_text = subcategory

                                                    # manually hide awawa mode if unseen
                                                    if persistent.awawa_mode == False and re.fullmatch("Awawa Mode Programming Assistance", subcategory):
                                                        $ sub_text = obfuscator(subcategory)

                                                    # manually hide characters if not seen
                                                    if "tate_ex" not in persistent.seen and re.fullmatch("Tate EX", subcategory):
                                                        $ sub_text = obfuscator(subcategory)
                                                    if "perfect_tate" not in persistent.seen and re.fullmatch("Perfect Tate", subcategory):
                                                        $ sub_text = obfuscator(subcategory)
                                                    if "mean_human" not in persistent.seen and re.fullmatch("Mean \(Human\)", subcategory):
                                                        $ sub_text = obfuscator(subcategory)

                                                    # print the subcategory
                                                    frame:
                                                        background None
                                                        xsize 900
                                                        text sub_text:
                                                            xalign 0.0
                                                            size 48
                                                            font "impact.ttf"

                                                    # get contributors
                                                    vbox:
                                                        xalign 1.0
                                                        for contributor in credits_map[route][category][subcategory]:
                                                            text contributor:
                                                                xalign 1.0

                                            # music requires special handling
                                            else:
                                                $ song = ""
                                                $ artist = ""

                                                for track in music_map:

                                                    # only get tracks for a given route, or if none specified, get everything
                                                    if route == "All":
                                                        # hide unheard tracks
                                                        if track in persistent.heard:
                                                            $ song = music_map[track]["title"]
                                                            if artist != music_map[track]["artist"]:
                                                                $ artist = music_map[track]["artist"]
                                                        else:
                                                            $ song = obfuscator(music_map[track]["title"])
                                                            $ artist = obfuscator(music_map[track]["artist"])
                                                    else:
                                                        if route in music_map[track]["tags"]:
                                                            # hide unheard tracks
                                                            if track in persistent.heard:
                                                                $ song = music_map[track]["title"]
                                                                if artist != music_map[track]["artist"]:
                                                                    $ artist = music_map[track]["artist"]
                                                            else:
                                                                $ song = obfuscator(music_map[track]["title"])
                                                                $ artist = obfuscator(music_map[track]["artist"])

                                                    hbox:
                                                        xsize 1600
                                                        frame:  
                                                            background None
                                                            xsize 900
                                                            text "{font=credits_music}"+song:
                                                                xalign 0.0
                                                                size 48

                                                        vbox:
                                                            xalign 1.0
                                                            xsize 600
                                                            text "{font=music_text}"+artist:
                                                                xalign 1.0
                                                
                                        # for special thanks
                                        elif category == "Special Thanks":
                                            vbox:
                                                xsize 1600
                                                
                                                $ thanks_text = subcategory
                                                $ thanks_for_text = credits_map[route][category][subcategory][0]

                                                # print the thanks + text under it
                                                vbox:
                                                    xsize 1600
                                                    text thanks_text:
                                                        xalign 0.5
                                                        size 48
                                                        font "impact.ttf"
                                                    text thanks_for_text+"\n":
                                                        xalign 0.5

                        # DPN logo
                        frame:
                            background None
                            ysize 500
                        image "gui/credits/dpn_logo.png":
                            xalign 0.5
                            yalign 1.0
                        text "DPN Games":
                            yoffset -128
                            size 96
                            xalign 0.5
                        text "MMXXIV":
                            yoffset -128
                            size 96
                            xalign 0.5


    ########## CLICK ANYWHERE TO KILL IT ##########
    button:
        xysize (1920, 1080)
        action [Stop("music"), Return()]
