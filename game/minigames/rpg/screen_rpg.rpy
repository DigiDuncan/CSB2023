init python:
    # Functions python will probably need later on in the code.
    pass

screen screen_rpg():
    # This is the main view of the RPG battle.
    # Fighter 1
    # TODO: Replace with if fighter is alive
    frame:
        padding(7,7)
        xalign 0.5
        yalign 0.5
        xsize 475
        # If it's the fighter's turn
        ysize 201
        background "gui/rpg/tall_box.png"
        # Otherwise
        # background "gui/rpg/small_box.png"
        has grid 2 2
        xfill True
        yfill True

        # The Fighter's Icon and Stats
        hbox:
            align(0.0, 0.0)
            ysize 88
            spacing 2
            # Icon
            add "gui/rpg/portraits/arceus.png" # TODO: Programatically obtain fighter icon
            # Stats
            grid 2 2:
                yalign 0.5
                xspacing 2
                add "gui/rpg/attack.png" yalign 0.5
                text "35" size 32 yalign 0.5 # TODO: Programatically obtain fighter attack stat
                add "gui/rpg/defense.png" yalign 0.5
                text "15" size 32 yalign 0.5# TODO: Programatically obtain fighter defense stat

        # The Fighter's name and healthbar        
        vbox:
            align(1.0, 0.0)
            text "Arceus": # TODO: Programatically obtain fighter name
                xalign 1.0
            # TODO: Figure out how to make a healthbar for the background.
            text "160/160 HP": # TODO: Programatically obtain the fighter current health and max health
                xalign 1.0

        # The attack button
        imagebutton:
            align(0.0, 1.0)
            idle "gui/rpg/attack_button.png"
            action Notify("Attack pressed on fighter 1!")
        
        # The defend button
        imagebutton:
            align(1.0, 1.0)
            idle "gui/rpg/defend_button.png"
            action Notify("Defend pressed on fighter 1!")

    # Dev Backdoor
    key "K_END" action Return(True)
    pass

label play_screenrpnggame:
    window hide
    $ quick_menu = False
    call screen screen_rpg
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label screenrpg_done:
    pass
