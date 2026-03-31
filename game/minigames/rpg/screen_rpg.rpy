"""
TODO list
- Add functionality to the attack text
- Depending on the action selected add the action to a list (To pass back to the back end)
- Make sprites be positioned dynamically based on number of enemies - bigger crowds should mean a tighter squeeze!
- Don't let anyone go completely offscreen!
- Fix the smaller sprites such as the K-types that are getting Mike Wazowski'd
"""

python early:
    def bypass_append(renpy_list, element):
        renpy_list.append(element)
    def print_action(print_str):
        logger.info(print_str)
    def dev_win(current_encounter):
        current_encounter.dev_win()
    def clear_list(l):
        l.clear()

init python:
    renpy.add_layer("rpg_context", above="master")
    renpy.add_layer("rpg_say", above="rpg_context")

    # Moving these things outside to here so that they can be accessed by the screen
    # and by functions. This isn't an ideal solution but nothing here is.
    working_list = []
    current_ally_mode = None

    def select_target(target):
        global current_ally_mode
        current_ally = RPG.encounter.allies[RPG.encounter.subturn]

        if target is not None:
            working_list.append(target)
        if len(working_list) == current_ally.next_attack.attack.target_count:
            current_ally.next_targets = working_list
            if RPG.encounter.subturn + 1 != len(RPG.encounter.allies):
                RPG.encounter.subturn += 1
            current_ally_mode = None
            renpy.restart_interaction()

    def get_next_signal() -> RPG.Signal | None:
        while RPG.encounter.has_signals():
            signal = RPG.encounter.get_next_signal()
            if isinstance(signal, RPG.DebugSignal):
                continue
            else:
                return signal
        return None

    def get_next_signals() -> list[RPG.Signal]:
        signals = []
        while RPG.encounter.has_signals():
            signal = RPG.encounter.get_next_signal()
            if isinstance(signal, RPG.DebugSignal):
                continue
            else:
                return signals.append(signal)
        return signals

init:
    transform _rpg_intro:
        on show:
            xanchor 0.5 xpos 0.5
            yanchor 0.5 ypos 0.05
            alpha 0.00
            ease_cubic 0.5 alpha 1.00
            time 2.5
            ease_expo 1 alpha 0.00

######### SAY SCREEN
screen say_rpg(rpg_what):
    modal True
    python:
        show_window = False
        renpy.choice_for_skipping()
    key "dismiss" action [ 
        Hide("say_rpg", immediately=True)
    ]

    frame:
        xalign 0.5 yalign 1.0
        padding(80, 5)
        xysize(1916, 262)
        background get_themed_attribute("rpg/main_box")
        frame:
            background None
            xsize 1.0 ysize 1.0
            xanchor 0.5 yanchor 0.5
            xpos 0.5 ypos 0.5

            frame:
                background None
                grid 1 1: # This is to keep the text lined up consistently with other screens
                    frame: 
                        background None
                        text rpg_what

######### STAT BOXES
screen rpg_stat_box(fighter, current_ally_mode):
    $ current_fighter = RPG.encounter.allies[RPG.encounter.subturn % len(RPG.encounter.allies)]
    frame:
        xalign 0.5 yalign 1.0

        ###### Change contents based on what "mode" this box is in.
        if not fighter.dead:

            ### Enemy only
            if fighter in RPG.encounter.enemies:
                background get_themed_attribute("rpg/small_box")
                xysize(475,105)

            ### For allies
            if fighter in RPG.encounter.allies:
                ### If this ally is selected
                if current_fighter and current_fighter == fighter:

                    if fighter in RPG.encounter.allies:
                        background get_themed_attribute("rpg/tall_box")
                        xysize(475,201)

                        # The attack button
                        frame:
                            background None
                            xsize 1.0 ysize 87
                            xalign 0.5 yalign 1.0
                            
                            imagebutton:
                                align(0.0, 1.0)
                                idle get_themed_attribute("rpg/attack_button")
                                hover get_themed_attribute("rpg/attack_button", prefix = "selectable")
                                insensitive get_themed_attribute("rpg/attack_button", prefix = "insensitive")
                                hover_sound "audio/sfx/sfx_select.ogg"
                                action [
                                    SensitiveIf(current_ally_mode != "TGT"),
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    SetVariable("current_ally_mode", "ATK")
                                    # Notify("Attack pressed on fighter "+str(fighter.display_name)+"!")
                                ]

                            # The defend button
                            imagebutton:
                                align(1.0, 1.0)
                                idle get_themed_attribute("rpg/defend_button")
                                hover get_themed_attribute("rpg/defend_button", prefix = "selectable")
                                insensitive get_themed_attribute("rpg/defend_button", prefix = "insensitive")
                                hover_sound "audio/sfx/sfx_select.ogg"
                                action [
                                    SensitiveIf(current_ally_mode != "TGT"),
                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                    SetVariable("current_ally_mode", "DEF")
                                    # Notify("Defend pressed on fighter "+str(fighter.display_name)+"!")
                                ]

                ### For unselected allies
                else:
                    background get_themed_attribute("rpg/small_box")
                    # TODO: these two lines don't work, this button IS functional just not changing visually when hovered yet
                    idle_background get_themed_attribute("rpg/small_box")
                    hover_background get_themed_attribute("rpg/small_box", prefix = "selectable")
                    xysize(475,105)
                    yalign 1.0

                    button:
                        xysize(475,105)
                        action [
                            SensitiveIf(current_ally_mode != "TGT"),
                            SetVariable("RPG.encounter.subturn", RPG.encounter.allies.index(fighter)),
                            SetVariable("current_ally_mode", None)
                        ]

            ###### Begin common items
            frame:
                background None
                xysize(465,105)
                xalign 0.5 yalign 0

                hbox:
                    xsize 195
                    xfill True yfill True
                    xalign 0 yalign 0
                    
                    ### Fighter portrait
                    frame:
                        background None 
                        
                        python:
                            if fighter.portrait:
                                this_portrait = fighter.portrait
                            else:
                                this_portrait = "gui/rpg_common/portraits/unknown.png"

                        add this_portrait:
                            xoffset -8 yoffset -9

                    ### ATK/DEF
                    frame:
                        background None
                        xalign 0
                        xmaximum 110 ysize 1.0
                        xoffset -20 yoffset -4

                        vbox:
                            xalign 0 yalign 0

                            frame:
                                background None
                                xmaximum 110 ysize 32
                                hbox:
                                    xmaximum 110
                                    spacing 5
                                    add get_themed_attribute("rpg/attack"):
                                        xalign 0 yalign 0.5
                                    text str(fighter.attack):
                                        size 32
                                        xalign 0 yalign 0.5
                                        text_align 0  
                            frame:
                                background None
                                xmaximum 110 ysize 32
                                hbox:
                                    xmaximum 110
                                    spacing 5
                                    add get_themed_attribute("rpg/defense"):
                                        xalign 0 yalign 0.5
                                    text str(fighter.defense):
                                        size 32
                                        xalign 0 yalign 0.5
                                        text_align 0  

                vbox:
                    xalign 1.0 yalign 0
                    yoffset -7

                    ### Fighter name
                    text fighter.display_name:
                        xalign 1.0 yalign 0
                        text_align 1.0

                    ### HP bar handling
                    hbox:
                        spacing 5
                        add get_themed_attribute("rpg/hp") yalign 0.5
                        frame:
                            background Solid("#132F83")
                            padding(0,0)
                            xysize(228, 32)
                            xalign 1.0 yalign 1.0

                            $ h_text = fighter.character.custom_health_string if fighter.character.custom_health_string else str(fighter.hit_points)+"/"+str(fighter.max_hp)

                            # Custom bar only
                            if fighter.character.custom_health_bar and not fighter.infinite:
                                $ h_bar = renpy.get_registered_image(fighter.character.custom_health_bar)
                                add h_bar corner1(int(228-(228*(fighter.hit_points/fighter.max_hp))),0) corner2(228,32) xalign 1.0
                                text h_text:
                                    xalign 1.0 yalign 0.5
                            # Custom bar + infinite HP
                            elif fighter.character.custom_health_bar and fighter.infinite:
                                $ h_bar = renpy.get_registered_image(fighter.character.custom_health_bar)
                                add h_bar corner1(0,0) corner2(228,32) xalign 1.0
                                text h_text:
                                    xalign 1.0 yalign 0.5
                            # Only infinite HP
                            elif fighter.infinite:
                                $ inf_bar = renpy.get_registered_image("hp_bar_inf")
                                add inf_bar corner1(0,0) corner2(228,32) xalign 1.0
                                add get_themed_attribute("rpg/infinite") xalign 1.0 yalign 0.5
                            # Overheal
                            # TODO: should we have a case for custom + overheal for non-infinite?
                            elif fighter.hit_points > fighter.max_hp and not fighter.character.custom_health_bar:
                                $ overheal_bar = renpy.get_registered_image("hp_bar_overheal")
                                add overheal_bar corner1(0,0) corner2(228,32) xalign 1.0
                                text h_text:
                                    xalign 1.0 yalign 0.5
                            # Normal bar
                            else:
                                add "gui/rpg_common/hp_bars/hp_bar.png" corner1(int(228-(228*(fighter.hit_points/fighter.max_hp))),0) corner2(228,32) xalign 1.0
                                text h_text:
                                    xalign 1.0 yalign 0.5

                ### Status effects
                if len(fighter.effects) > 0:
                    
                    python:
                        # Count up all the effects
                        checked_effects = {}
                        effect_sources = {}
                        for effect in fighter.effects:
                            if effect.effect not in checked_effects:
                                checked_effects[effect.effect] = 1
                                effect_sources[effect.effect] = [effect.source.display_name]
                            else:
                                checked_effects[effect.effect] += 1
                                effect_sources[effect.effect].append(effect.source.display_name)
                    
                        # Get the position of the box
                        if fighter in RPG.encounter.enemies:
                            effect_pos = 98
                            effect_yanchor = 0.0
                        else:
                            effect_yanchor = 1.0
                            effect_pos = -17

                    frame:
                        xanchor 1.0 yanchor effect_yanchor
                        xpos 1.0 ypos effect_pos
                        xoffset 11

                        hbox:
                            for effect in checked_effects:
                                frame:
                                    background None
                                    xysize(36,36)

                                    $ effect_hover_icon = effect.icon[:-4] + "_hover" + effect.icon[-4:]

                                    imagebutton:
                                        xalign 0.5 yalign 0.5
                                        idle effect.icon
                                        hover effect_hover_icon
                                        hover_sound "audio/sfx/sfx_select.ogg"
                                        action NullAction()
                                        tooltip [effect.name, effect.description, str(checked_effects[effect]), f"From {sentence_join(effect_sources[effect], oxford=True)}"]

                                    if checked_effects[effect] > 1:
                                        text str(checked_effects[effect]):
                                            size 16
                                            xanchor 1.0 yanchor 0.0
                                            xoffset 33 yoffset -11
                                            text_align 1.0
                                            color Color("#FFFFFF")
                                            outlines [(2.25, "#000000", absolute(0), absolute(0))]

        ### For dead fighters
        else:
            background None
            frame:
                background None
                xysize(465,105)

######### ACTUAL SCREEN HERE

screen screen_rpg(no_stat_boxes = False):
    if RPG.encounter.won is None:
        $ renpy.suspend_rollback(True)
        $ current_ally = RPG.encounter.allies[RPG.encounter.subturn % len(RPG.encounter.allies)]

        # Drawing the enemies in the background.
        frame:
            background None
            xsize 1.1 ysize 0.7
            xanchor 0.5 yanchor 1.0
            xpos 0.5 ypos 0.8

            $ dynamic_spacing = 100 - (len(RPG.encounter.enemies) * 100)

            hbox:
                xfill True
                xalign 0.5 yalign 1.0
                spacing dynamic_spacing

                for enemy in RPG.encounter.enemies:
                    if not enemy.dead:
                        # Attempt to add animated sprite if one exists, else fallback to the normal sprite
                        python:
                            try:
                                enemy_sprite = enemy.anim_sprite
                            except:
                                enemy_sprite = enemy.sprite

                        add enemy_sprite:
                            xalign 0.5 yalign 1.0
                            ysize 1.0
                            fit "scale-down"
                    else:
                        add Null(500,500)

        # Add enemy stat boxes
        frame:
            background None
            xsize 1920 ysize 105
            xalign 0.5 yalign 0

            grid len(RPG.encounter.enemies) 1:
                xalign 0.5
                xfill True
                if not no_stat_boxes:
                    for e in range(len(RPG.encounter.enemies)):
                        use rpg_stat_box(RPG.encounter.enemies[e], current_ally_mode)

        # Add player stat boxes
        frame:
            background None
            xsize 1920 ymaximum 201
            yanchor 1.0
            xalign 0.5 ypos 819

            grid len(RPG.encounter.allies) 1:
                xalign 0.5 yalign 1.0
                xfill True
                if not no_stat_boxes:
                    for a in range(len(RPG.encounter.allies)):
                        use rpg_stat_box(RPG.encounter.allies[a], current_ally_mode)

        # This is the context menu of the RPG
        frame:
            xsize 1916
            xalign 0.5 yalign 1.0 
            padding(0,0)
            background None
            has vbox
            box_reverse True

            # The Action Selection Box:
            frame:
                padding(80, 5)
                xysize(1916, 262)
                background get_themed_attribute("rpg/main_box")
                xalign 0.5
                frame:
                    background None
                    xfill True yfill True

                    # The options.
                    frame:
                        background None
                        xsize 1.0 ysize 1.0

                        ### If you choose to attack, get access to the attacks.
                        if current_ally_mode == "ATK":
                                                       
                            viewport:
                                xsize 0.75 ysize 1.0
                                                                
                                # Mostly for Copguy EX
                                if current_ally.attacks and len(current_ally.attacks) > 4:
                                    scrollbars "vertical"
                                    mousewheel True

                                grid 2 len(current_ally.attacks) / 2 + 1:
                                    xsize 0.5 ysize 1.0
                                    
                                    for attack in current_ally.attacks:
                                        python:
                                            attack_actions = []
                                            # If the attack is not available, make this insensitive
                                            attack_actions.append(Function(current_ally.set_next_attack, attack))
                                            attack_actions.append(Function(clear_list, working_list))
                                            attack_actions.append(SetVariable("current_ally_mode", "TGT"))
                                            # This might be needed if the attack has 0 targets
                                            if attack.attack.target_count == 0:
                                                attack_actions.append(Function(current_ally.set_next_targets, []))

                                        # Adds selectable attack texts/descriptions
                                        frame:
                                            background None
                                            xsize 1.0 ymaximum 120
                                            button:
                                                hover_sound "audio/sfx/sfx_select.ogg"
                                                action [
                                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                                    *attack_actions
                                                ]
                                                if not attack.available:
                                                    sensitive False

                                                vbox:
                                                    text attack.name:
                                                        size 40
                                                        color gui.text_color
                                                        hover_color gui.hover_color
                                                        selected_color gui.selected_color
                                                        insensitive_color gui.insensitive_color

                                                    text "("+attack.attack.properties+")":
                                                        xoffset 32
                                                        size 21
                                                        color gui.text_color
                                                        hover_color gui.hover_color
                                                        selected_color gui.selected_color
                                                        insensitive_color gui.insensitive_color

                                                    text "{alpha=0.5}"+attack.attack.description+"{/alpha}":
                                                        xoffset 32
                                                        size 21
                                                        color gui.text_color
                                                        hover_color gui.hover_color
                                                        selected_color gui.selected_color
                                                        insensitive_color gui.insensitive_color
                        
                               
                        ### If you choose to defend, do that.
                        elif current_ally_mode == "DEF":
                            frame:
                                background None
                                xsize 1.0 ysize 1.0
                                text current_ally.display_name+" will defend this turn!"

                                imagebutton:
                                    xalign 1.0
                                    yalign 1.0
                                    idle get_themed_attribute("rpg/confirm_button")
                                    hover get_themed_attribute("rpg/confirm_button", prefix = "selectable")
                                    hover_sound "audio/sfx/sfx_select.ogg"
                                    action [
                                        Play("sound", "audio/sfx/sfx_valid.ogg"),
                                        Function(current_ally.set_next_attack, RPG.encounter.DEFEND_ACTION),
                                        SetVariable("current_ally_mode", None),
                                        IncrementVariable("RPG.encounter.subturn")
                                    ]

                        elif current_ally_mode == "TGT":
                            $ targets = RPG.encounter.possible_targets(current_ally, current_ally.next_attack.attack)

                            python:
                                if current_ally_mode == "TGT":
                                    if current_ally.next_attack.attack.target_count == 0:
                                        select_target(None)

                            # Create visual buttons for target selection
                            vbox:
                                text _("Select target for [attack.name]:")
                                hbox:
                                    for target in targets:
                                        frame:
                                            background None
                                            yoffset 20
                                            xsize 200 ysize 148
                                            button:
                                                xalign 0.5 yalign 0

                                                hover_sound "audio/sfx/sfx_select.ogg"
                                                action [
                                                    SelectedIf(target in working_list),
                                                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                                                    Function(select_target, target)
                                                    ]

                                                # Conditional border because it was bothering me
                                                python:
                                                    if target in RPG.encounter.allies:
                                                        border_img =  "gui/rpg_common/portraits/border_sel_a.png"
                                                    else:
                                                        border_img =  "gui/rpg_common/portraits/border_sel_e.png"

                                                frame:
                                                    xysize(88,88)
                                                    xalign 0.5

                                                    # Portrait shenanigans
                                                    background target.portrait
                                                    hover_background Transform(target.portrait, matrixcolor=shade_select_matrix)
                                                    selected_background Composite(
                                                        (88,88),
                                                        (0,0), target.portrait,
                                                        (0,0), border_img
                                                    )
                                                    selected_hover_background Composite(
                                                        (88,88),
                                                        (0,0), Transform(target.portrait, matrixcolor=shade_select_matrix),
                                                        (0,0), border_img
                                                    )

                                                text "{size=-12}"+target.display_name:
                                                    color gui.text_color
                                                    hover_color gui.hover_color
                                                    selected_color gui.selected_color
                                                    selected_hover_color gui.accent_color
                                                    xalign 0.5 yalign 1.0
                                                    text_align 0.5

                        ### Default text
                        else:
                            frame:
                                background None
                                
                                # If the player goes back to a previous subturn, text will vary based on what the player chose to do
                                if current_ally.next_attack:
                                    if current_ally.next_attack.attack.target_count == 0:
                                        text _(current_ally.display_name+" will use "+current_ally.next_attack.name+"!")
                                    else:
                                        python:
                                            targets_list = []
                                            for t in current_ally.next_targets:
                                                targets_list.append(t)
                                            targets_list = list(set(targets_list))
                                            targets_list = sentence_join([t.display_name for t in targets_list], oxford=True)

                                        text current_ally.display_name+" will use "+current_ally.next_attack.name+" on "+targets_list+"!"
                                else:
                                    text _("What will "+current_ally.display_name+" do?")


        # If everything is set and good to go, show the confirm button)
        # TODO: Further checks to make sure everything is good and valid.
        if all(f.next_attack is not None for f in RPG.encounter.allies) and all(f.next_attack.attack.target_count == len(f.next_targets) for f in RPG.encounter.allies):
            imagebutton:
                xpos 1581 ypos 970 # it wanted to be stupid so it gets the manual positioning
                idle get_themed_attribute("rpg/confirm_button")
                hover get_themed_attribute("rpg/confirm_button", prefix = "selectable")
                hover_sound "audio/sfx/sfx_select.ogg"
                action [
                    Play("sound", "audio/sfx/sfx_valid.ogg"),
                    Return()
                ]

        # For effect data
        $ effect_info = GetTooltip()
        $ get_mouse()
        if effect_info:

            # Prevent box going offscreen on the right   
            python:
                if mouse_xy[0] + 125 > 1920:
                    effect_desc_xpos = 1797
                else:
                    effect_desc_xpos = mouse_xy[0]

            # Actually draw it
            frame:
                xanchor 0.5 yanchor 0

                xpos effect_desc_xpos 
                ypos mouse_xy[1]
                xmaximum 250

                vbox:
                    text effect_info[0]: # effect name
                        xalign 0.5
                        text_align 0.5
                        size 40

                    text effect_info[1]: # effect description
                        xalign 0.5
                        text_align 0.5
                        size 32

                    if effect_info[2] != "1":
                        text _("(×"+effect_info[2]+" multiplier)"): # effect multiplier info
                            xalign 0.5
                            text_align 0.5
                            size 21
                        
                    text effect_info[3]: # effect source info
                        color gui.idle_color
                        italic True
                        xalign 0.5
                        text_align 0.5
                        size 21

        # Signal processing mode
        if RPG.encounter.has_signals():
            $ signal = get_next_signal()
            if signal is not None:
                
                $ output_string = "If you're reading this, something is broken!"
                $ output_color = "#FFFF00"
                $ output_say = "If you're reading this, something is wrong!"

                # Handle visuals here
                # TODO: these colors blow and also we need better outlines
                python:
                    if isinstance(signal, RPG.IndicatorSignal):

                        # Handle numbers
                        if signal.value < 0:
                            output_color = "#FF0000"
                        else:
                            output_color = "#00FF00"

                        output_string = str(signal.value) + " " + str(signal.typ.name)

                if isinstance(signal, RPG.IndicatorSignal):   
                    text output_string at t_rpg_text(0.5, 0.5):
                        color output_color
                        outlines [(4.5, "#000000", absolute(0), absolute(0))]

                elif isinstance(signal, RPG.MessageSignal):   
                    use say_rpg( signal.message )

                # vbox:
                #     text str(signal)
                #     if isinstance(signal, RPG.IndicatorSignal):

                #         text _("{size=-12}{color=#AAAAAA}Pssst, Tate! This is an indicator! It's for [signal.target.name], it's type [signal.typ.name], and value [signal.value]!")
                #     textbutton _("Next") action Function(renpy.restart_interaction)

    # Debug
    # python:
    #     debug_text = f"Current Ally: {current_ally.display_name}\nCurrent Ally Mode: {current_ally_mode}\nNext Attack: {current_ally.next_attack.name}\nTarget Count: {current_ally.next_attack.attack.target_count if current_ally.next_attack is not None else None}"
    # text debug_text:
    #     xoffset 25
    #     yoffset 25
    #     outlines [(2.25, "#000000", absolute(0), absolute(0))]

    # Dev Backdoor
    key "K_END" action Jump("pass_rpg")

######### PLAY BATTLE

label play_rpggame:
    window hide
    $ quick_menu = False
    scene image RPG.encounter.background
    $ renpy.music.play(MUSIC_MAP[RPG.encounter.music]["file"])
    $ persistent.heard.add(str(RPG.encounter.music))
    # This is where the game actually takes place.
    show screen screen_rpg(True) onlayer rpg_context
    show screen say_rpg(RPG.encounter.intro_text) onlayer rpg_say
    $ renpy.pause(delay=None, modal=True)
    hide screen screen_rpg
    hide screen say_rpg
    while RPG.encounter.won is None:
        call screen screen_rpg()
        python:
            RPG.rpg_logger.debug(f"=== TURN {RPG.encounter.turn} ===")
            RPG.encounter.run_attacks()
            RPG.encounter.run_effects()
            RPG.encounter.cleanup_turn()
        if RPG.encounter.won is not None:
            jump pass_rpg
        # Visuals and stuff need to go here.
        # Reset variables at the end
        $ RPG.encounter.subturn = 0

    jump pass_rpg

######### END BATTLE

label pass_rpg:
    $ renpy.suspend_rollback(False)
    $ renpy.hide_screen("say_rpg", layer="rpg_say", immediately=True)
    $ renpy.hide_screen("screen_rpg", layer="rpg_context", immediately=True)

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
