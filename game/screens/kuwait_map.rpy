screen kuwait_map():
    add "gui/kuwait_map/map_kuwait.png"
    textbutton _("Return"):
        action MainMenu(confirm=False), Stop("jukebox"), PauseAudio("music", False)
        text_color "#FFFFFF"
        text_outlines [(4.5, "#000000", absolute(0), absolute(0))]
        xalign 0.02
        yalign 0.04
        background "#DEA25E"

    vbox:
        xalign 0.5
        viewport:
            xysize(1080, 1080)
            style_prefix "choice"
            $ tt = GetTooltip() or "Select area to travel:"
            text tt:
                xalign 0.5
                text_align 0.5
                color "#FFFFFF"
                outlines [(4.5, "#000000", absolute(0), absolute(0))]


            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(570,650)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kuwait_city")
                tooltip _("Kuwait City")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(560,600)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sharq")
                tooltip _("Sharq")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(460,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_hawally")
                tooltip _("Hawally")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(580,830)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_bayan_water_towers")
                tooltip _("Bayan Water Towers")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(670,790)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_salmiya")
                tooltip _("Salmiya")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(730,980)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_khiran_camp")
                tooltip _("Khiran Camp")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(560,1020)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_wafra")
                tooltip _("Al Wafra")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(310,620)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_jahra_industrial")
                tooltip _("Jahra Industrial")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(270,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_sulaibiya")
                tooltip _("Sulaibiya")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(820,520)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_icarus")
                tooltip _("Icarus")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(860,240)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_boubyan_island")
                tooltip _("Boubyan Island")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(920,760)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_namil")
                tooltip _("Um Al Namil")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(850,860)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_kubar_island")
                tooltip _("Kubar Island")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(920,940)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_um_al_maradim")
                tooltip _("Um Al Maradim")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(160,540)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_burgan_oil_fields")
                tooltip _("Burgan Oil Fields")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(140,140)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_saqr_airbase")
                tooltip _("Saqr Airbase")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(380,180)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_al_abdally")
                tooltip _("Al-Abdally")

            imagebutton:
                idle "gui/kuwait_map/map_marker.png"
                hover "gui/kuwait_map/map_marker_current.png"
                hover_sound "audio/sfx/sfx_select.ogg"
                at transform:
                    zoom 0.5
                    pos(460,270)
                action Play("sound", "audio/sfx/sfx_valid.ogg"), Hide("dx_select"), Jump("kuwait_mutla_ridge")
                tooltip _("Mutla Ridge")
