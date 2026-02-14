# This is for viewing the various outcomes in Christmas Edition.
screen d20_viewer_screen():
    tag menu

    add "gui/game_menu.png"
    
    text "{size=+48}D20 Viewer":
        xalign 0.5
        yalign 0.1
        text_align 0.5

    text "See what fate could have been...\n{size=-12}{color=#BBBBBB}(Or, more accurately, see who would have arrived at the Christmas party first.)":
        xalign 0.5
        yalign 0.19
        text_align 0.5

    image "gui/d20.png":
        xalign 0.5
        yalign 0.6

    # decrease roll
    if d20 > 0:
        imagebutton:
            idle "gui/left_off.png" 
            hover "gui/left_on.png"
            action IncrementVariable("d20", amount=-1), Show("d20_viewer_screen", None)
            xalign 0.3
            yalign 0.55

    # increase roll
    if d20 < 21:
        imagebutton:
            idle "gui/right_off.png"
            hover "gui/right_on.png"
            action IncrementVariable("d20"), Show("d20_viewer_screen")
            xalign 0.7
            yalign 0.55

    text "{color=#FF6A00}"+str(d20):
        xalign 0.5
        yalign 0.55
        size 288

    textbutton "{size=69}View" action Replay("ce_party_before", scope={"d20":d20}):
        xalign 0.5
        yalign 0.9

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
