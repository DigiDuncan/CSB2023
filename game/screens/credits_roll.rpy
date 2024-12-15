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

transform credit_scroll(starting = 0, duration = 60):
    yanchor 1.0
    ypos starting
    # this end position is always the same, do not change it
    linear duration ypos 1075

screen credits_roll(route = "All", bgm = "goodbye_summer_hello_winter.ogg", scroll_start = 25500, duration = 343, replace_music = False):
    on "show":
        if replace_music == True:
            action Play("music", bgm, loop=False, if_changed=True)

    if bgm:
        for b in music_map:
            if music_map[b]["file"] == bgm and b not in persistent.heard:
                $ persistent.heard.add(b)
                break

    #only get tracks for a given route, or if none specified/invalid tag, get everything
    python:
        global jukebox_presort
        jukebox_presort = {}
        for song in music_map:
            if route == "All":
                jukebox_presort.update({ song : { "title": music_map[song]["title"], "artist": music_map[song]["artist"] } })
            else:
                if route in music_map[song]["tags"]:
                    jukebox_presort.update({ song : { "title": music_map[song]["title"], "artist": music_map[song]["artist"] } })

            jukebox_sorted = dict(sorted(jukebox_presort.items(), key = lambda a: (a[1]["artist"].lower(), a[1]["title"].lower())))

    modal True
    zorder 1

    # by default, show the full game's credits. this will allow us to write credits per-route at a later date.
    # chosen route MUST match jukebox JSON tagging

    add color("#000000")

    frame:
        background None
        xsize 1920
        xalign 0.5

        ##### BEGIN CONTENTS #####
        frame at credit_scroll(scroll_start, duration):
            background None
            xalign 0.5

            vbox:
                xsize 1600
                xalign 0.5

                frame:
                    background None
                    xsize 1600
                    ysize 1580
                    xalign 0.5

                for category in credits_map[route]:
                    frame:
                        background None
                        xsize 1600

                        vbox:
                            xsize 1600

                            # big categories get printed in the center, if they exist.
                            # categories with underscores are strictly for organization and should not be printed.
                            # some categories are hidden based on player progression
                            if category[0] == "_":
                                $ cat_text = "\n"
                            elif category == "CS-ocola (3D Sprite)":
                                if persistent.defeated_perfect_tate == False:
                                    $ cat_text = obfuscator(category)
                                else:
                                    $ cat_text = category
                            elif category == "DigiDuncan Character Sprite":
                                if "digi" not in persistent.seen:
                                    $ cat_text = obfuscator(category)
                                else:
                                    $ cat_text = category
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

                                # Handling for everything EXCEPT cast, special thanks, music, logo
                                # These are nested for a reason
                                if category != "Special Thanks" and category != "Cast" and category != "_logo":
                                    if category != "Music":
                                        hbox:
                                            xsize 1600

                                            $ sub_text = subcategory

                                            # manually hide awawa mode / CS 3D / digi sprite if unseen
                                            if ( (persistent.awawa_mode == False and re.fullmatch("Awawa Mode Programming Assistance", subcategory)) or (persistent.defeated_perfect_tate == False and category == "CS-ocola (3D Sprite)") or ("digi" not in persistent.seen and category == "DigiDuncan Character Sprite") ):
                                                $ sub_text = obfuscator(subcategory)

                                            # manually hide characters SPRITES if not seen, scroll down for CAST list
                                            $ hide_these = { "Arceus": "arceus", "Kitty": "kitty", "DigiDuncan": "digi", "Aria": "aria", "Pakoo": "pakoo", "Blank": "blank", "Bubble": "bubble", "Tate": "tate", "Tate EX": "tate_ex", "Perfect Tate": "perfect_tate", "Mean": "mean", "Mean \(Human\)": "mean_human", "Ges": "ges", "blanknam3d": "blank", "Midge": "midge", "Elizabeth": "eliza", "Anne": "anne", "Grace": "grace", "K-22": "k22", "K-17": "k17", "Addy": "addy", "Pakoopara": "k17", "Mikapara": "eliza" }

                                            for h in hide_these:
                                                if hide_these[h] not in persistent.seen and re.fullmatch(h, subcategory):
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

                                                    # manually hide CS 3D and Digi if unseen
                                                    if (persistent.defeated_perfect_tate == False and category == "CS-ocola (3D Sprite)") or ("digi" not in persistent.seen and category == "DigiDuncan Character Sprite"):
                                                        $ contributor = obfuscator(contributor)

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
                                # for game logo
                                elif category == "_logo":
                                    vbox:
                                        xsize 1600
                                        vbox:
                                            xsize 1600
                                            image credits_map[route][category][subcategory][0]:
                                                xalign 0.5
                                                yalign 0.5

                                # for cast
                                elif category == "Cast":
                                    vbox:
                                        xsize 1600
                                        # print the one line
                                        vbox:
                                            xsize 1600
                                            text subcategory+"\n":
                                                xalign 0.5
                                                size 48
                                                font "impact.ttf"

                                        # only print names if they've been seen
                                        python:
                                            hide_these = { "ItsNovaHere": "nova", "meancarnavor": "mean", "EddieJustEddie": "hoh_worker", "AFuckingChicken": "hoh_worker", "Guithais": "hoh_worker", "Arceus3251": "arceus", "Annorexorcist": "anno", "Aria \"Estroteric\"": "aria", "DigiDuncan": "digi", "Pakoopara": "pakoo", "Mikapara": "mika", "Tate \"alleZSoyez\"": "tate", "UndeadKitty": "kitty", "blanknam3d": "blank", "Ges \"DefinitelyNotGes\"": "ges", "Midgalicis": "midge", "db05": "db", "BubbleTheSlime": "bubble", "4Bakers": "iris" }

                                            char_text = ""

                                        for c in credits_map[route][category][subcategory]:
                                            if c in hide_these and hide_these[c] not in persistent.seen:
                                                $ char_text = obfuscator(c)
                                            else:
                                                $ char_text = c

                                            text char_text:
                                                xalign 0.5
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

    if renpy.context_nesting_level() != 0:
        dismiss action Play("music", "bubble_tea.ogg", loop = False), Jump("start")
    else:
        dismiss action [ Stop("music"), Return() ]
