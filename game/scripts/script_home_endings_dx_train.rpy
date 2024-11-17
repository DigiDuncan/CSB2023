label train_home_rich_thief:
    "Placeholder for if you completed train route with recovered stolen money."
    $ achievement_manager.unlock("train_first")
    jump train_very_final

label train_home_rich_winner:
    "Placeholder for if you completed train route with recovered Vegas winnings."
    $ achievement_manager.unlock("train_first")
    jump train_very_final

label train_home_broke:
    "Placeholder for if you completed train route without any money."
    $ achievement_manager.unlock("train_first")
    jump train_very_final

label train_very_final:

    # track how many endings you've seen
    python:
        train_endings = {"train_home_rich_thief", "train_home_rich_winner", "train_home_broke"}

        if "train_all" not in persistent.unlocked_achievements:
            count_seen = 0
            for e in train_endings:
                if renpy.seen_label(e):
                    count_seen = count_seen + 1
                   
            persistent.train_routes_seen = count_seen

        if persistent.train_routes_seen == 3:
            achievement_manager.unlock("train_all")

    # unlock awawa mode if you've seen all there is to see in train route
    if "train_all" in persistent.unlocked_achievements and "beat_tate" in persistent.unlocked_achievements:
        if persistent.awawa_mode == False:
            $ persistent.awawa_mode = True
            call screen special_unlock("Awa awawa? AAAAAA! You've unlocked Awawa Mode! Check it out in CSettings!")
    return
