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
    if renpy.seen_label("train_home_rich_thief") and renpy.seen_label("train_home_rich_winner") and renpy.seen_label("train_home_broke"):
        $ achievement_manager.unlock("train_all")

    # unlock awawa mode if you've seen all there is to see in train route
    if "train_all" in persistent.unlocked_achievements and "beat_tate" in persistent.unlocked_achievements:
        if persistent.awawa_mode == False:
            $ persistent.awawa_mode = True
            call screen special_unlock("Awa awawa? AAAAAA! You've unlocked Awawa Mode! Check it out in CSettings!")
    return
