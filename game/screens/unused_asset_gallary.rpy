screen unused_gallery(i):
    $ renpy.music.play("gallery/what_the_night_will_bring.mp3", channel='music2', relative_volume=8.0)
    $ renpy.music.set_pause(True, channel = "music")
    tag menu
    add Color('#323e42', alpha=0.75)

    python:
        file = renpy.file("gallery/captions.json")
        asset_dict = json.load(file)

    # Left Button
    imagebutton idle "gui/left_off.png" hover "gui/left_on.png":
        action ShowMenu("unused_gallery", i-1)
        yalign 0.1
        xalign 0.1

    # Right Button
    imagebutton idle "gui/right_off.png" hover "gui/right_on.png":
        action ShowMenu("unused_gallery", i+1)
        yalign 0.1
        xalign 0.9

    # Counter
    python:
        ## fix counter if it goes over the length of list or under 1
        pretty_count = (i % len(asset_dict)) + 1

    text list( str(pretty_count)+" of "+str(len(asset_dict)) ):
        size 48
        xalign 0.5
        yalign 0.07
        
    # File Name
    text list(asset_dict.values())[i % len(asset_dict)]["title"]:
        size 72
        xalign 0.5
        yalign 0.125
    
    # Caption
    text list(asset_dict.values())[i % len(asset_dict)]["caption"]:
        textalign 0.5
        xcenter 0.7
        ycenter 0.6
        xsize 600
        ysize 800

    # Main Image (if image)
    if list(asset_dict.values())[i%len(asset_dict)]["type"] == "image":
        $ renpy.music.set_pause(False, channel = "music2")
        $ renpy.music.stop(channel='jukebox')
        image ProportionalScale("gallery/images/" + list(asset_dict.keys())[i % len(asset_dict)], 500, 800):
            xcenter 0.3
            ycenter 0.6

    # Main Image (if audio)
    else:
        $ renpy.music.set_pause(True, channel = "music2")
        $ renpy.music.play(list(asset_dict.values())[i % len(asset_dict)]["title"], "jukebox")

    # Return Button
    textbutton "{color=#fff}Return{/color}":
        action Stop("jukebox"), Stop("music2"), PauseAudio("music", False), Return()
        xalign 0.02
        yalign 0.04
        background "#5F777F"