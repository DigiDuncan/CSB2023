screen dx_select():

    default tt = Tooltip("Or something else?")

    textbutton "{color=#fff}Back{/color}":
        action Jump("chapter_select"), Stop("jukebox"), PauseAudio("music", False)
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
                imagebutton auto "menu/dx/speedrun_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Speedrun")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("vibration")

                ### KUWAIT ###
                imagebutton auto "menu/dx/kuwait_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Kuwait")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_travel")

                ### BRONSON ###
                imagebutton auto "menu/dx/bronson_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
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
                imagebutton auto "menu/dx/train_winner_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Train (Winner)")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("train_start_good")

                ### TRAIN (THIEF) ###
                imagebutton auto "menu/dx/train_thief_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Train (Thief)")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("train_start_bad")

                ### CHRISTMAS ###
                imagebutton auto "menu/dx/christmas_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Christmas")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("ce_start")

                ### BEACH EPISODE ###
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    hovered tt.Action("Beach Episode")
                    at transform:
                        zoom 0.333
                        xalign 0.5
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("beach_start")

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5

                imagebutton auto "menu/csbiiidx_%s.png":
                    at transform:
                        zoom 0.333
                        xalign 0.5
