import renpy.exports as renpy

"""renpy
init python:
"""

from dataclasses import dataclass
from typing import TypedDict
import json

class CommentaryData(TypedDict):
    audio_path: str
    speaker: str
    transcript: str
    length: float

@dataclass
class Commentary:
    audio_path: str
    speaker: str
    transcript: str
    length: float

    @property
    def full_path(self) -> str:
        return "audio/dxcom/" + self.audio_path + ".ogg"

    @property
    def full_text(self) -> str:
        return f"{self.speaker}: {self.transcript}"

    @property
    def color(self) -> str:
        if self.speaker == "Digi":
            return "#0fcdf7"
        elif self.speaker == "Arceus":
            return "#f1c40f"
        elif self.speaker == "Kitty":
            return "#51c6ff"
        elif self.speaker == "Pakoo":
            return "#a85cff"
        elif self.speaker == "Tate":
            return "#ffdbfc"
        elif self.speaker == "Baker":
            return "#9900b2"
        elif self.speaker == "Mika":
            return "#f5b226"
        else:
            return "#ffffff"


class CommentaryString:
    def __init__(self, id: str, commentaries: list[Commentary]):
        self.id = id
        self.commentaries = commentaries

    @classmethod
    def from_JSON(cls, id: str, data: list[CommentaryData]) -> "CommentaryString":
        commentaries = []
        for d in data:
            commentaries.append(Commentary(d["audio_path"], d["speaker"], d["transcript"], d["length"]))
        return CommentaryString(id, commentaries)

    def show(self):
        for c in self.commentaries:
            renpy.with_statement(determination)
            renpy.show_screen("_dxcom", c)
            renpy.music.play(c.full_path, channel="dxcom", loop=False, relative_volume = 1.25)
            renpy.with_statement(determination)
            renpy.pause(c.length)


class CommentaryManager:
    def __init__(self):
        with renpy.open_file("data/dxcom.json") as j:
            jsondata = json.load(j)

        self.strings: dict[str, CommentaryString] = {}

        for k, v in jsondata.items():
            self.strings[k] = CommentaryString.from_JSON(k, v)

    def play(self, id: str):
        self.strings[id].show()

commentary_manager = CommentaryManager()
