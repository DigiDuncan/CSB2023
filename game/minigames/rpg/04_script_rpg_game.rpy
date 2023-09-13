screen rpggame():
    add rpggame.encounter.background
    add rpggame

label game_loop:
    python:
        global rpggame
        encounter = rpggame.encounter
        while encounter.won is None:
            # First phase, get the user inputs of what each fighter should do.
            actions = []
            for c in range(len(encounter.allies)):
                curr_fighter = encounter.allies[c]
                if not curr_fighter.dead:
                    print("Current fighter: ", curr_fighter.name)
                    valid_move = False
                    attacks = []
                    for i, a in enumerate(curr_fighter.attacks):
                        name = a.name if a._turns_until_available == 0 else f"{a.name} [[{a._turns_until_available} turns remaining]"
                        attacks.append((name, str(i)))
                    print("Attacks:", attacks)
                    while not valid_move:
                        selected_move = renpy.display_menu([("What will " + curr_fighter.name + " do?", None)] + attacks)
                        curr_attack = curr_fighter.attacks[int(selected_move)]
                        print("Attack selected:", curr_attack.name)
                        valid_move = curr_attack.available
                        if not valid_move:
                            print("Invalid move.")
                    target_count = curr_attack.target_count
                    targets = []
                    target_type = curr_attack.target_type
                    print("Target count:", target_count)
                    print("Target type:", target_type)
                    if target_count == 0:
                        print("Auto targeting...")
                        if target_type == "enemies":
                            targets = encounter.enemies
                        if target_type == "allies":
                            targets = encounter.allies
                        if target_type == "all":
                            targets = encounter.fighters
                    else:
                        for g in range(target_count):
                            targets.append(renpy.display_menu([("Who will " + curr_fighter.name + " attack? (" + str(target_count - g) + ")", None)] + [(e.name, e) for e in getattr(encounter, curr_attack.target_type)]))
                    print("Targets: ", [t.name for t in targets])
                    actions.append((curr_fighter, int(selected_move), targets))
            # Execute the attacks
            print("Executing ally moves.")
            for c in range(len(actions)):
                renpy.notify(actions[c][0].name + " uses " + actions[c][0].attacks[actions[c][1]].name + " on " + sentence_join([f.name for f in actions[c][2]]))
                renpy.pause(1.0)
                answer = actions[c][0].attack(actions[c][1], actions[c][2])
            print("Executing enemy moves.")
            for e in encounter.enemies:
                e.attack_ai(encounter)
            renpy.redraw(rpggame, 0)
            print("Running tick.")
            for f in encounter.turn_order:
                f.tick()
                if f.dead:
                    encounter.fighters.remove(f)
            renpy.redraw(rpggame, 0)

    jump rpggame_done

label play_rpggame:
    window hide
    $ quick_menu = False
    play music rpggame.encounter.music
    show screen rpggame
    jump game_loop

label rpggame_done:
    stop music
    $ quick_menu = True
    window show
    hide screen rpggame

    if rpggame.encounter.won == True:
        $ renpy.jump(rpggame.encounter.on_win)
    else:
        $ renpy.jump(rpggame.encounter.on_lose)
