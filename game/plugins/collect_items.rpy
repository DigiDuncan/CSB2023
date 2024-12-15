init python:
    def collect(i):
        global ITEM_MAP
        if i in ITEM_MAP.keys():
            persistent.collected.add(i)
            print(f"Collected item '{i}'.")
        else:
            print(f"WARNING: Failed to collect item '{i}', which does not exist in ITEM_MAP.")

            for i in ITEM_MAP.keys():
                if i not in persistent.collected:
                    collected_all_items = False
                if collected_all_items:
                    achievement_manager.unlock("items")
