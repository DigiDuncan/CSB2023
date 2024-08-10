screen dx_select():
    
    default tt = Tooltip("Or something else?")

    textbutton "{color=#fff}Return{/color}":
        action MainMenu(confirm=False), Stop("jukebox"), PauseAudio("music", False)
        xalign 0.02
        yalign 0.04
        background "#5F777F"

    vbox:
        xalign 0.5
        viewport:
            xysize(950, 550)
            xalign 0.75
            ypos 0.1
            style_prefix "choice"
            vbox:
                xalign 0.5
                spacing 20
                text "Play the After Story?" xalign 0.5 textalign 0.5
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    at transform:
                        zoom 0.666
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("dx_after_true")
                text tt.value xalign 0.5 textalign 0.5
        viewport:
            xysize(1920, 600)
            yanchor -0.025
            xoffset -0.1
            grid 5 2:
                xfill True
                yfill True
                # We can have 10 entries here
            
                ### SPEEDRUN ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Speedrun")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("vibration")

                ### KUWAIT ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Kuwait")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_travel")

                ### BRONSON ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Bronson")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("michigan_bronson")

                ### ROCKSTAR II ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Rockstar II")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("rockstar_start")

                ### TRAIN (WINNER) ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Train (Winner)")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("train_start_good")

                ### TRAIN (THIEF) ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Train (Thief)")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("train_start_bad")

                ### RESERVED ###
                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

label lose_car_game:
    bad_end "100 percent\nunsatisfied." "true_iowa"
    return

label lose_pencil_game:
    bad_end "Try, uh, mashing... faster?" "minigame_pencil"
    return

label lose_pencil_game2:
    bad_end "You dumb skinfore." "play_pencil2_game"
    return

label play_edit_game:
    minigame "minigame_editing" "minigame_editing" "minigame_editing"
    return

label play_car_game:
    minigame "minigame_car" "minigame_car" "minigame_car"
    return

label play_pencil_game:
    minigame "minigame_pencil" "minigame_pencil" "minigame_pencil"
    return

label play_slots_game:
    minigame "minigame_slots" "minigame_slots" "minigame_slots"
    return

label show_dxcom:
    $ commentary_manager.play(current_dxcom)
    return

label back_out_archival:
    $ persistent.seen.add("k174")
    $ persistent.seen.add("addy")
    $ persistent.heard.add("Facing Worlds - Michiel van den Bos")
    $ persistent.heard.add("BATTLE UNDER A BROKEN SKY - AZALI")
    $ persistent.heard.add("Take a Trip from Me - u4ia")
    $ persistent.heard.add("Everybody Wants To Rule The World - Tears For Fears")
    $ achievement_manager.unlock("Archived")
    return

label back_out_i69:
    $ persistent.seen.add("gnome")
    $ persistent.heard.add("Wayward Wanderer - Deep Gnome")
    $ persistent.heard.add("MisLeader - Triosk and Jan Jelinek")
    $ persistent.heard.add("Dense Woods B - Kikiyama")
    $ persistent.heard.add("Melancholy - Imori")
    $ achievement_manager.unlock("You've Been Gnomed")
    $ achievement_manager.unlock("Analog Horror Protagonist")
    jump michigan_interstate_94

label dx_start:
    call screen dx_select
