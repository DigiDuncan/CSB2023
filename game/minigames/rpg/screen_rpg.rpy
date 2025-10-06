init python:
    Fighter1 = Fighters.get("ARCEUS")
    Fighter2 = Fighters.get("KITTY")
    Fighter3 = Fighters.get("DIGI")
    Fighter4 = Fighters.get("MEAN")
    CurrentTurn = 1
    pass

screen screen_rpg():
    # This is the main view of the RPG battle.
    frame:
        yalign 1.0
        xalign 0.5
        padding(0,0)
        background None
        has vbox
        spacing 3
        box_reverse True
        # The Fight box
        frame:
            padding(5,5)
            xysize(1916, 262)
            background "gui/rpg/main_box.png"
        grid 4 1:
            xfill True

        # Fighter 1
            if Fighter1 and not Fighter1.dead:
                frame:
                    padding(7,7)
                    xalign 0.5
                    yalign 1.0
                    xsize 475
                    # If it's the fighter's turn
                    if CurrentTurn == 1:
                        ysize 201
                        background "gui/rpg/tall_box.png"
                    # Otherwise
                    else:
                        background "gui/rpg/small_box.png"
                        ysize 105
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
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(Fighter1.health_points/Fighter1.max_health))),0) corner2(228,32) xalign 1.0
                            text str(Fighter1.health_points)+"/"+str(Fighter1.max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 1:
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

        #Fighter 2
            if Fighter2 and not Fighter2.dead:
                frame:
                    padding(7,7)
                    xalign 0.5
                    yalign 1.0
                    xsize 475
                    # If it's the fighter's turn
                    if CurrentTurn == 2:
                        ysize 201
                        background "gui/rpg/tall_box.png"
                    # Otherwise
                    else:
                        background "gui/rpg/small_box.png"
                        ysize 105
                    has grid 2 2
                    xfill True
                    yfill True

                    # The Fighter's Icon and Stats
                    hbox:
                        align(0.0, 0.0)
                        ysize 88
                        spacing 2
                        # Icon
                        if Fighter2.sprite:
                            add Fighter2.sprite
                        else:
                            add "gui/rpg/portraits/unknown.png"
                        # Stats
                        grid 2 2:
                            yalign 0.5
                            xspacing 2
                            add "gui/rpg/attack.png" yalign 0.5
                            text str(Fighter2.attack_points):
                                size 32
                                yalign 0.5
                            add "gui/rpg/defense.png" yalign 0.5
                            text str(Fighter2.armor_points):
                                size 32
                                yalign 0.5

                    # The Fighter's name and healthbar        
                    vbox:
                        align(1.0, 0.0)
                        text Fighter2.display_name:
                            xalign 1.0
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(Fighter2.health_points/Fighter2.max_health))),0) corner2(228,32) xalign 1.0
                            text str(Fighter2.health_points)+"/"+str(Fighter2.max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 2:
                        # The attack button
                        imagebutton:
                            align(0.0, 1.0)
                            idle "gui/rpg/attack_button.png"
                            action Notify("Attack pressed on fighter 2!")

                        # The defend button
                        imagebutton:
                            align(1.0, 1.0)
                            idle "gui/rpg/defend_button.png"
                            action Notify("Defend pressed on fighter 2!")

        # Fighter 3
            if Fighter3 and not Fighter3.dead:
                frame:
                    padding(7,7)
                    xalign 0.5
                    yalign 1.0
                    xsize 475
                    # If it's the fighter's turn
                    if CurrentTurn == 3:
                        ysize 201
                        background "gui/rpg/tall_box.png"
                    # Otherwise
                    else:
                        background "gui/rpg/small_box.png"
                        ysize 105
                    has grid 2 2
                    xfill True
                    yfill True
        
                    # The Fighter's Icon and Stats
                    hbox:
                        align(0.0, 0.0)
                        ysize 88
                        spacing 2
                        # Icon
                        if Fighter3.sprite:
                            add Fighter3.sprite
                        else:
                            add "gui/rpg/portraits/unknown.png"
                        # Stats
                        grid 2 2:
                            yalign 0.5
                            xspacing 2
                            add "gui/rpg/attack.png" yalign 0.5
                            text str(Fighter3.attack_points):
                                size 32
                                yalign 0.5
                            add "gui/rpg/defense.png" yalign 0.5
                            text str(Fighter3.armor_points):
                                size 32
                                yalign 0.5
        
                    # The Fighter's name and healthbar        
                    vbox:
                        align(1.0, 0.0)
                        text Fighter3.display_name:
                            xalign 1.0
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(Fighter3.health_points/Fighter3.max_health))),0) corner2(228,32) xalign 1.0
                            text str(Fighter3.health_points)+"/"+str(Fighter3.max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 3:
                        # The attack button
                        imagebutton:
                            align(0.0, 1.0)
                            idle "gui/rpg/attack_button.png"
                            action Notify("Attack pressed on fighter 3!")

                        # The defend button
                        imagebutton:
                            align(1.0, 1.0)
                            idle "gui/rpg/defend_button.png"
                            action Notify("Defend pressed on fighter 3!")

        # Fighter 4
            if Fighter4 and not Fighter4.dead:
                frame:
                    padding(7,7)
                    xalign 0.5
                    yalign 1.0
                    xsize 475
                    # If it's the fighter's turn
                    if CurrentTurn == 4:
                        ysize 201
                        background "gui/rpg/tall_box.png"
                    # Otherwise
                    else:
                        background "gui/rpg/small_box.png"
                        ysize 105
                    has grid 2 2
                    xfill True
                    yfill True
        
                    # The Fighter's Icon and Stats
                    hbox:
                        align(0.0, 0.0)
                        ysize 88
                        spacing 2
                        # Icon
                        if Fighter4.sprite:
                            add Fighter4.sprite
                        else:
                            add "gui/rpg/portraits/unknown.png"
                        # Stats
                        grid 2 2:
                            yalign 0.5
                            xspacing 2
                            add "gui/rpg/attack.png" yalign 0.5
                            text str(Fighter4.attack_points):
                                size 32
                                yalign 0.5
                            add "gui/rpg/defense.png" yalign 0.5
                            text str(Fighter4.armor_points):
                                size 32
                                yalign 0.5
        
                    # The Fighter's name and healthbar        
                    vbox:
                        align(1.0, 0.0)
                        text Fighter4.display_name:
                            xalign 1.0
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(Fighter4.health_points/Fighter4.max_health))),0) corner2(228,32) xalign 1.0
                            text str(Fighter4.health_points)+"/"+str(Fighter4.max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 4:
                        # The attack button
                        imagebutton:
                            align(0.0, 1.0)
                            idle "gui/rpg/attack_button.png"
                            action Notify("Attack pressed on fighter 4!")

                        # The defend button
                        imagebutton:
                            align(1.0, 1.0)
                            idle "gui/rpg/defend_button.png"
                            action Notify("Defend pressed on fighter 4!")

    # Dev Backdoor
    key "K_END" action Return(True)
    key "K_i" action IncrementVariable("CurrentTurn")
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
