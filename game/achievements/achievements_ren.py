from renpy.game import persistent
from renpy.display.transition import Dissolve
import renpy.exports as renpy

persistent.achievements = set()
determination = Dissolve(0.0)

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

        if not any(self.name == a.name for a in persistent.achievements):
            persistent.achievements.add(self)

    @property
    def desc(self) -> str:
        return self.unlocked_desc if self.unlocked else self.locked_desc

    @property
    def icon(self) -> str:
        if self.unlocked:
            return self.icon_image

        return f"{self.icon_image}_locked"

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Achievement):
            return self.name == other.name
        return False

    def unlock(self):
        if self.unlocked:
            return

        self.unlocked = True
        persistent.achievements.add(self)
        renpy.with_statement(determination)
        renpy.show_screen("popup", self)
        renpy.with_statement(determination)


class AchievementManager:
    @property
    def unlocked(self) -> list[Achievement]:
        return [a for a in persistent.achievements if a.unlocked]

    @property
    def locked(self) -> list[Achievement]:
        return [a for a in persistent.achievements if not a.unlocked]

    def get(self, name: str) -> Achievement:
        for achievement in persistent.achievements:
            if achievement.name == name:
                return achievement

        raise ValueError(f"Unrecognized achievement {name}")


achievement_manager = AchievementManager()
