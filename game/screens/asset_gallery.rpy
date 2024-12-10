screen unused_gallery():

    $ persistent.heard.add("what_the_night_will_bring")

    tag menu
    add "images/bg/michael_calendar.png"
    add Color("#00000070")

    python:
        file = renpy.file("data/gallery.json")
        asset_dict_preload = json.load(file)

        # begin anti-spoiler technology
        # some things will be unlocked by default but most will require a character, label, ending, or some combination of these.
        asset_dict = {}

        for item in asset_dict_preload:
            # character
            if "need_character" in asset_dict_preload[item] and asset_dict_preload[item]["need_character"] in persistent.seen:
                asset_dict[item] = asset_dict_preload[item]
            # ending
            if "need_ending" in asset_dict_preload[item] and asset_dict_preload[item]["need_ending"] in persistent.seen_all_endings:
                asset_dict[item] = asset_dict_preload[item]
            # label
            if "need_label" in asset_dict_preload[item] and renpy.seen_label(asset_dict_preload[item]["need_label"]) == True:
                asset_dict[item] = asset_dict_preload[item]
            # unlocked by default
            if "need_character" not in asset_dict_preload[item] and "need_ending" not in asset_dict_preload[item] and "need_label" not in asset_dict_preload[item]:
                asset_dict[item] = asset_dict_preload[item]

    # Counter
    python:
        ## fix counter if it goes over the length of list or under 1
        pretty_count = unused_page+1

    text list( str(pretty_count)+" of "+str(len(asset_dict)) ):
        size 48
        xalign 0.5
        yalign 0.07
        
    # File Name
    text list(asset_dict.values())[unused_page]["title"]:
        size 72
        xalign 0.5
        yalign 0.125
    
    # Caption
    text list(asset_dict.values())[unused_page]["caption"]:
        textalign 0.5
        xcenter 0.7
        ycenter 0.6
        xsize 600
        ysize 800

    # Main Image (if image)
    if list(asset_dict.values())[unused_page]["type"] == "image":
        image ProportionalScale("gallery/images/" + list(asset_dict.keys())[unused_page], 500, 800):
            xcenter 0.3
            ycenter 0.6

    # Main Image (if audio)
    if list(asset_dict.values())[unused_page]["type"] == "audio":
        image ProportionalScale("gallery/album_art/" + list(asset_dict.values())[unused_page]["album_art"], 500, 800):
            xcenter 0.3
            ycenter 0.6

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
                action PauseAudio("music2"), Play("jukebox", "gallery/audio/" + list(asset_dict.keys())[unused_page+1], loop = False), SetVariable("unused_page", unused_page+1)
            elif list(asset_dict.values())[unused_page+1]["type"] == "image":
                action PauseAudio("music2", False), Stop("jukebox"), SetVariable("unused_page", unused_page+1)
            yalign 0.1
            xalign 0.9

    # Left Button
    if unused_page>0:
        imagebutton idle "gui/left_off.png" hover "gui/left_on.png":
            if list(asset_dict.values())[unused_page-1]["type"] == "audio":
                action PauseAudio("music2"), Play("jukebox", "gallery/audio/" + list(asset_dict.keys())[unused_page-1], loop = False), SetVariable("unused_page", unused_page-1)
            elif list(asset_dict.values())[unused_page-1]["type"] == "image":
                action PauseAudio("music2", False), Stop("jukebox"), SetVariable("unused_page", unused_page-1)
            yalign 0.1
            xalign 0.1
