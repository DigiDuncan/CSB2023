# Mocking
import renpy
persistent = {}
persistent.unlocked_achievements = set()

"""renpy
default persistent.unlocked_achievements = set()
init python:
"""

grayscale = Matrix(
    [0.2126, 0.7152, 0.0722, 0,
    0.2126, 0.7152, 0.0722, 0,
    0.2126, 0.7152, 0.0722, 0,
    0.0000, 0.0000, 0.0000, 1]
)

achieves = [
        ("Ocean Man", "???", "Go west eight times.", "ocean")
    ]

class Achievement:
    def __init__(self, name: str, locked_desc: str, unlocked_dec: str, icon: str):
        self.name = name
        self.locked_desc = locked_desc
        self.unlocked_desc = unlocked_dec
        self._icon = icon

        self.unlocked = False

    @property
    def desc(self) -> str:
        return self.unlocked_desc if self.unlocked else self.unlocked_desc
    
    @property
    def icon(self) -> renpy.Displayable:
        if self.unlocked:
            return renpy.displayable(self._icon)
        else:
            return renpy.Transform(child = renpy.displayable(self._icon), function = grayscale)

class AchievementManager:
    def __init__(self):
        self.achievements: list[Achievement] = []

        for t in achieves:
            self.achievements.append(Achievement(*t))

        for a in self.achievements:
            if a.name in persistent.unlocked_achievements:
                a.unlocked = True

    def unlock(self, name: str):
        if name not in [a.name for a in self.achievements]:
            raise ValueError(f"Unrecognized achievement {name}")
        ach = [a for a in self.achievements if a.name == name][0]
        ach.unlocked = True

    def reset(self):
        for a in self.achievements:
            a.unlocked = False
