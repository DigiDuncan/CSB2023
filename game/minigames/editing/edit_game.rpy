init python:
    import math

    class EditGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # Do some fancy things here!
            rectangle_renderer = renpy.render(Solid("#00FF00", xysize=(600, 900)), 1920, 1080, st, at)
            r.blit(rectangle_renderer, (50, 50))
            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load

screen edit_game:
    default edit_game = EditGameDisplayable()
    # Add a background or any static images here.
    add edit_game

label play_edit_game:
    window hide
    $ quick_menu = False
    call screen edit_game
    $ quick_menu = True
    window show

    if _return == True:
        pass
    else:
        pass

label edit_game_done:
    # Thing to do after the game if we reach here.