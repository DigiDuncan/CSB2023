init python:
    Fighter1 = Fighters.get("MEAN")
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
            if Fighter1.sprite:
                add Fighter1.sprite
            else:
                add "gui/rpg/portraits/unknown.png"
            # Stats
            grid 2 2:
                yalign 0.5
                xspacing 2
                add "gui/rpg/attack.png" yalign 0.5
                text str(Fighter1.attack_points):
                    size 32
                    yalign 0.5
                add "gui/rpg/defense.png" yalign 0.5
                text str(Fighter1.armor_points):
                    size 32
                    yalign 0.5

        # The Fighter's name and healthbar        
        vbox:
            align(1.0, 0.0)
            text Fighter1.display_name:
                xalign 1.0
            # TODO: Figure out how to make a healthbar for the background.
            text str(Fighter1.health_points)+"/"+str(Fighter1.max_health)+" HP":
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
    hide arceus
    hide cs
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
