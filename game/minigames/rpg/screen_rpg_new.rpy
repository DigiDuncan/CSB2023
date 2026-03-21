label awawa_rpg_test:
    call screen rpg_screen_new()

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