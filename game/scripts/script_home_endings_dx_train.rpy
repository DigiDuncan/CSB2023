label train_home_rich_thief:
    "Placeholder for if you completed train route with recovered stolen money."
    $ achievement_manager.unlock("All Aboard!")
    return

label train_home_rich_winner:
    "Placeholder for if you completed train route with recovered Vegas winnings."
    $ achievement_manager.unlock("All Aboard!")
    return

label train_home_broke:
    "Placeholder for if you completed train route without any money."
    $ achievement_manager.unlock("All Aboard!")
    return
