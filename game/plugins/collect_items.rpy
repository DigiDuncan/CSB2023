init python:
    def collect(i):
        global ITEM_MAP
        if i in ITEM_MAP.keys():
            persistent.collected.add(i)
            logger.info(f"Collected item '{i}'.")
        else:
            logger.warn(f"Failed to collect item '{i}', which does not exist in ITEM_MAP.")

            for i in ITEM_MAP.keys():
                if i not in persistent.collected:
                    collected_all_items = False
                if collected_all_items:
                    achievement_manager.unlock("items")
