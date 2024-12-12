# This is for viewing the various outcomes in Christmas Edition.
screen ce_minigame_screen():
    tag menu

    add "gui/game_menu.png"
    
    text "{size=+48}Minigames":
        xalign 0.5
        ypos 0.1 yanchor 0.5
        text_align 0.5

    text "Go back and play your favorite games from Christmas Edition!":
        xalign 0.5
        ypos 0.15 yanchor 0.5
        text_align 0.5

    if persistent.carrot_game_unlocked:
        imagebutton idle "carrot_box.png":
            action Jump("play_ce_carrot")
            yalign 0.5
            xpos 0.33 xanchor 0.5
    else:
        image "carrot_box.png":
            blur 70
            yalign 0.5
            xpos 0.33 xanchor 0.5

    if persistent.reversi_game_unlocked:
        imagebutton idle "reversi_box.png":
            action Jump("play_ce_reversi")
            yalign 0.5
            xpos 0.67 xanchor 0.5
    else:
        image "reversi_box.png":
            blur 70
            yalign 0.5
            xpos 0.67 xanchor 0.5
    

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25