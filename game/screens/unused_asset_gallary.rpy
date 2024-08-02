screen unused_nav():
    $ current_index = 0

    add Color('#5F777F', alpha=0.5)

    # Left Button
    imagebutton idle "gui/left_off.png" hover "gui/left_on.png":
        action SetLocalVariable("current_index", current_index - 1), ShowMenu("unused_gallery", current_index)
        yalign 0.5
        xalign 0.1

    # Right Button
    imagebutton idle "gui/right_off.png" hover "gui/right_on.png":
        action SetLocalVariable("current_index", current_index + 1), ShowMenu("unused_gallery", current_index)
        yalign 0.5
        xalign 0.9

    # Return Button
    textbutton "{color=#fff}Return{/color}":
        action Return(), Stop("jukebox"), PauseAudio("music", False)
        xalign 0.02
        yalign 0.04
        background "#5F777F"

screen unused_gallery(i):
    tag menu
    use unused_nav

    python:
        file = renpy.file("gallery/captions.json")
        asset_dict = json.load(file)

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