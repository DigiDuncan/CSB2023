screen unused_gallery():
    tag menu
    add Color('#5F777F', alpha=0.5)
    $ current_index = 0

    python:
        file = renpy.file("gallery/captions.json")
        asset_dict = json.load(file)

    # Left Button

    # Right Button

    # Return Button
    textbutton "{color=#fff}Return{/color}":
        action Return()
        xalign 0.02
        yalign 0.04
        background "#5F777F"

    # File Name
    text list(asset_dict.values())[current_index%len(asset_dict)]["title"]:
        xalign 0.5
        yalign 0.04
    
    # Caption
    text list(asset_dict.values())[current_index%len(asset_dict)]["caption"]:
        textalign 0.5
        xalign 0.5
        yalign 0.75

    # Main Image