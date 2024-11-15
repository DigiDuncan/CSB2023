from renpy.display.transform import Transform
from renpy.game import persistent
import renpy.exports as renpy

"""renpy
init python:
"""

from dataclasses import dataclass
from typing import TypedDict, Union
import json

class AchievementData(TypedDict):
    name: str
    locked: str
    unlocked: str
    img: str
    type: str
    hidden: bool
    dx: bool
    steps: Union[int, str]
    tracker: str

@dataclass
class Achievement:
    id: str
    name: str
    locked_desc: str
    unlocked_desc: str
    icon_image: str
    category: str
    hidden: bool = False
    dx: bool = False
    steps: int = 1
    tracker: str = None

    @property
    def stepped(self) -> bool:
        return self.steps != 1
   
    @property
    def unlocked(self) -> bool:
        if not self.stepped:
            return self.id in persistent.unlocked_achievements 
        else:
            return self.current_steps >= self.steps or self.id in persistent.unlocked_achievements

    @property
    def current_steps(self) -> int:
        if not self.stepped:
            return int(self.id in persistent.unlocked_achievements)
        var = getattr(persistent, self.tracker)
        if isinstance(var, set):
            return len(var)
        else:
            return var

    @property
    def progress(self) -> float:
        if not self.stepped:
            return float(self.unlocked)
        else:
            return min(1.0, self.current_steps / self.steps)

    @property
    def desc(self) -> str:
        return self.unlocked_desc if self.unlocked else self.locked_desc

    @property
    def icon(self) -> str:
        if self.dx:
            d = Composite((128, 128), (0, 0), f"images/achievements/{self.icon_image}.png", (0, 0), "images/achievements/dx_border.png")
        else:
            d = renpy.displayable(f"images/achievements/{self.icon_image}.png")

        if self.unlocked:
            return d
        else:
            return Transform(d, matrixcolor=SaturationMatrix(0.0))  # type: ignore

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Achievement):
            return self.name == other.name
        return False

    def __str__(self) -> str:
        return f"<Achievement {self.id} \"{self.name}\": {'Unlocked' if self.unlocked else 'Locked'} ({self.progress:.2%}%)>"

    def __repr__(self) -> str:
        return self.__str__()

    def unlock(self, show_screen = True):
        if self.unlocked:
            return

        persistent.unlocked_achievements.add(self.id)
        if show_screen:
            renpy.with_statement(determination)
            renpy.show_screen("popup", self)
            renpy.with_statement(determination)

    @classmethod
    def from_JSON(cls, id: str, data: AchievementData) -> "Achievement":
        a = Achievement(id, data["name"], data["locked"], data["unlocked"], data["img"], data["type"], data.get("hidden", False), data.get("dx", False))
        if "steps" in data:
            if isinstance(data["steps"], int):
                a.steps = data["steps"]
            elif isinstance(data["steps"], str):
                vars = globals() | locals()
                if data["steps"] in vars:
                    a.steps = vars[data["steps"]]
                else:
                    print(f"WARNING: {data['steps']} not defined before achievement load!")
            if "tracker" in data:
                a.tracker = data["tracker"]
            else:
                print(f"WARNING: {a.name} has no tracker defined, but has {a.steps} steps!")
        return a


class AchievementManager:
    def __init__(self) -> None:
        self.achievements: dict[str, Achievement] = {}
        with renpy.open_file("data/achievements.json") as j:
            jsondata = json.load(j)
        for k, v in jsondata.items():
            self.achievements[k] = Achievement.from_JSON(k, v)

    @property
    def unlocked(self) -> list[Achievement]:
        return [a for a in self.achievements.values() if a.unlocked]

    @property
    def locked(self) -> list[Achievement]:
        return [a for a in self.achievements.values() if not a.unlocked]

    def get(self, id: str) -> Achievement:
        for achievement in self.achievements:
            if achievement.id == id:
                return achievement

        raise ValueError(f"Unrecognized achievement {id}")
    
    def unlock(self, id: str, show_screen = True):
        ach = self.get(id)
        if not ach.unlocked:
            renpy.sound.play("audio/sfx/sfx_achieve.ogg", channel = "sound", loop = False)
            ach.unlock(show_screen)

    def unlock_all(self):
        for achievement in self.achievements:
            self.unlock(achievement.id, show_screen = False)

    def reset(self):
        persistent.unlocked_achievements = set()


achievement_manager = AchievementManager()
