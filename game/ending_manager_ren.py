KNOWN_ENDINGS = [
    "true", "south", "rockstar", "country", "friend", "archival"
]

persistent.current_endings = []

class EndingManager:
    def __init__(self):
        self.current_endings = persistent.current_endings