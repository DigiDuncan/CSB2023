## Replay Gallery screen ######################################
## Take care when making changes to this file #################

screen Replayexit():
    zorder 100
    imagebutton auto "images/replay/exit_%s.png" action EndReplay() yalign .99 xalign .99
            #yes AUTO create 2 images titled exit_hover.png and exit_idle.png
#add these 2 line below if you want an exit button during the replay(optional)
#this must be added after every label used for replay
#if _in_replay:
#        show screen Replayexit

screen replay_gallery():

    tag menu
    add Color('#5F777F', alpha=0.5)

    $start = replay_page * 9
    $end = min(start + 9 - 1, len(Replay_items) - 1)

    #grid for images
    grid 3 3:
        xfill True
        yfill True

        for i in range(start, end + 1):
            if renpy.seen_label(Replay_items[i].replay):
                imagebutton idle Replay_items[i].thumbs:
                    action Replay(Replay_items[i].replay)
                    xalign 0.5
                    yalign 0.5
            else:
                vbox xalign 0.5 yalign 0.5:
                    #locked image, we might change this to be blurred or some shit
                    image Replay_items[i].thumbs:
                        blur 70
                    #image "lockedthumb" #if you're using the gallery use the same image (optional)
        #required to fill in empty grid items (do not change)
        for i in range(end - start + 1, 9):
            null

    #grid for info
    grid 3 3:
        xfill True
        yfill True
        for i in range(start, end + 1):
            if renpy.seen_label(Replay_items[i].replay):
                hbox:
                    spacing maxthumbx - 20
                    xalign 0.5
                    yalign 0.1
                    text Replay_items[i].name:
                        outlines [(absolute(10), "#000", absolute(0), absolute(0))]
            else:
                null
        #required to fill in empty grid items (do not change)
        for i in range(end - start + 1, 9):
            null

    #previous/next buttons
    if replay_page > 0:
        textbutton "{color=#fff}Previous{/color}":
            action SetVariable("replay_page", replay_page - 1)
            xalign 0.1
            yalign 0.98
            background "#5F777F"
    if (replay_page + 1) * 9 < len(Replay_items):
        textbutton "{color=#fff}Next{/color}":
            action SetVariable("replay_page", replay_page + 1)
            xalign 0.9
            yalign 0.98
            background "#5F777F"
    #return button
    textbutton "{color=#fff}Return{/color}":
        action Return()
        xalign 0.5
        yalign 0.98
        background "#5F777F"
