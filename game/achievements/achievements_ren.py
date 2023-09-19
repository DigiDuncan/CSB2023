from renpy.display.transform import Transform
from renpy.game import persistent
import renpy.exports as renpy

"""renpy
init python:
"""

from dataclasses import dataclass


@dataclass
class Achievement:
    name: str
    locked_desc: str
    unlocked_desc: str
    icon_image: str

    def __post_init__(self) -> None:
        self.unlocked = False

        if self.name in persistent.unlocked_achievements:
            self.unlocked = True

    @property
    def desc(self) -> str:
        return self.unlocked_desc if self.unlocked else self.locked_desc

    @property
    def icon(self) -> str:
        d = renpy.displayable(f"achievements/{self.icon_image}.png")
        if self.unlocked:
            return d

        return Transform(d, matrixcolor=SaturationMatrix(0.0))  # type: ignore

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Achievement):
            return self.name == other.name
        return False

    def unlock(self, show_screen = True):
        if self.unlocked:
            return

        self.unlocked = True
        persistent.unlocked_achievements.add(self.name)
        if show_screen:
            renpy.with_statement(determination)
            renpy.show_screen("popup", self)
            renpy.with_statement(determination)


class AchievementManager:
    @property
    def unlocked(self) -> list[Achievement]:
        return [a for a in achievements if a.unlocked]

    @property
    def locked(self) -> list[Achievement]:
        return [a for a in achievements if not a.unlocked]

    def get(self, name: str) -> Achievement:
        for achievement in achievements:
            if achievement.name == name:
                return achievement

        raise ValueError(f"Unrecognized achievement {name}")
    
    def unlock(self, name: str, show_screen = True):
        ach = self.get(name)
        if not ach.unlocked:
            renpy.sound.play("audio/achieve.wav", channel = "sound", loop = False)
            ach.unlock(show_screen)

    def unlock_all(self):
        for achievement in achievements:
            self.unlock(achievement.name, show_screen = False)

    def reset(self):
        for ach in achievements:
            ach.unlocked = False
        persistent.unlocked_achievements = set()


achievement_manager = AchievementManager()
