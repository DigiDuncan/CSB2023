from renpy.display.transform import Transform
from renpy.game import persistent
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
        return "dxcom/audio/" + self.audio_path + ".wav"
    
    @property
    def full_text(self) -> str:
        return f"{self.speaker}: {self.transcript}"
    
    @property
    def color(self) -> str:
        if self.speaker == "Digi":
            return "#0fcdf7"
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
            renpy.music.play(c.full_path, channel="dxcom", loop=False)
            renpy.with_statement(determination)
            renpy.pause(c.length)


class CommentaryManager:
    def __init__(self):
        with renpy.open_file("dxcom/dxcom.json") as j:
            jsondata = json.load(j)

        self.strings: dict[str, CommentaryString] = {}

        for k, v in jsondata.items():
            self.strings[k] = CommentaryString.from_JSON(k, v)

    def play(self, id: str):
        self.strings[id].show()

commentary_manager = CommentaryManager()
