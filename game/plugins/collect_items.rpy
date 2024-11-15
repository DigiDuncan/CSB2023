init python:
    def collect(i):
        global item_map
        if i in item_map.keys():
            persistent.collected.add(i)
            print(f"Collected item '{i}'.")
        else:
            print(f"WARNING: Failed to collect item '{i}', which does not exist in item_map.")
        
            for i in item_map.keys():
                if i not in persistent.collected():
                    collected_all_items = False
                if collected_all_items:
                    achievement_manager.unlock("items")
