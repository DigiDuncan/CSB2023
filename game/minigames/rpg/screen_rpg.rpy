"""
TODO list
- Add the possibility of a fighter being confused.
- Rescale the attack text based on the number of attacks
- Add functionality to the attack text
- Depending on the action selected add the action to a list (To pass back to the back end)
"""

python early:
    def bypass_append(renpy_list, element):
        renpy_list.append(element)

init:
    transform _rpg_intro:
        on show:
            xanchor 0.5 xpos 0.5
            yanchor 0.5 ypos 0.05
            alpha 0.00
            ease_cubic 0.5 alpha 1.00
            time 2.5
            ease_expo 1 alpha 0.00

screen screen_rpg():
    grid len(RPG.encounter.enemies) 1:
        xalign 0.5
        yalign 0.5
        for i in range(len(RPG.encounter.enemies)):
            add RPG.encounter.enemies[i].sprite

    # Show intro text above the enemies
    frame at _rpg_intro:
        text RPG.encounter.intro_text

    # This is the context menu of the RPG
    frame:
        yalign 1.0
        xalign 0.5
        padding(0,0)
        background None
        has vbox
        spacing 3
        box_reverse True
        # The Attack Selection Box:
        frame:
            padding(80, 5)
            xysize(1916, 262)
            background "gui/rpg/main_box.png"
            grid 2 1:
                xfill True
                yfill True
                # The attacks.
                vbox:
                    yalign 0.5
                    if RPG.encounter.turn < len(RPG.encounter.allies):
                        for i in range(len(RPG.encounter.allies[RPG.encounter.turn].attacks)):
                            # If the attack is not available, make this insensitive
                            $ attack_actions = []
                            $ attack_actions.append(Function(RPG.encounter.allies[RPG.encounter.turn].set_next_attack, RPG.encounter.allies[RPG.encounter.turn].attacks[i]))
                            if (RPG.encounter.turn+1 != len(RPG.encounter.allies)) and (RPG.encounter.allies[RPG.encounter.turn].attacks[i].attack.target_count == 0):
                                $ attack_actions.append(IncrementVariable("RPG.encounter.turn"))
                            button:
                                action attack_actions
                                if not RPG.encounter.allies[RPG.encounter.turn].attacks[i].available:
                                    sensitive False
                                has vbox
                                text "{size=42}"+RPG.encounter.allies[RPG.encounter.turn].attacks[i].name+" {/size}{size=21}("+RPG.encounter.allies[RPG.encounter.turn].attacks[i].attack.description+"){/size}":
                                    if RPG.encounter.allies[RPG.encounter.turn].attacks[i] is RPG.encounter.allies[RPG.encounter.turn].next_attack:
                                        color "#FFCC00"
                                    else:
                                        color "#FFFFFF"
                                    hover_color "#00B7EC"
                                text "{size=21}"+RPG.encounter.allies[RPG.encounter.turn].attacks[i].attack.description+"{/size}":
                                    first_indent 32
                                    if RPG.encounter.allies[RPG.encounter.turn].attacks[i] is RPG.encounter.allies[RPG.encounter.turn].next_attack:
                                        color "#844200"
                                    else:
                                        color "#848484"
                                    hover_color "#006582"

                # The target select box
                vbox:
                    $ curr_att = RPG.encounter.allies[RPG.encounter.turn].next_attack
                    if curr_att is not None:
                        $ victims = RPG.encounter.possible_targets(RPG.encounter.allies[RPG.encounter.turn], RPG.encounter.allies[RPG.encounter.turn].next_attack.attack)
                        $ working_list = []
                        for i in range(curr_att.attack.target_count):
                            text "{size=42}Select target [i]"
                            for victim in victims:
                                $ target_actions = [Function(bypass_append, working_list, victim)]
                                if i+1 == curr_att.attack.target_count:
                                    $ target_actions.append(Function(RPG.encounter.allies[RPG.encounter.turn].set_next_targets, working_list))
                                    if (RPG.encounter.turn+1 != len(RPG.encounter.allies)):
                                        $ target_actions.append(IncrementVariable("RPG.encounter.turn"))
                                button:
                                    action target_actions
                                    text "{size=42}"+victim.display_name:
                                        color "#FFFFFF"
                                        hover_color "#00B7EC"
                            if not i == 0:
                                button:
                                    text "{size=42}Back":
                                        color "#FFFFFF"
                                        hover_color "#00B7EC"
                                    action RemoveFromSet("working_list", working_list[i-1]), IncrementVariable("i", -1)

            # If everything is set and good to go, show the confirm button)
            # TODO: Further checks to make sure everything is good and valid.
            if all(f.next_attack is not None for f in RPG.encounter.allies):
                imagebutton:
                    xalign 1.0
                    yalign 1.0
                    idle "gui/rpg/confirm_button.png"
                    action Function(RPG.encounter.run_attacks)
        # The stat boxes for Allies
        grid len(RPG.encounter.allies) 1:
            xfill True
            for i in range(len(RPG.encounter.allies)):
                if not RPG.encounter.allies[i].dead:
                    button:
                        padding(7,7)
                        xalign 0.5
                        yalign 1.0
                        xsize 475
                        # If it's the fighter's turn
                        if RPG.encounter.turn == i:
                            ysize 201
                            background "gui/rpg/tall_box.png"
                        # Otherwise
                        else:
                            background "gui/rpg/small_box.png"
                            ysize 105
                            action SetVariable("RPG.encounter.turn", i)
                        has grid 2 2
                        xfill True
                        yfill True
                        # The Fighter's Icon and Stats
                        hbox:
                            align(0.0, 0.0)
                            ysize 88
                            spacing 2
                            # Icon
                            if RPG.encounter.allies[i].character.portrait:
                                add RPG.encounter.allies[i].character.portrait
                            else:
                                add "gui/rpg/portraits/unknown.png"
                            # Stats
                            grid 2 2:
                                yalign 0.5
                                xspacing 2
                                add "gui/rpg/attack.png" yalign 0.5
                                text str(RPG.encounter.allies[i].attack):
                                    size 32
                                    yalign 0.5
                                add "gui/rpg/defense.png" yalign 0.5
                                text str(RPG.encounter.allies[i].defense):
                                    size 32
                                    yalign 0.5
                        # The Fighter's name and healthbar
                        vbox:
                            align(1.0, 0.0)
                            hbox:
                                xalign 1.0
                                # if encounter.allies[i].confused:
                                    # add "gui/rpg/confusion_status.png"
                                text RPG.encounter.allies[i].character.display_name:
                                    xalign 1.0
                            frame:
                                background None
                                padding(0,0)
                                xysize(228, 32)
                                xalign 1.0
                                yalign 1.0
                                add "gui/rpg/hp_bar.png" corner1(int(228-(228*(RPG.encounter.allies[i].hit_points/RPG.encounter.allies[i].max_hp))),0) corner2(228,32) xalign 1.0
                                text str(RPG.encounter.allies[i].hit_points)+"/"+str(RPG.encounter.allies[i].max_hp):
                                    xalign 1.0
                                    yalign 0.5
                                add "gui/rpg/hp.png" yalign 0.5 xalign -0.15
                        if RPG.encounter.turn == i:
                            # The attack button
                            imagebutton:
                                align(0.0, 1.0)
                                idle "gui/rpg/attack_button.png"
                                action Notify("Attack pressed on fighter"+str(i+1)+"!")
                            # The defend button
                            imagebutton:
                                align(1.0, 1.0)
                                idle "gui/rpg/defend_button.png"
                                action Notify("Defend pressed on fighter"+str(i+1)+"!")


    # Dev Backdoor
    key "K_END" action Return(True)
    pass

label play_rpggame:
    window hide
    $ quick_menu = False
    show image RPG.encounter.background
    $ renpy.music.play(MUSIC_MAP[RPG.encounter.music]["file"])
    $ persistent.heard.add(str(RPG.encounter.music))
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
