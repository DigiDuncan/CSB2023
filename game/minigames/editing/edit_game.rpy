init python:
    import math

    hit_width = 69
    hit_position = 69

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
            rectangle_renderer = renpy.render(Solid("#00FF00", xysize=(hit_width, 115)), 1920, 1080, st, at)
            r.blit(rectangle_renderer, (hit_position, 454))
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

screen edit_game:
    default edit_game = EditGameDisplayable()
    # Add a background or any static images here.
    add "minigames/editing/bg.png"
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