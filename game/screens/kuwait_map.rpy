screen kuwait_map():
    default tt = Tooltip("Select area to travel:")
    textbutton "{color=#fff}Return{/color}":
        action MainMenu(confirm=False), Stop("jukebox"), PauseAudio("music", False)
        xalign 0.02
        yalign 0.04
        background "#DEA25E"
    vbox:
        xalign 0.5
        viewport:
            xysize(1080, 1080)
            style_prefix "choice"
            text tt.value xpos(450)
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Kuwait City")
                at transform:
                    zoom 0.1
                    pos(570,650)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kuwait_city")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Sharq")
                at transform:
                    zoom 0.1
                    pos(560,600)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sharq")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Hawally")
                at transform:
                    zoom 0.1
                    pos(460,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_hawally")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Bayan Water Towers")
                at transform:
                    zoom 0.1
                    pos(580,830)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_bayan_water_towers")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Salmiya")
                at transform:
                    zoom 0.1
                    pos(670,790)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_salmiya")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Khiran Camp")
                at transform:
                    zoom 0.1
                    pos(730,980)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_khiran_camp")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Al Wafra")
                at transform:
                    zoom 0.1
                    pos(560,1020)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_wafra")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Jahra Industrial")
                at transform:
                    zoom 0.1
                    pos(310,620)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_jahra_industrial")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Sulaibiya")
                at transform:
                    zoom 0.1
                    pos(270,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sulaibiya")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Icarus")
                at transform:
                    zoom 0.1
                    pos(820,520)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_icarus")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Boubyan Island")
                at transform:
                    zoom 0.1
                    pos(860,240)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_boubyan_island")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Um Al Namil")
                at transform:
                    zoom 0.1
                    pos(920,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_namil")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Kubar Island")
                at transform:
                    zoom 0.1
                    pos(850,860)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kubar_island")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Um Al Maradim")
                at transform:
                    zoom 0.1
                    pos(920,940)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_maradim")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Burgan Oil Fields")
                at transform:
                    zoom 0.1
                    pos(160,540)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_burgan_oil_fields")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Saqr Airbase")
                at transform:
                    zoom 0.1
                    pos(140,140)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_saqr_airbase")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Al-Abdally")
                at transform:
                    zoom 0.1
                    pos(380,180)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_abdally")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                hovered tt.Action("Mutla Ridge")
                at transform:
                    zoom 0.1
                    pos(460,270)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_mutla_ridge")
