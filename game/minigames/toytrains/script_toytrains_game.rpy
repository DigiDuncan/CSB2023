init python:
    import math

    class ToyTrainsGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            
            self.train_cs = Image("minigames/toytrains/train_cs.png")
            self.train_arceus = Image("minigames/toytrains/train_arceus.png")
            
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # Do some fancy things here!
            
            # CS Train
            train_cs_displayable = renpy.displayable(self.train_cs)
            train_cs_transform = Transform(train_cs_displayable, zoom = 0.5)
            train_cs_renderer = renpy.render(train_cs_transform, 475, 597, st, at)
            r.blit(train_cs_renderer, (1300, 300))

            # Arc Train
            train_arceus_displayable = renpy.displayable(self.train_arceus)
            train_arceus_transform = Transform(train_arceus_displayable, zoom = 0.5)
            train_arceus_renderer = renpy.render(train_arceus_transform, 475, 597, st, at)
            r.blit(train_arceus_renderer, (1000, 300))

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
    add "minigames/toytrains/bg.png"
    
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
