init python:
    import math

    # Constants

    class CarGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            # Set start time if it isn't (frame 0)
            if self.start_time is None:
                self.start_time = st

            # Render object we return at the end
            r = renpy.Render(1920, 1080)

            # Main game loop
            pass

            renpy.redraw(self, 0)
            return r
            
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_LEFT:
                pass
            if self.win is not None:
                return self.win

        def visit(self):
            return []


screen pencilgame:
    default pencilgame = CarGameDisplayable()
    add "minigames/car/background.png" at transform:
        yanchor 0.5 ypos 0.0
        linear 1.0 ypos 1.0
        repeat
    add pencilgame

label play_pencilgame:
    window hide
    $ quick_menu = False
    call screen pencilgame
    $ quick_menu = True
    window show

    if _return == True:
        jump win_pencil
    else:
        arceus "You dumb foreskin."
        jump play_pencilgame

label pencilgame_done:
    show arceus
    arceus ":3"
