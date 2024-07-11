screen dx_select(items):
    vbox:
        xalign 0.5
        viewport:
            xysize(950, 540)
            xalign 0.75
            ypos 0.1
            style_prefix "choice"
            vbox:
                xalign 0.5
                spacing 20
                text "Play the After Story?" xalign 0.5 textalign 0.5
                imagebutton auto "menu/csbiiidx_%s.png" hover_sound "sfx_select.ogg":
                    at transform:
                        zoom 0.666
                        xalign 0.5
                    action Play("sound", "sfx_valid.ogg"), Hide("dx_select"), Jump("after_true")
                text "Or something else?" xalign 0.5 textalign 0.5
        viewport:
            xysize(1920, 540)
            yanchor -0.25
            xoffset -0.1
            style_prefix "choice"
            side_yfill True
            scrollbars "vertical"
            mousewheel True
            vbox:
                for i in items:
                    textbutton i.caption:
                        anchor(-0.25, -0.25)
                        action i.action

label lose_car_game:
    bad_end "100 percent\nunsatisfied." "iowa"
    return

label lose_pencil_game:
    bad_end "Try, uh, mashing... faster?" "minigame_pencil"
    return

label lose_pencil_game2:
    bad_end "You dumb skinfore." "minigame_pencil2"
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

label pussy_out_archival:
    $ persistent.seen.add("k174")
    $ persistent.seen.add("addy")
    $ persistent.heard.add("Facing Worlds - Michiel van den Bos")
    $ persistent.heard.add("BATTLE UNDER A BROKEN SKY - AZALI")
    $ persistent.heard.add("Take a Trip from Me - u4ia")
    $ persistent.heard.add("Everybody Wants To Rule The World - Tears For Fears")
    $ achievement_manager.unlock("Archived")
    return

label pussy_out_i69:
    $ persistent.seen.add("gnome")
    $ persistent.heard.add("Wayward Wanderer - Deep Gnome")
    $ persistent.heard.add("MisLeader - Triosk and Jan Jelinek")
    $ persistent.heard.add("Dense Woods B - Kikiyama")
    $ persistent.heard.add("Melancholy - Imori")
    $ achievement_manager.unlock("You've Been Gnomed")
    $ achievement_manager.unlock("Analog Horror Protagonist")
    jump interstate_94

label dx_start:
    python:
        destinations = {
            "Craptop": "csbi_craptop",
            "Kuwait": "airport_choose",
            "Train": None
        }
        
        place_to_go = renpy.display_menu([(k, v) for k, v in destinations.items()], screen="dx_select")
        renpy.jump(place_to_go)