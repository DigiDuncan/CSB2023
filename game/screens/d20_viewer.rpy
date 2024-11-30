# this is for viewing the various outcomes in Christmas Edition.

$ global current_roll

screen d20_viewer_screen(dice_roll):
    tag menu

    if dice_roll is None:
        $ rolled = 0
        $ current_roll = 0
    else:
        $ rolled = dice_roll
        $ current_roll = dice_roll
    
    # add background color
    add Color('#323e42', alpha=0.75)
    
    text "{size=+36}D20 Viewer\n{/size}{size=+12}See what fate could have been...\n{size=-24}{color=#BBBBBB}(Or, more accurately, who would have arrived to the Christmas party first.)":
        xalign 0.5
        yalign 0.1
        text_align 0.5

    image "gui/d20.png":
        xalign 0.5
        yalign 0.6

    text "{color=#FF6A00}"+str(current_roll):
        xalign 0.5
        yalign 0.55
        size 288

    # decrease roll
    if current_roll > -1:
        imagebutton:
            idle "gui/left_off.png" 
            hover "gui/left_on.png"
            action SetScreenVariable("current_roll", current_roll-1)
            xalign 0.3
            yalign 0.55

    # increase roll
    if current_roll < 20:
        imagebutton:
            idle "gui/right_off.png"
            hover "gui/right_on.png"
            action SetScreenVariable("current_roll", current_roll+1)
            xalign 0.7
            yalign 0.55

    textbutton "{size=69}View" action Notify("Digi needs to get this working!"):
        xalign 0.5
        yalign 0.9

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
