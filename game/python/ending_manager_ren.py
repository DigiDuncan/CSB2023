"""renpy
init python:
"""

# TODO: ADD THE NEW ENDINGS HERE
KNOWN_ENDINGS = [
    "true", "south", "rockstar", "country", "friend", "archival"
]

class EndingManager:
    def __init__(self):
        pass

    def mark(self, ending: str):
        if ending in KNOWN_ENDINGS:
            persistent.seen_endings.add(ending)
        else:
            raise ValueError(f"Unknown ending: {ending}")\

        if preferences.csbounciness == 100:
            achievement_manager.unlock("bouncy")

    def seen(self, ending: str) -> bool:
        return ending in persistent.seen_endings

    def all_seen(self) -> bool:
        for ending in KNOWN_ENDINGS:
            if ending not in persistent.seen_endings:
                return False
        return True

ending_manager = EndingManager()
