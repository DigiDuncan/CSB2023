screen kuwait_map():
    textbutton _("{color=#fff}Return{/color}"):
        action MainMenu(confirm=False), Stop("jukebox"), PauseAudio("music", False)
        xalign 0.02
        yalign 0.04
        background "#DEA25E"
    vbox:
        xalign 0.5
        viewport:
            xysize(1080, 1080)
            style_prefix "choice"
            $ tt = GetTooltip() or "Select area to travel:"
            text tt xpos(450)
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(570,650)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kuwait_city")
                tooltip _("Kuwait City")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(560,600)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sharq")
                tooltip _("Sharq")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(460,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_hawally")
                tooltip _("Hawally")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(580,830)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_bayan_water_towers")
                tooltip _("Bayan Water Towers")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(670,790)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_salmiya")
                tooltip _("Salmiya")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(730,980)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_khiran_camp")
                tooltip _("Khiran Camp")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(560,1020)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_wafra")
                tooltip _("Al Wafra")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(310,620)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_jahra_industrial")
                tooltip _("Jahra Industrial")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(270,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sulaibiya")
                tooltip _("Sulaibiya")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(820,520)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_icarus")
                tooltip _("Icarus")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(860,240)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_boubyan_island")
                tooltip _("Boubyan Island")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(920,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_namil")
                tooltip _("Um Al Namil")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(850,860)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kubar_island")
                tooltip _("Kubar Island")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(920,940)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_maradim")
                tooltip _("Um Al Maradim")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(160,540)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_burgan_oil_fields")
                tooltip _("Burgan Oil Fields")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(140,140)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_saqr_airbase")
                tooltip _("Saqr Airbase")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(380,180)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_abdally")
                tooltip _("Al-Abdally")
            imagebutton auto "menu/csbiiidx_%s.png" hover_sound "audio/sfx/sfx_select.ogg":
                at transform:
                    zoom 0.1
                    pos(460,270)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_mutla_ridge")
                tooltip _("Mutla Ridge")
