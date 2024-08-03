screen unused_gallery(i):
    tag menu
    add Color('#323e42', alpha=0.75)

    python:
        file = renpy.file("gallery/captions.json")
        asset_dict = json.load(file)

    # Left Button
    imagebutton idle "gui/left_off.png" hover "gui/left_on.png":
        action ShowMenu("unused_gallery", i-1)
        yalign 0.5
        xalign 0.1

    # Right Button
    imagebutton idle "gui/right_off.png" hover "gui/right_on.png":
        action ShowMenu("unused_gallery", i+1)
        yalign 0.5
        xalign 0.9

    # Return Button
    textbutton "{color=#fff}Return{/color}":
        action Return(), Stop("jukebox"), PauseAudio("music", False)
        xalign 0.02
        yalign 0.04
        background "#5F777F"

    # File Name
    text list(asset_dict.values())[i % len(asset_dict)]["title"]:
        xalign 0.5
        yalign 0.04
    
    # Caption
    text list(asset_dict.values())[i % len(asset_dict)]["caption"]:
        textalign 0.5
        xalign 0.5
        yalign 0.95
        xsize 1500

    # Main Image
    image ProportionalScale("gallery/images/" + list(asset_dict.keys())[i % len(asset_dict)], 750, 750):
        xalign(0.5)
        yalign(0.5)