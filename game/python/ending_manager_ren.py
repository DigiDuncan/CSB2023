"""renpy
init python:
"""

# only the original 27 endings here. not including error ending.
ROUTE_ENDINGS = [ "true", "south", "rockstar", "country", "friend", "archival", "call_cops", "ltt", "ytp" ]
BAD_ENDINGS = [ "asylum", "attorney", "bad_driver", "fuckin_raw", "god_fail", "god_success", "grand_dad", "hotwire", "pencil_shart", "premature", "revenge", "rip_house", "rip_money", "scottnt", "threw_away_fame", "top_loser" ] 
MISC_ENDINGS = [ "ai", "reality_break" ]

class EndingManager:
    def __init__(self):
        pass

    def mark(self, ending: str):
        if ending in ROUTE_ENDINGS or ending in BAD_ENDINGS or ending in MISC_ENDINGS:
            persistent.seen_endings.add(ending)
        else:
            raise ValueError(f"Unknown ending: {ending}")\

        if preferences.csbounciness == 100:
            if ending in ROUTE_ENDINGS:
                achievement_manager.unlock("bouncy")

    def seen(self, ending: str) -> bool:
        return ending in persistent.seen_endings

    def all_seen(self) -> bool:
        for ending in KNOWN_ENDINGS:
            if ending not in persistent.seen_endings:
                return False
        return True

ending_manager = EndingManager()
