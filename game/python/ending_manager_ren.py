"""renpy
init python:
"""

# original endings
ROUTE_ENDINGS = [ "true", "south", "rockstar", "country", "friend", "archival", "call_cops", "ltt", "ytp" ]
BAD_ENDINGS = [ "asylum", "attorney", "bad_driver", "fuckin_raw", "god_fail", "god_success", "grand_dad", "hotwire", "pencil_shart", "premature", "revenge", "rip_house", "rip_money", "scottnt", "threw_away_fame", "top_loser" ] 
MISC_ENDINGS = [ "ai", "reality_break" ]
ORIGINAL_27 = ROUTE_ENDINGS + BAD_ENDINGS + MISC_ENDINGS
EXTRA_ENDING = [ "error" ]

# DX endings
# TODO: add more as they're completed.
DX_ROUTE_ENDINGS = [ "train_broke", "train_winner", "train_thief", "christmas" ]
DX_MISC_ENDINGS = [ "underpants" ]

# ALL endings, to be used mostly for timeline tracer but might be useful later
ALL_ENDINGS = ROUTE_ENDINGS + BAD_ENDINGS + MISC_ENDINGS + EXTRA_ENDING  + DX_ROUTE_ENDINGS + DX_MISC_ENDINGS

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
        for ending in ORIGINAL_27:
            if ending not in persistent.seen_endings:
                return False
        return True

ending_manager = EndingManager()
