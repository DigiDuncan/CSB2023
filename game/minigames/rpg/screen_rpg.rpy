"""
TODO list
- Add the possibility of a fighter being confused.
- Rescale the attack text based on the number of attacks
- Recolor the attack text
- Add functionality to the attack text
- Depending on the action selected add the action to a list (To pass back to the back end)
"""

init python:
    CombatAllies = [Fighters.get("ARCEUS"), Fighters.get("KITTY"), Fighters.get("DIGI"), Fighters.get("MEAN")]
    CurrentTurn = 0
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
            padding(91, 5)
            xysize(1916, 262)
            background "gui/rpg/main_box.png"
            vbox:
                yalign 0.5
                for i in range(len(CombatAllies[CurrentTurn].attacks)):
                    # If the attack is not available, make this insensitive
                    button:
                        action NullAction()
                        has vbox
                        text "{size=42}"+CombatAllies[CurrentTurn].attacks[i].name+" {/size}{size=21}("+CombatAllies[CurrentTurn].attacks[i].properties+"){/size}":
                            color "#FFFFFF"
                            hover_color "#00B7EC"
                        text "{size=21}"+CombatAllies[CurrentTurn].attacks[i].description+"{/size}":
                            first_indent 32
                            color "#848484"
                            hover_color "#006582"
                    #textbutton "{color=#FFFFFF}{size=42}"+CombatAllies[CurrentTurn].attacks[i].name+" {size=21}("+CombatAllies[CurrentTurn].attacks[i].properties+")\n{color=#848484}"+CombatAllies[CurrentTurn].attacks[i].description:
                        #text_rest_indent 32
        grid 4 1:
            xfill True

        # Fighter 1
            if CombatAllies[0] and not CombatAllies[0].dead:
                frame:
                    padding(7,7)
                    xalign 0.5
                    yalign 1.0
                    xsize 475
                    # If it's the fighter's turn
                    if CurrentTurn == 0:
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
                        if CombatAllies[0].sprite:
                            add CombatAllies[0].sprite
                        else:
                            add "gui/rpg/portraits/unknown.png"
                        # Stats
                        grid 2 2:
                            yalign 0.5
                            xspacing 2
                            add "gui/rpg/attack.png" yalign 0.5
                            text str(CombatAllies[0].attack_points):
                                size 32
                                yalign 0.5
                            add "gui/rpg/defense.png" yalign 0.5
                            text str(CombatAllies[0].armor_points):
                                size 32
                                yalign 0.5
        
                    # The Fighter's name and healthbar        
                    vbox:
                        align(1.0, 0.0)
                        text CombatAllies[0].display_name:
                            xalign 1.0
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(CombatAllies[0].health_points/CombatAllies[0].max_health))),0) corner2(228,32) xalign 1.0
                            text str(CombatAllies[0].health_points)+"/"+str(CombatAllies[0].max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 0:
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
            if CombatAllies[1] and not CombatAllies[1].dead:
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
                        if CombatAllies[1].sprite:
                            add CombatAllies[1].sprite
                        else:
                            add "gui/rpg/portraits/unknown.png"
                        # Stats
                        grid 2 2:
                            yalign 0.5
                            xspacing 2
                            add "gui/rpg/attack.png" yalign 0.5
                            text str(CombatAllies[1].attack_points):
                                size 32
                                yalign 0.5
                            add "gui/rpg/defense.png" yalign 0.5
                            text str(CombatAllies[1].armor_points):
                                size 32
                                yalign 0.5

                    # The Fighter's name and healthbar        
                    vbox:
                        align(1.0, 0.0)
                        text CombatAllies[1].display_name:
                            xalign 1.0
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(CombatAllies[1].health_points/CombatAllies[1].max_health))),0) corner2(228,32) xalign 1.0
                            text str(CombatAllies[1].health_points)+"/"+str(CombatAllies[1].max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 1:
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
            if CombatAllies[2] and not CombatAllies[2].dead:
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
                        if CombatAllies[2].sprite:
                            add CombatAllies[2].sprite
                        else:
                            add "gui/rpg/portraits/unknown.png"
                        # Stats
                        grid 2 2:
                            yalign 0.5
                            xspacing 2
                            add "gui/rpg/attack.png" yalign 0.5
                            text str(CombatAllies[2].attack_points):
                                size 32
                                yalign 0.5
                            add "gui/rpg/defense.png" yalign 0.5
                            text str(CombatAllies[2].armor_points):
                                size 32
                                yalign 0.5
        
                    # The Fighter's name and healthbar        
                    vbox:
                        align(1.0, 0.0)
                        text CombatAllies[2].display_name:
                            xalign 1.0
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(CombatAllies[2].health_points/CombatAllies[2].max_health))),0) corner2(228,32) xalign 1.0
                            text str(CombatAllies[2].health_points)+"/"+str(CombatAllies[2].max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 2:
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
            if CombatAllies[3] and not CombatAllies[3].dead:
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
                        if CombatAllies[3].sprite:
                            add CombatAllies[3].sprite
                        else:
                            add "gui/rpg/portraits/unknown.png"
                        # Stats
                        grid 2 2:
                            yalign 0.5
                            xspacing 2
                            add "gui/rpg/attack.png" yalign 0.5
                            text str(CombatAllies[3].attack_points):
                                size 32
                                yalign 0.5
                            add "gui/rpg/defense.png" yalign 0.5
                            text str(CombatAllies[3].armor_points):
                                size 32
                                yalign 0.5
        
                    # The Fighter's name and healthbar        
                    vbox:
                        align(1.0, 0.0)
                        text CombatAllies[3].display_name:
                            xalign 1.0
                        frame:
                            background None
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0
                            yalign 1.0
                            add "gui/rpg/hp_bar.png" corner1(int(228-(228*(CombatAllies[3].health_points/CombatAllies[3].max_health))),0) corner2(228,32) xalign 1.0
                            text str(CombatAllies[3].health_points)+"/"+str(CombatAllies[3].max_health)+" HP":
                                xalign 1.0
                                yalign 0.5

                    if CurrentTurn == 3:
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
