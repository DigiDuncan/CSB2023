screen unused_gallery():

    $ persistent.heard.add("what_the_night_will_bring")

    tag menu
    add "images/bg/books_misc/michael_calendar.png"
    add Color("#00000070")

    python:
        file = renpy.file("data/gallery.json")
        asset_dict_preload = json.load(file)

        # begin anti-spoiler technology
        # some things will be unlocked by default but most will require a character, label, ending, or some combination of these.
        asset_dict = {}

        for item in asset_dict_preload:
            requirements_met = True
            # character
            if "need_character" in asset_dict_preload[item] and asset_dict_preload[item]["need_character"] not in persistent.seen:
                requirements_met = False
            # ending
            if "need_ending" in asset_dict_preload[item] and asset_dict_preload[item]["need_ending"] not in persistent.seen_all_endings:
                requirements_met = False
            # label
            if "need_label" in asset_dict_preload[item] and renpy.seen_label(asset_dict_preload[item]["need_label"]) == False:
                requirements_met = False

            if requirements_met:
                asset_dict[item] = asset_dict_preload[item]

        ## fix counter if it goes over the length of list or under 1
        pretty_count = unused_page+1

        # Filename
        filename = list(asset_dict.keys())[unused_page]
        entry = list(asset_dict.values())[unused_page]

    text list( str(pretty_count)+" of "+str(len(asset_dict)) ):
        size 48
        xalign 0.5
        yalign 0.07

    # File Name
    text entry["title"]:
        size 72
        xalign 0.5
        yalign 0.125

    # Caption
    text entry["caption"]:
        textalign 0.5
        xcenter 0.7
        ycenter 0.6
        xsize 600
        ysize 800

    # Main Image (if image)
    if entry["type"] == "image":
        image ProportionalScale("gallery/images/" + filename, 500, 800):
            xcenter 0.3
            ycenter 0.6

    # Unused Route Handling
    if entry["type"] == "route":
        image ProportionalScale("gallery/images/" + filename, 500, 800):
            xcenter 0.3
            ycenter 0.6
        frame:
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos 0.415
            textbutton "{color=#fff}Click To Play!{/color}":
                action Replay(str(entry["jump_to"]), locked = False), Stop("music2"), PauseAudio("music", False), Stop("jukebox"), SetVariable("unused_page", 0)

    # Main Image (if audio)
    if entry["type"] == "audio":
        image ProportionalScale("gallery/album_art/" + entry["album_art"], 500, 800):
            xcenter 0.3
            ycenter 0.6

    # Main Image (if image set)
    if entry["type"] == "imgset":

        python:
            img_list = []
            for img in entry["imgs"]:
                img_list.append( "gallery/images/" + img)

        image ProportionalScale(img_list[current_gallery_img], 500, 800):
            xcenter 0.3
            ycenter 0.6

        frame:
            background None
            xsize 0.3 ysize 0.1
            xcenter 0.3 ycenter 0.9

            # box for left arrow
            frame:
                background None
                xysize 64, 64
                xalign 0 yalign 0.5

                if current_gallery_img-1>=0:
                    imagebutton:
                        xalign 0.5 yalign 0.5
                        xysize 64, 64
                        idle "/gui/left_off_small.png"
                        hover "/gui/left_on_small.png"
                        action IncrementVariable("current_gallery_img", -1)

            frame:
                background None
                xalign 0.5 yalign 0.5
                text entry["imgs"][current_gallery_img]:
                    xalign 0.5 yalign 0.5
                    text_align 0.5

            # right arrow
            frame:
                background None
                xysize 64, 64
                xalign 1.0 yalign 0.5

                if current_gallery_img+1 < len(entry["imgs"]):
                    imagebutton:
                        xalign 1.0 yalign 0.5
                        xysize 64, 64
                        idle "/gui/right_off_small.png"
                        hover "/gui/right_on_small.png"
                        action IncrementVariable("current_gallery_img", 1)

    # Return Button
    textbutton "{color=#fff}Return{/color}":
        action ShowMenu("category_welcome"), Stop("music2"), PauseAudio("music", False), Stop("jukebox"), SetVariable("unused_page", 0)
        xalign 0.02
        yalign 0.04
        background "#5F777F"

    # Right Button
    if unused_page+1<len(list(asset_dict.keys())):
        imagebutton idle "gui/right_off.png" hover "gui/right_on.png":
            if list(asset_dict.values())[unused_page+1]["type"] == "audio":
                action [
                    PauseAudio("music2"),
                    Play("jukebox", "gallery/audio/" + list(asset_dict.keys())[unused_page+1], loop = False),
                    SetVariable("unused_page", unused_page+1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page+1]["type"] == "image":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page+1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page+1]["type"] == "route":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page+1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page+1]["type"] == "route2":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page+1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page+1]["type"] == "imgset":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page+1),
                    SetVariable("current_gallery_img", 0)
                ]
            xalign 0.9 yalign 0.1

    # Left Button
    if unused_page>0:
        imagebutton idle "gui/left_off.png" hover "gui/left_on.png":
            if list(asset_dict.values())[unused_page-1]["type"] == "audio":
                action [
                    PauseAudio("music2"),
                    Play("jukebox", "gallery/audio/" + list(asset_dict.keys())[unused_page-1], loop = False),
                    SetVariable("unused_page", unused_page-1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page-1]["type"] == "image":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page-1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page-1]["type"] == "route":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page-1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page-1]["type"] == "route2":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page-1),
                    SetVariable("current_gallery_img", 0)
                ]
            elif list(asset_dict.values())[unused_page-1]["type"] == "imgset":
                action [
                    PauseAudio("music2", False),
                    Stop("jukebox"),
                    SetVariable("unused_page", unused_page-1)
                ]
            xalign 0.1 yalign 0.1

