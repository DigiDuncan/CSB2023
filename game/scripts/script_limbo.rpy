########## Minigame Jumps ##########

label play_ce_carrot:
    minigame "play_carrotgame" "play_ce_done" "play_ce_done"
    $ renpy.end_replay()
    return

label play_ce_reversi:
    scene game_menu
    menu:
        "Who would you like to play against?"
        "Tate (Beginner)":
            $ reversi_difficulty = ReversiAI.TATE
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
        "Digi (Easy)":
            $ reversi_difficulty = ReversiAI.DIGI
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
        "K-22 (Medium)":
            $ reversi_difficulty = ReversiAI.PAKOO
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
        "Arceus (Hard)":
            $ reversi_difficulty = ReversiAI.ARCEUS
            minigame "play_reversigame" "play_ce_done" "play_ce_done"
        "Aria (Expert)":
            $ reversi_difficulty = ReversiAI.ARIA
            minigame "play_reversigame" "play_ce_done" "play_ce_done"

label play_ce_done:
    $ renpy.end_replay()
    return

########## Special Screens ##########

label show_dxcom:
    $ commentary_manager.play(current_dxcom)
    return

label woohoo_counter:
    play music interference2
    $ persistent.heard.add("interference2")
    scene conferencetv
    show cs at left
    show arceus festive at right
    with dissolve
    arceus "Well, boss, let's see how many \"woohoos\" you got!"
    scene conferencetv at Move((0.0 , -1.0), (0.0, 0.0), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show cs at Move((0.0 , 0.25), (0.0, 1.75), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    show arceus festive at Move((0.735 , 0.4), (0.735, 1.75), 3, repeat=False, bounce=False, xanchor="left", yanchor="top")
    pause 3.0
    show screen woohoo_counter
    play sound sfx_fabeep
    arceus "Wow, that's [persistent.woohoo] woohoos!"
    arceus "Err... that's now [persistent.woohoo]. My bad."
    play sound sfx_woohoo
    pause 1.5
    $ persistent.woohoo += 1
    play sound sfx_fabeep
    pause 0.5
    cs "Now, it's [persistent.woohoo]!"
    return

screen hatch_button():
    modal True

    ##### poster button
    imagebutton:
        auto "gui/ce_point_click/poster/poster_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(720, 323, 0)
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.poster")

    ##### rug button
    imagebutton:
        auto "gui/ce_point_click/rug/rug_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(961, 56, 0)
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.rug")

    ##### cs button
    imagebutton:
        idle "images/characters/cs/christmas/disappointed.png"
        hover "gui/ce_point_click/cs_hover.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at mid_left
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.cs")

    ##### flashlight button
    imagebutton:
        auto "gui/ce_point_click/flashlight/flashlight_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at manual_pos(0.3, 0.7, 0.5)

        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.flashlight")

    ##### mean button
    imagebutton:
        idle "images/characters/mean/meanhumanannoyedfestive.png"
        hover "gui/ce_point_click/mean_hover.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        at mid_right
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_point_click.mean")

    ##### hatch button (correct one)
    imagebutton:
        auto "gui/ce_point_click/hatch/hatch_%s.png"
        hover_sound "audio/sfx/sfx_select.ogg"
        xpos 0.3
        ypos -0.2
        action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("hatch_button"), Jump("ce_after_hatch")

    add Flashlight()
