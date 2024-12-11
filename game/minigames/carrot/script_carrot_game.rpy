# This game is a reference to Rhythm Heaven, or rather, my take on a Rhythm Heaven
# style game. CS chops carrots to the beat.

init python:
    import math

    class CarrotGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

            self.is_fcing = True
            self.song_time = 0.0

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


screen carrotgame():
    default templategame = CarrotGameDisplayable()
    # Add a background or any static images here.
    add templategame

label play_carrotgame:
    window hide
    $ quick_menu = False
    call screen carrotgame
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label carrotgame_done:
    # Thing to do after the game if we reach here.
    pass
