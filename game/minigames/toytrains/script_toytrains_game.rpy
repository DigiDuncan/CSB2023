init python:
    import math

    CS_TRAIN_HP = 3

    class Jig:
        def __init__(self):
            self.position = (0, 0)

        @property
        def x(self) -> int:
            return self.position[0]

        @x.setter
        def x(self, i: int):
            self.position = (i, self.position[1])

        @property
        def y(self) -> int:
            return self.position[1]

        @y.setter
        def y(self, i: int):
            self.position = (self.position[0], i)

        def pos(self, x, y) -> tuple[int, int]:
            return (x - self.position[0], y - self.position[1])

    class ToyTrainsGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.hp = CS_TRAIN_HP
            self.total_laps = 3
            self.current_lap = 1
            self.current_key = None
            
            self.bg = Image("minigames/toytrains/bg_do_not_resize.png")
            self.train_cs = Image("minigames/toytrains/train_cs.png")
            self.train_arceus = Image("minigames/toytrains/train_arceus.png")

            self.up = False
            self.left = False
            self.down = False
            self.right = False

            self.jig = Jig()
            self.jig.position = (2760, 1590)
            
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # Do some fancy things here!
            if self.up:
                self.jig.y -= 5
            if self.down:
                self.jig.y += 5
            if self.left:
                self.jig.x -= 5
            if self.right:
                self.jig.x += 5
            
            # Moving Backgound
            bg_displayable = renpy.displayable(self.bg)
            bg_transform = Transform(bg_displayable)
            bg_renderer = renpy.render(bg_transform, 0, 0, st, at)
            r.blit(bg_renderer, self.jig.pos(0, 0))
            
            # CS Train
            train_cs_displayable = renpy.displayable(self.train_cs)
            train_cs_transform = Transform(train_cs_displayable, zoom = 0.8)
            train_cs_renderer = renpy.render(train_cs_transform, 475, 597, st, at)
            r.blit(train_cs_renderer, self.jig.pos(4043, 2015))

            # Arc Train
            train_arceus_displayable = renpy.displayable(self.train_arceus)
            train_arceus_transform = Transform(train_arceus_displayable, zoom = 0.8)
            train_arceus_renderer = renpy.render(train_arceus_transform, 475, 597, st, at)
            r.blit(train_arceus_renderer, self.jig.pos(4338, 2015))
            
            ### Text Elements
            
            # Lap Counter
            laps_left_txt_render = renpy.render(Text("LAP: "+str(self.current_lap)+"/"+str(self.total_laps), color = "#FFFFFF", size = 72), 300, 100, st, at)
            r.blit(laps_left_txt_render, (16, 0))
            
            # HP
            hp_left_txt_render = renpy.render(Text("HP: "+str(self.hp), color = "#FFFFFF", size = 72), 300, 100, st, at)
            r.blit(hp_left_txt_render, (16, 60))
            
            
            # Temporary
            temp_txt = "Hi, this doesn't work yet.\nUse arrow keys to check out the map, at least.\nPress END to \"win\", Space to \"lose.\""
            temp_txt_render = renpy.render(Text(temp_txt, color = "#FFFFFF", size = 50), 1920, 100, st, at)
            r.blit(temp_txt_render, (16, 128))

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            # temporary
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                self.win = False
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_UP:
                self.up = True
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_LEFT:
                self.left = True
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_DOWN:
                self.down = True
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_RIGHT:
                self.right = True
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_UP:
                self.up = False
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT:
                self.left = False
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_DOWN:
                self.down = False
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT:
                self.right = False

            if self.win is not None:
                return self.win

        def visit(self):
            return [self.bg, self.train_cs, self.train_arceus] # Assets needed to load

screen toytrainsgame():
    default toytrainsgame = ToyTrainsGameDisplayable()
    # Add a background or any static images here.
    add "minigames/toytrains/bg_carpet.png"
    add toytrainsgame

label play_toytrains_game:
    window hide
    $ quick_menu = False
    play music hide_and_seek if_changed
    call screen toytrainsgame
    $ persistent.heard.add("hide_and_seek")
    $ quick_menu = True
    window show

    if _return == True:
        $ achievement_manager.unlock("trains_minigame")
        
        if CS_TRAIN_HP == 3:
            $ achievement_manager.unlock("trains_perfect")
        
        stop music fadeout 2.0
        
        $ renpy.jump(minigame_win)
    else:
        $ achievement_manager.unlock("trains_minigame")
        stop music fadeout 2.0
        
        $ renpy.jump(minigame_loss)

label toytrainsgame_done:
    # Thing to do after the game if we reach here.
    pass
