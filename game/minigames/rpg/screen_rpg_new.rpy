label play_rpg_game:
    window hide
    $ quick_menu = False
    scene image RPG.encounter.background
    $ renpy.music.play(MUSIC_MAP[RPG.encounter.music]["file"])
    $ persistent.heard.add(str(RPG.encounter.music))
    # This is where the game actually takes place.
    show screen screen_rpg_new() onlayer rpg_context
    show screen say_rpg(RPG.encounter.intro_text) onlayer rpg_say
    $ renpy.pause(delay=None, modal=True)
    hide screen screen_rpg_new
    hide screen say_rpg
    while RPG.encounter.won is None:
        call screen screen_rpg_new()
        $ RPG.rpg_logger.debug(f"=== TURN {RPG.encounter.turn} ===")
        $ RPG.encounter.run_attacks()
        $ RPG.encounter.run_effects()
        $ RPG.encounter.cleanup_turn()
        if RPG.encounter.won is not None:
            jump pass_rpg
        # Visuals and stuff need to go here.
        # Reset variables at the end
        $ RPG.encounter.subturn = 0

    jump pass_rpg

screen rpg_screen_new():

    if RPG.encounter.won is None:

        $ current_ally = RPG.encounter.allies[RPG.encounter.subturn]
        default current_ally_mode = None

        ##### ATTACK MODE
        if current_ally_mode == "ATK":
            vbox:
                text "Attacking!"         
                text "Select a target"
                textbutton "Pretend target":
                    action [
                        SetScreenVariable("current_ally_mode", "None")
                        # Increment turn here
                    ]

        ##### DEFEND MODE
        elif current_ally_mode == "DEF":
            text "Defending!"
            textbutton "Confirm":
                action [
                    SetScreenVariable("current_ally_mode", "None")
                    # Increment turn here
                ]

        ##### DEFAULT MODE
        else:
            vbox:
                text "What will this fighter do?"
                textbutton "Attack" action SetScreenVariable("current_ally_mode", "ATK")
                textbutton "Defend" action SetScreenVariable("current_ally_mode", "DEF")
