init python:
    import math

    class Attack:
        def __init__(self, name: str, func: callable[list[Fighter], None]):
            self.name = name
            self.func = func

        def run(self, fighters: list[Fighter]):
            self.func(fighters)

    class Fighter:
        def __init__(self, name: str, enemy: bool, hp: int, ap: int, atk: int, attacks: list[Attack], multiplier: float = 1):
            self.name = name
            self.enemy = enemy
            self.health_points = int(hp * multiplier)
            self.armor_points = ap
            self._attack_points = int(atk * multiplier)
            self.attacks = attacks

            self.confused: bool = False

        @property
        def dead(self) -> bool:
            return self.health_points <= 0

    class Encounter:
        def __init__(self, fighters: list[Fighter]):
            self.fighters = fighters

        @property
        def allies(self) -> list[Fighter]:
            return [f for f in self.fighters if not f.enemy]

        @property
        def enemies(self) -> list[Fighter]:
            return [f for f in self.fighters if f.enemy]


    class RPGGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # Do some fancy things here!

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load


screen rpggame:
    default rpggame = RPGGameDisplayable()
    # Add a background or any static images here.
    add rpggame

label play_rpggame:
    window hide
    $ quick_menu = False
    call screen rpggame
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label rpggame_done:
    # Thing to do after the game if we reach here.
    pass
