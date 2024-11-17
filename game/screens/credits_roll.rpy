init python:
    import re
    import json

    with renpy.open_file("data/credits.json") as json_file:
        credits_file = json.load(json_file)

    with renpy.open_file("data/jukebox.json") as json_file:
        jukebox_file = json.load(json_file)

    global credits_map
    global music_map
    global jukebox_presort

    credits_map = credits_file
    music_map = jukebox_file["tracks"]
    jukebox_presort = {}

transform credit_scroll(starting = 0, ending = 0, duration = 60):
    ypos starting
    linear duration ypos ending

screen credits_roll(route = "All", bgm = "goodbye_summer_hello_winter.ogg", scroll_end = -20000, duration = 343):
    on "show" action Play("music", bgm, loop=False, if_changed=True)

    #only get tracks for a given route, or if none specified/invalid tag, get everything
    python:
        for song in music_map:
            if route in music_map[song]["tags"]:
                jukebox_presort.update({ song : { "title": music_map[song]["title"], "artist": music_map[song]["artist"] } })
            else:
                jukebox_presort.update({ song : { "title": music_map[song]["title"], "artist": music_map[song]["artist"] } })
     
            jukebox_sorted = dict(sorted(jukebox_presort.items(), key = lambda a: a[1]["artist"]))
            print(jukebox_sorted)

    modal True
    zorder 1

    for b in music_map:
        if music_map[b]["file"] == bgm and b not in persistent.heard:
            $ persistent.heard.add(b)
            break

    # by default, show the full game's credits. this will allow us to write credits per-route at a later date.
    # chosen route MUST match jukebox JSON tagging

    add color("#000000")

    frame:
        background None
        xsize 1920
        xalign 0.5

        ##### BEGIN CONTENTS ##### 
        frame at credit_scroll(0, scroll_end, duration):
            background None
            xalign 0.5

            vbox:
                xsize 1600
                xalign 0.5

                # game logo
                frame:
                    background None
                    xsize 1600
                    ysize 1580
                    xalign 0.5
                    image "gui/credits/csbiiidx_small.png":
                        xalign 0.5
                        yalign 1.0

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
                                                        yalign 0.5

                                    # music requires special handling
                                    # use the pre-sorted list from earlier, hide unseen tracks
                                    else:
                                        $ title = ""
                                        $ artist = None
                                        $ artist_displayed = ""

                                        for track in jukebox_sorted:
                                            if track in persistent.heard:
                                                $ title = jukebox_sorted[track]["title"]
                                                # make duplicate artists not repeat
                                                if jukebox_sorted[track]["artist"] == artist:
                                                    $ artist_displayed = ""
                                                else:
                                                    $ artist = jukebox_sorted[track]["artist"]
                                                    $ artist_displayed = artist
                                            else:
                                                $ title = obfuscator(jukebox_sorted[track]["title"])
                                                $ artist = obfuscator(jukebox_sorted[track]["artist"])
                                                $ artist_displayed = artist

                                            hbox:
                                                xsize 1600
                                                frame:  
                                                    background None
                                                    xsize 900
                                                    text "{font=credits_music}"+title:
                                                        xalign 0.0
                                                        size 48

                                                vbox:
                                                    xalign 1.0
                                                    xsize 600
                                                    text "{font=music_text}"+artist_displayed:
                                                        xalign 1.0
                                                        yalign 0.5
                                        
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
                                                yalign 0.5

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
