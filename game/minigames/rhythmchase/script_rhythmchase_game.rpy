init python:
    import math

    class RhythmChaseGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
                      
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # Do some fancy things here!

            # Temporary

            temp_txt = "Hi, this doesn't exist yet, but the outcome will affect the ending.\nPress END to \"win\", Space to \"lose.\""
            temp_txt_render = renpy.render(Text(temp_txt, color = "#FFFFFF", size = 50), 1920, 100, st, at)
            r.blit(temp_txt_render, (16, 16))

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            # temporary
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                self.win = False

            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load

screen rhythmchasegame():
    default rhythmchasegame = RhythmChaseGameDisplayable()
    # Add a background or any static images here.
    add "minigames/rhythmchase/bg.png"
    add rhythmchasegame

label play_rhythmchase_game:
    window hide
    $ quick_menu = False
    call screen rhythmchasegame
    $ quick_menu = True
    window show

    if _return == True:
        $ achievement_manager.unlock("beat_lupin") 
        $ renpy.jump(minigame_win)
    else:
        $ renpy.jump(minigame_loss)

label rhythmchasegame_done:
    # Thing to do after the game if we reach here.
    pass
