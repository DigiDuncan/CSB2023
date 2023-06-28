"""renpy
screen popup(a):
    zorder 100
    layer "popup"
    style_prefix "popup"

    frame at popup_appear:
        xysize(367, 152)
        image a.icon:
            xysize(100, 100)
            xanchor 0.0 xpos 17
            yanchor 0.0 ypos 19
        image "popup.png":
            xanchor 0.0 xpos -2
            yanchor 0.0 ypos -2
        vbox:
            xysize(320, 83)
            xanchor 0.0 xpos 132
            yanchor 0.0 ypos 30
            spacing 15
            text a.name:
                size 22
                font "fonts/DIN-Medium.ttf"
                layout "greedy"
            text a.desc:
                size 16
                xmaximum 180
                font "fonts/DIN-Medium.ttf"
                layout "greedy"

    timer 5 action Hide('popup')

transform popup_appear:
    on show:
        xalign 1.0
        yanchor 0.0 ypos 1.0
        linear 0.5 yanchor 1.0
    on hide:
        linear 0.5 yanchor 0.0

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
        ("ZUP!", "???", "Start the game.", "zup"),
        ("I Don't Like People!", "Avoid responsibility.", "Tell CS not to go to Wal-Mart.", "no_person"),
        ("Dead Meme", "???", "Sparta kick Wesley.", "sparta"),
        ("#1 Rated Pooper", "???", "Use your skills to keep your job.", "poop"),
        ("Can We Go Back?", "???", "Try to go back to Canada.", "compass"),
        ("Ocean Man", "???", "Go west eight times.", "ocean"),
        ("Bored", "Sit through all the car dialouge.", "Sit through all the car dialouge.", "yawn"),
        ("HoH SiS's Most Wanted", "???", "Complete CSBI.", "csbi"),
        ("Welcome to CSBIII, Mother Fucker", "???", "Complete CSBII.", "csbii")
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
        return self.unlocked_desc if self.unlocked else self.locked_desc
    
    @property
    def icon(self) -> renpy.Displayable:
        if self.unlocked:
            return renpy.displayable(self._icon)
        else:
            return Transform(child = renpy.displayable(self._icon), matrixcolor = grayscale)

class AchievementManager:
    def __init__(self):
        self.achievements: list[Achievement] = []

        for t in achieves:
            self.achievements.append(Achievement(*t))

        for a in self.achievements:
            if a.name in persistent.unlocked_achievements:
                a.unlocked = True

    @property
    def unlocked(self) -> list[Achievement]:
        return [a for a in self.achievements if a.unlocked]
    
    @property
    def locked(self) -> list[Achievement]:
        return [a for a in self.achievements if not a.unlocked]

    def get(self, name: str) -> Achievement:
        if name not in [a.name for a in self.achievements]:
            raise ValueError(f"Unrecognized achievement {name}")
        ach = [a for a in self.achievements if a.name == name][0]
        return ach

    def unlock(self, name: str):
        ach = self.get(name)
        if not ach.unlocked:
            ach.unlocked = True
            persistent.unlocked_achievements.add(name)
            renpy.with_statement(determination)
            renpy.show_screen("popup", ach)
            renpy.with_statement(determination)

    def reset(self):
        for a in self.achievements:
            a.unlocked = False
        persistent.unlocked_achievements = set()


achievement_manager = AchievementManager()
