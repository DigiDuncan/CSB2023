style start_window is empty

screen chapter_menu():
    zorder 100
    style_prefix "start"
    window id "start_window" xalign 0.5 yalign 0.5:
        vbox xalign 0.5 yalign 0.5:
            spacing 50
            text "Start where?" textalign 0.5 size 72 xalign 0.5 yalign 0.5
            hbox xalign 0.5 yalign 0.5:
                spacing 50
                imagebutton auto "menu/csbi_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbi_start")
                imagebutton auto "menu/csbii_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.csb2_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbii_start")
                imagebutton auto "menu/csbiii1_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.csb3a_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbiii_start")
                imagebutton auto "menu/csbiii2_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.csb3b_unlocked
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu", Fade(1.0)), Jump("csbiii_choose_direction")
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                    sensitive persistent.true_ending
                    at transform:
                        zoom 0.666
                    action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("chapter_menu"), Jump("dx_start")
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25
