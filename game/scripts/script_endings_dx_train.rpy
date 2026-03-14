label train_home_rich_thief:
    "Placeholder for if you completed train route with recovered stolen money."
    $ ending_manager.mark("train_thief")
    jump train_very_final

label train_home_rich_winner:
    "Placeholder for if you completed train route with recovered Vegas winnings."
    $ ending_manager.mark("train_winner")
    jump train_very_final

label train_home_broke:
    "Placeholder for if you completed train route without any money."
    $ ending_manager.mark("train_broke")
    jump train_very_final

label train_very_final:

    python:
        # track how many endings you've seen, give achievement for first-time playthrough
        train_endings = {"train_home_rich_thief", "train_home_rich_winner", "train_home_broke"}

        if "train_all" not in persistent.unlocked_achievements or "train_first" not in persistent.unlocked_achievements:
            count_seen = 0
            for e in train_endings:
                if renpy.seen_label(e):
                    achievement_manager.unlock("train_first")
                    count_seen = count_seen + 1
                   
            persistent.train_routes_seen = count_seen

        # unlock the achievement if you've seen all routes
        if persistent.train_routes_seen == 3:
            achievement_manager.unlock("train_all")
 
            # awawa mode unlock
            if "beat_tate" in persistent.unlocked_achievements:
                if not persistent.awawa_mode:
                    persistent.awawa_mode = True
                    renpy.call_screen("special_unlock", "Awa awawa? AAAAAA! You've unlocked Awawa Mode! Check it out in CSettings!")

