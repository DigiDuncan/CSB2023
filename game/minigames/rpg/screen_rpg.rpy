"""
TODO list
- Properly implement status icons; account for longer character names + multiple effects
- Rescale the attack text based on the number of attacks
- Add functionality to the attack text
- Depending on the action selected add the action to a list (To pass back to the back end)
- Make the little heart icon actually move down with the HP counter bar
- Remove enemies from target select if they are dead
- Make target select use icons?
- Make sprites be positioned dynamically based on number of enemies - bigger crowds should mean a tighter squeeze!
- Don't let anyone go completely offscreen!
- Fix the smaller sprites such as the K-types that are getting Mike Wazowski'd
"""

python early:
    def bypass_append(renpy_list, element):
        renpy_list.append(element)
    def print_action(print_str):
        print(print_str)
    def dev_win(current_encounter):
        current_encounter.dev_win()

init python:
    renpy.add_layer("rpg_context", above="master")
    renpy.add_layer("rpg_say", above="rpg_context")

init:
    transform _rpg_intro:
        on show:
            xanchor 0.5 xpos 0.5
            yanchor 0.5 ypos 0.05
            alpha 0.00
            ease_cubic 0.5 alpha 1.00
            time 2.5
            ease_expo 1 alpha 0.00

screen say_rpg(rpg_what):
    modal True

    frame:
        xalign 0.0
        yalign 0.0
        xsize 1.0
        ysize 0.10
        background "gui/rpg/main_box.png"
        button:
            text rpg_what

screen screen_rpg():
    # Drawing the enemies in the background.
    grid len(RPG.encounter.enemies) 1:
        xalign 0.5
        yalign 1.0
        for i in range(len(RPG.encounter.enemies)):
            if not RPG.encounter.enemies[i].dead:
                # Attempt to add animated sprite if one exists, else fallback to the normal sprite
                python:
                    try:
                        enemy_sprite = RPG.encounter.enemies[i].anim_sprite
                    except:
                        enemy_sprite = RPG.encounter.enemies[i].sprite

                add enemy_sprite
            else:
                add Null(200,200)

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
                                hover_sound "audio/sfx/sfx_select.ogg"
                                action [
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    attack_actions
                                ]
                                if not RPG.encounter.allies[RPG.encounter.turn].attacks[i].available:
                                    sensitive False
                                has vbox
                                text "{size=42}"+RPG.encounter.allies[RPG.encounter.turn].attacks[i].name+" {/size}{size=21}("+RPG.encounter.allies[RPG.encounter.turn].attacks[i].attack.properties+"){/size}":
                                    if RPG.encounter.allies[RPG.encounter.turn].attacks[i] is RPG.encounter.allies[RPG.encounter.turn].next_attack:
                                        color "#FF8A00"
                                        hover_color "#F5DD00"
                                        insensitive_color "#888888"
                                    else:
                                        color "#FFFFFF"
                                        hover_color "#0099CC"
                                        insensitive_color "#888888"
                                text "{size=21}"+RPG.encounter.allies[RPG.encounter.turn].attacks[i].attack.description+"{/size}":
                                    first_indent 32
                                    if RPG.encounter.allies[RPG.encounter.turn].attacks[i] is RPG.encounter.allies[RPG.encounter.turn].next_attack:
                                        color "#844200"
                                        hover_color "#7B6F00"
                                        insensitive_color "#888888"
                                    else:
                                        color "#848484"
                                        hover_color "#006582"
                                        insensitive_color "#888888"

                # The target select box
                vbox:
                    $ curr_att = RPG.encounter.allies[RPG.encounter.turn].next_attack
                    if curr_att is not None:
                        $ victims = RPG.encounter.possible_targets(RPG.encounter.allies[RPG.encounter.turn], RPG.encounter.allies[RPG.encounter.turn].next_attack.attack)
                        $ working_list = []
                        for i in range(curr_att.attack.target_count):
                            text "{size=42}Select target [i]"
                            for victim in victims:
                                $ target_actions = [ Function(bypass_append, working_list, victim) ]
                                if i+1 == curr_att.attack.target_count:
                                    $ target_actions.append(Function(RPG.encounter.allies[RPG.encounter.turn].set_next_targets, working_list))
                                    if (RPG.encounter.turn+1 != len(RPG.encounter.allies)):
                                        $ target_actions.append(IncrementVariable("RPG.encounter.turn"))
                                button:
                                    hover_sound "audio/sfx/sfx_select.ogg"
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        target_actions
                                    ]
                                    text "{size=42}"+victim.display_name:
                                        color "#FFFFFF"
                                        hover_color "#0099CC"
                            if not i == 0:
                                button:
                                    hover_sound "audio/sfx/sfx_select.ogg"
                                    text "{size=42}Back":
                                        color "#FFFFFF"
                                        hover_color "#0099CC"
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        RemoveFromSet("working_list", working_list[i-1]),
                                        IncrementVariable("i", -1)
                                    ]

            # If everything is set and good to go, show the confirm button)
            # TODO: Further checks to make sure everything is good and valid.
            if all(f.next_attack is not None for f in RPG.encounter.allies):
                imagebutton:
                    xalign 1.0
                    yalign 1.0
                    idle "gui/rpg/confirm_button.png"
                    hover "selectable:gui/rpg/confirm_button.png"
                    hover_sound "audio/sfx/sfx_select.ogg"
                    action [
                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                        Return()
                    ]
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

                        # Status effects
                        if len(RPG.encounter.allies[i].effects) > 0:
                            # Count up all the effects
                            python:
                                checked_effects = {}
                                for effect in RPG.encounter.allies[i].effects:
                                    if effect.effect not in checked_effects:
                                        checked_effects[effect.effect] = 1
                                    else:
                                        checked_effects[effect.effect] += 1
                            frame:
                                xanchor 1.0
                                xpos 1.0 ypos -60
                                hbox:
                                    for effect in checked_effects:
                                        frame:
                                            xysize(36,36)
                                            background effect.icon
                                            if checked_effects[effect] > 1:
                                                text str(checked_effects[effect]):
                                                    size 16
                                                    xanchor 1.0 yanchor 0.0
                                                    xoffset 32 yoffset -11
                                                    text_align 1.0
                                                    color Color("#FFFFFF")
                                                    outlines [(2.5, "#000000", absolute(0), absolute(0))]
                        grid 2 2:
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
                                    text RPG.encounter.allies[i].character.display_name:
                                        xalign 1.0
                                frame:
                                    background None
                                    padding(0,0)
                                    xysize(228, 32)
                                    xalign 1.0
                                    yalign 1.0
                                    if not RPG.encounter.allies[i].infinite:
                                        add "gui/rpg/hp_bar.png" corner1(int(228-(228*(RPG.encounter.allies[i].hit_points/RPG.encounter.allies[i].max_hp))),0) corner2(228,32) xalign 1.0
                                        text str(RPG.encounter.allies[i].hit_points)+"/"+str(RPG.encounter.allies[i].max_hp):
                                            xalign 1.0 yalign 0.5
                                    else:
                                        add "gui/rpg/hp_bar_inf.png" corner1(0,0) corner2(228,32) xalign 1.0
                                        add "gui/rpg/infinite.png" xalign 1.0 yalign 0.5
                                    add "gui/rpg/hp.png" yalign 0.5 xalign -0.15
                            if RPG.encounter.turn == i:
                                # The attack button
                                imagebutton:
                                    align(0.0, 1.0)
                                    idle "gui/rpg/attack_button.png"
                                    hover "selectable:gui/rpg/attack_button.png"
                                    hover_sound "audio/sfx/sfx_select.ogg"
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        Notify("Attack pressed on fighter"+str(i+1)+"!")
                                    ]
                                # The defend button
                                imagebutton:
                                    align(1.0, 1.0)
                                    idle "gui/rpg/defend_button.png"
                                    hover "selectable:gui/rpg/defend_button.png"
                                    hover_sound "audio/sfx/sfx_select.ogg"
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        Notify("Defend pressed on fighter"+str(i+1)+"!")
                                    ]
                # Don't just collapse the space if ally has been knocked out
                else:
                    add Null(489,88):
                        xalign 0.5 yalign 1.0


        # Enemy stat boxes
        grid len(RPG.encounter.enemies) 1:
            xfill True
            for i in range(len(RPG.encounter.enemies)):
                if not RPG.encounter.enemies[i].dead:
                    frame:
                        padding(7,7)
                        xalign 0.5 yalign 0.5
                        yoffset -500
                        xsize 475 ysize 105
                        background "gui/rpg/small_box.png"

                        # Status effects
                        if len(RPG.encounter.enemies[i].effects) > 0:
                            # Count up all the effects
                            python:
                                checked_effects = {}
                                for effect in RPG.encounter.enemies[i].effects:
                                    if effect.effect not in checked_effects:
                                        checked_effects[effect.effect] = 1
                                    else:
                                        checked_effects[effect.effect] += 1
                            frame:
                                xanchor 1.0
                                xpos 1.0 ypos 103
                                hbox:
                                    for effect in checked_effects:
                                        frame:
                                            xysize(36,36)
                                            background effect.icon
                                            if checked_effects[effect] > 1:
                                                text str(checked_effects[effect]):
                                                    size 16
                                                    xanchor 1.0 yanchor 0.0
                                                    xoffset 32 yoffset -11
                                                    text_align 1.0
                                                    color Color("#FFFFFF")
                                                    outlines [(2.5, "#000000", absolute(0), absolute(0))]
                        grid 2 2:
                            xfill True
                            yfill True
                            # The Fighter's Icon and Stats
                            hbox:
                                align(0.0, 0.0)
                                ysize 88
                                spacing 2
                                # Icon
                                if RPG.encounter.enemies[i].character.portrait:
                                    add RPG.encounter.enemies[i].character.portrait
                                else:
                                    add "gui/rpg/portraits/unknown.png"
                                # Stats
                                grid 2 2:
                                    yalign 0.5
                                    xspacing 2
                                    add "gui/rpg/attack.png" yalign 0.5
                                    text str(RPG.encounter.enemies[i].attack):
                                        size 32
                                        yalign 0.5
                                    add "gui/rpg/defense.png" yalign 0.5
                                    text str(RPG.encounter.enemies[i].defense):
                                        size 32
                                        yalign 0.5
                            # The Fighter's name and healthbar
                            vbox:
                                align(1.0, 0.0)
                                hbox:
                                    xalign 1.0
                                    text RPG.encounter.enemies[i].character.display_name:
                                        xalign 1.0
                                frame:
                                    background None
                                    padding(0,0)
                                    xysize(228, 32)
                                    xalign 1.0
                                    yalign 1.0
                                    if not RPG.encounter.enemies[i].infinite:
                                        add "gui/rpg/hp_bar.png" corner1(int(228-(228*(RPG.encounter.enemies[i].hit_points/RPG.encounter.enemies[i].max_hp))),0) corner2(228,32) xalign 1.0
                                        text str(RPG.encounter.enemies[i].hit_points)+"/"+str(RPG.encounter.enemies[i].max_hp):
                                            xalign 1.0 yalign 0.5
                                    else:
                                        add "gui/rpg/hp_bar_inf.png" corner1(0,0) corner2(228,32) xalign 1.0
                                        add "gui/rpg/infinite.png" xalign 1.0 yalign 0.5
                                    add "gui/rpg/hp.png" yalign 0.5 xalign -0.15

                # Don't just collapse the space if enemy has been knocked out
                else:
                    add Null(489,88):
                        xalign 0.5 yalign 1.0

    # Dev Backdoor
    key "K_END" action Jump("pass_rpg")

label play_rpggame:
    window hide
    $ quick_menu = False
    show image RPG.encounter.background
    $ renpy.music.play(MUSIC_MAP[RPG.encounter.music]["file"])
    $ persistent.heard.add(str(RPG.encounter.music))
    # This is where the game actually takes place.
    while RPG.encounter.won is None:
        call screen screen_rpg
        $ RPG.encounter.run_attacks()
        show screen screen_rpg onlayer rpg_context
        while RPG.encounter.has_signals():
            $ curr_signal = RPG.encounter.get_next_signal()
            if hasattr(curr_signal, "message") and type(curr_signal) != RPG.DebugSignal:
                show screen say_rpg(curr_signal.message) onlayer rpg_say
                pause
                hide screen say_rpg
        hide screen say_rpg
        hide screen screen_rpg

label pass_rpg:
    hide screen screen_rpg
    $ quick_menu = True
    window show
    if RPG.encounter.won:
        $ renpy.jump(RPG.encounter.on_win)
        # Thing for win condition
    else:
        $ renpy.jump(RPG.encounter.on_lose)
        # Thing for lose condition

label screenrpg_done:
    pass
