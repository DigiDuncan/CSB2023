# This is for viewing the various outcomes in Christmas Edition.
screen ce_minigame_screen():
    tag menu

    python:
        if renpy.music.get_playing(channel='music') != "christmas_tea.ogg":
            pass
        elif renpy.music.get_playing(channel='music') != "<from 14.7>christmas_tea.ogg":
            pass
        else:
            renpy.music.play("<from 14.7>christmas_tea.ogg", channel="music", loop=False)

    add "gui/game_menu.png"
    
    text "{size=+48}Minigames":
        xalign 0.5
        ypos 0.1 yanchor 0.5
        text_align 0.5

    text "Go back and play your favorite games from Christmas Edition!":
        xalign 0.5
        ypos 0.17 yanchor 0.5
        text_align 0.5

    if persistent.carrot_game_unlocked:
        imagebutton idle "images/minigames/carrot_box.png":
            action Replay("play_ce_carrot", locked = False)
            yalign 0.55
            xpos 0.33 xanchor 0.5
    else:
        image "images/minigames/carrot_box.png":
            blur 70
            yalign 0.55
            xpos 0.33 xanchor 0.5

    if persistent.reversi_game_unlocked:
        imagebutton idle "images/minigames/reversi_box.png":
            action Replay("play_ce_reversi", locked = False)
            yalign 0.55
            xpos 0.67 xanchor 0.5
    else:
        image "images/minigames/reversi_box.png":
            blur 70
            yalign 0.55
            xpos 0.67 xanchor 0.5
    

    textbutton "Return to Extras" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
