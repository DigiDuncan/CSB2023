screen unused_gallery():

    tag menu
    add "images/bg/michael_calendar.png"
    add Color("#00000070")

    python:
        file = renpy.file("gallery/captions.json")
        asset_dict = json.load(file)

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
        action Return(), Stop("music2"), PauseAudio("music", False), Stop("jukebox")
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