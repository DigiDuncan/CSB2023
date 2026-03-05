init python:
    global jukebox_presort
    jukebox_presort = {}

screen credits_roll(route = "All", bgm = "goodbye_summer_hello_winter.ogg", scroll_start = 0, duration = 343, replace_music = True):
    modal True
    zorder 1

    add color("#000000")

    on "show":
        if replace_music == True:
            action Play("music", bgm, loop=False, if_changed=True)

    if bgm:
        for b in MUSIC_MAP:
            if MUSIC_MAP[b]["file"] == bgm and b not in persistent.heard:
                $ persistent.heard.add(b)
                break

    # only get tracks for a given route, or if none specified/invalid tag, get everything
    python:
        global jukebox_presort
        jukebox_presort = {}
        for song in MUSIC_MAP:
            if route == "All":
                jukebox_presort.update({ song : { "title": MUSIC_MAP[song]["title"], "artist": MUSIC_MAP[song]["artist"] } })
            else:
                if route in MUSIC_MAP[song]["tags"]:
                    jukebox_presort.update({ song : { "title": MUSIC_MAP[song]["title"], "artist": MUSIC_MAP[song]["artist"] } })

            jukebox_sorted = dict(sorted(jukebox_presort.items(), key = lambda a: (a[1]["artist"].lower(), a[1]["title"].lower())))

    # By default, show the full game's credits. this will allow us to write credits per-route at a later date.
    # Chosen route MUST match jukebox JSON tagging.

    ##### BEGIN CONTENTS #####
    frame as credits_frame:
        background None
        xsize 1920
        xalign 0.5

        vbox:
            xsize 1600
            xalign 0.5

            frame:
                background None
                xsize 1600
                ysize 1580
                xalign 0.5

            for category in CREDITS_MAP[route]:
                frame:
                    background None
                    xsize 1600

                    vbox:
                        xsize 1600

                        # Big categories get printed in the center, if they exist.
                        # Categories with underscores are strictly for organization and should not be printed.
                        # Some categories are hidden based on player progression
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

                        for subcategory in CREDITS_MAP[route][category]:

                            # Handling for everything EXCEPT cast, special thanks, music, logo
                            # These are nested for a reason
                            if category != "Special Thanks" and category != "Cast" and category != "_logo":
                                if category != "Music":
                                    hbox:
                                        xsize 1600

                                        $ sub_text = subcategory

                                        # Manually hide Awawa Mode / CS 3D / Digi sprite if unseen
                                        if ( (persistent.awawa_mode == False and re.fullmatch("Awawa Mode Programming Assistance", subcategory)) or (persistent.defeated_perfect_tate == False and category == "CS-ocola (3D Sprite)") or ("digi" not in persistent.seen and category == "DigiDuncan Character Sprite") ):
                                            $ sub_text = obfuscator(subcategory)

                                        # Manually hide characters SPRITES if not seen, scroll down for CAST list
                                        $ hide_these = { "Arceus": "arceus", "Kitty": "kitty", "DigiDuncan": "digi", "Aria": "aria", "Pakoo": "pakoo", "Blank": "blank", "Bubble": "bubble", "Tate": "tate", "Tate EX": "tate_ex", "Perfect Tate": "perfect_tate", "Mean": "mean", "Mean \(Human\)": "mean_human", "Ges": "ges", "blanknam3d": "blank", "Midge": "midge", "Elizabeth": "eliza", "Anne": "anne", "Grace": "grace", "K-22": "k22", "K-17": "k17", "Addy": "addy" }

                                        for h in hide_these:
                                            if hide_these[h] not in persistent.seen and re.fullmatch(h, subcategory):
                                                $ sub_text = obfuscator(subcategory)

                                        # Print the subcategory
                                        frame:
                                            background None
                                            xsize 900
                                            text sub_text:
                                                xalign 0.0
                                                size 48
                                                font "impact.ttf"
                                                text_align 0

                                        # Get contributors
                                        vbox:
                                            xalign 1.0
                                            for contributor in CREDITS_MAP[route][category][subcategory]:

                                                # manually hide CS 3D and Digi if unseen
                                                if (persistent.defeated_perfect_tate == False and category == "CS-ocola (3D Sprite)") or ("digi" not in persistent.seen and category == "DigiDuncan Character Sprite"):
                                                    $ contributor = obfuscator(contributor)

                                                text "{font=music_text}"+contributor: # handler for CJK text in contributor names
                                                    xalign 1.0 yalign 0.5
                                                    text_align 1.0

                                # Music requires special handling
                                # Use the pre-sorted list from earlier, hide unseen tracks
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
                                                    text_align 0

                                            vbox:
                                                xalign 1.0
                                                xsize 600
                                                text "{font=music_text}"+artist_displayed:
                                                    xalign 1.0 yalign 0.5
                                                    text_align 1.0
                            # For game logo
                            elif category == "_logo":
                                vbox:
                                    xsize 1600
                                    vbox:
                                        xsize 1600
                                        image CREDITS_MAP[route][category][subcategory][0]:
                                            xalign 0.5
                                            yalign 0.5

                            # For cast
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

                                    # Only print names if they've been seen
                                    python:
                                        hide_these = { "4Bakers": ["iris"], "AFuckingChicken": ["hoh_worker"], "Annorexorcist": ["anno"], "Arceus3251": ["arceus"], "Aria \"Estroteric\"": ["aria"], "blanknam3d": ["blank"], "BubbleTheSlime": ["bubble"], "db05": ["db"], "DigiDuncan": ["digi"], "EddieJustEddie": ["hoh_worker"], "Ges \"DefinitelyNotGes\"": ["ges"], "Guithais": ["hoh_worker"], "ItsNovaHere": ["nova"], "meancarnavor": ["mean", "mean_human"], "Midgalicis": ["midge"], "Mikapara": ["mika", "eliza", "grace", "anne"], "Pakoopara": ["pakoo", "addy", "k17", "k22"], "Tate \"alleZSoyez\"": ["tate"], "UndeadKitty": ["kitty"] }

                                        char_text = ""

                                    # No matter how tempting, do NOT put this in a python block.
                                    for c in CREDITS_MAP[route][category][subcategory]:
                                        if c in hide_these:
                                            for c_linked in hide_these[c]:
                                                if any(character in c_linked for character in persistent.seen):
                                                    $ char_text = c
                                                else:
                                                    $ char_text = obfuscator(c)
                                        else:
                                            $ char_text = c

                                        text char_text:
                                            xalign 0.5 yalign 0.5

                            # For special thanks
                            elif category == "Special Thanks":
                                vbox:
                                    xsize 1600

                                    $ thanks_text = subcategory
                                    $ thanks_for_text = CREDITS_MAP[route][category][subcategory][0]

                                    # print the thanks + text under it
                                    vbox:
                                        xsize 1600
                                        text thanks_text:
                                            xalign 0.5
                                            size 48
                                            font "impact.ttf"
                                        text thanks_for_text+"\n":
                                            xalign 0.5 yalign 0.5

            # DPN logo
            frame:
                background None
                ysize 500
            image "gui/credits/dpn_logo.png":
                xalign 0.5 yalign 1.0
            text "DPN Games":
                yoffset -128
                size 96
                xalign 0.5
            text "MMXXIV":
                yoffset -128
                size 96
                xalign 0.5

    # Actually move the frame
    $ credits_frame_size = get_size(credits_frame)
    $ print(credits_frame_size)
    add credits_frame:
        at transform:
            yanchor scroll_start 
            linear duration yanchor credits_frame_size[1]-1080

    if renpy.context_nesting_level() != 0:
        dismiss action Play("music", "bubble_tea.ogg", loop = False), Jump("start")
    else:
        dismiss action [ Stop("music"), Return() ]