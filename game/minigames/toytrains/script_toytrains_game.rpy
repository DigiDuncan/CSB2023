init python:
    import math

    class ToyTrainsGameDisplayable(renpy.Displayable):
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


screen toytrainsgame:
    default toytrainsgame = ToyTrainsGameDisplayable()
    # Add a background or any static images here.
    add toytrainsgame

label play_toytrainsgame:
    window hide
    $ quick_menu = False
    play music hide_and_seek if_changed
    call screen toytrainsgame
    $ persistent.heard.add("Chiro - Hide and Seek")
    $ quick_menu = True
    window show

    if _return == True:
        $ achievement_manager.unlock("Lots & Lots of Trains!")
        $ renpy.jump(minigame_win)
    else:
        $ renpy.jump(minigame_loss)

label toytrainsgame_done:
    # Thing to do after the game if we reach here.
    pass
