init python:
    import math

    # Graphics
    LANE_X = [671, 880, 1107]
    CAR_Y = 770
    UFO_Y = 100
    SWAY_PERIOD = 5
    SWAY_DISTANCE = 20

    # Difficulty
    MOVE_FREQUENCY = 5
    TELEGRAPH_DELAY = 1
    TELEGRAPH_TIME = 0.5
    DANGER_TIME = 1.0
    FIRE_COUNT = 21

    class CarGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.win = None
            self.billycar = Image("minigames/car/billy_car.png")
            self.ufo = Image("minigames/car/joj_ufo.png")
            self.laser = Image("minigames/car/laser.png")
            self.laser_ball = Image("minigames/car/energy_ball.png")

            self.start_time = None
            self.round_timer = -3  # Time since last UFO move
            self.enemy_lane = 0
            self.current_lane = 0

            self.danger_lane = None
            self.fires = 0
            self.played_charge = False
            self.played_fire = False

            self.entered = False
            self.exited = False

        def render(self, width, height, st, at):
            global MOVE_FREQUENCY, TELEGRAPH_DELAY
            if self.start_time is None:
                self.start_time = st

            r = renpy.Render(1920, 1080)

            car_renderer = renpy.load_image(self.billycar)
            ufo_renderer = renpy.load_image(self.ufo)
            if self.fires < 10:
                laser_renderer = renpy.load_image(self.laser)
            else:
                laser_displayable = renpy.displayable(self.laser)
                t = Transform(laser_displayable, matrixcolor = TintMatrix("#f00"))
                laser_renderer = renpy.render(t, 1920, 1080, st, at)
            if not self.entered:
                if (st - self.start_time < 3.5):
                    curr_y = ease_linear(-UFO_Y, UFO_Y, self.start_time+2, self.start_time+3.5, st)
                    r.blit(ufo_renderer, (LANE_X[self.enemy_lane], curr_y))
                else:
                    self.entered = True
            elif self.exited:
                # Exit logic
                if (st - self.round_timer < 3.5):
                    curr_y = ease_linear(UFO_Y, -UFO_Y, self.round_timer+2, self.round_timer+3.5, st)
                    r.blit(ufo_renderer, (LANE_X[self.enemy_lane], curr_y))
                else:
                    self.win = True
                    renpy.timeout(0)
            else:
            # ENEMY LOGIC
                telegraph_start = self.round_timer + TELEGRAPH_TIME
                telegraph_cutoff = telegraph_start  + TELEGRAPH_DELAY
                danger_cutoff = telegraph_cutoff + DANGER_TIME
                # Move enemy
                if st - self.round_timer > MOVE_FREQUENCY:
                    renpy.sound.play("minigames/car/joj_loop.wav", channel=0)
                    #Fire logic
                    self.enemy_lane = renpy.random.randint(0, 2)
                    self.fires += 1
                    self.round_timer = st
                    MOVE_FREQUENCY -= 0.15
                    if self.fires == 10:
                        TELEGRAPH_DELAY = 0.5
                    self.played_charge = False
                    self.played_fire = False

                # Danger period
                if telegraph_cutoff < st < danger_cutoff:
                    self.danger_lane = self.enemy_lane
                    if not self.played_fire:
                        renpy.sound.play("minigames/car/gaster_blast.wav", channel=0)
                        self.played_fire = True
                    r.blit(laser_renderer, (LANE_X[self.enemy_lane] - 15, UFO_Y+50))
                current_ufo_x = LANE_X[self.enemy_lane] + math.sin(st * SWAY_PERIOD) * SWAY_DISTANCE
                # Starting to telegraph

                # Telegraphing period
                if telegraph_start < st < telegraph_cutoff:
                    if not self.played_charge:
                        renpy.sound.play("minigames/car/gaster_charge.wav", channel=0)
                        self.played_charge = True
                    # Logic for the energy ball
                    laser_ball_displayable = renpy.displayable(self.laser_ball)
                    l = (st - telegraph_start) / (telegraph_cutoff - telegraph_start)
                    t = Transform(laser_ball_displayable, xysize=(l, l), anchor=(0.5, 0.5))
                    if self.fires >= 10:
                        t.matrixcolor = TintMatrix("#f00")
                    w = 180
                    h = 180
                    laser_ball_renderer = renpy.render(t, w, h, st, at)
                    xo = (abs(l-1) * 180) / 2
                    yo = (abs(l-1) * 180) / 2
                    r.blit(laser_ball_renderer, ((LANE_X[self.enemy_lane] + xo)-25, UFO_Y + yo))

                    r.blit(ufo_renderer, (LANE_X[self.enemy_lane], UFO_Y))
                else:
                    r.blit(ufo_renderer, (current_ufo_x, UFO_Y))

                # No more danger
                if danger_cutoff < st:
                    self.danger_lane = None

            # PLAYER LOGIC
            if self.current_lane == self.danger_lane:
                self.win = False
                renpy.timeout(0)
            if self.fires >= FIRE_COUNT:
                self.exited = True

            r.blit(car_renderer, (LANE_X[self.current_lane], CAR_Y))

            renpy.redraw(self, 0)
            return r
            
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_LEFT:
                self.current_lane -= 1
                if self.current_lane == -1:
                    self.current_lane = 0
                renpy.restart_interaction()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RIGHT:
                self.current_lane += 1
                if self.current_lane == 3:
                    self.current_lane = 2
                renpy.restart_interaction()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [self.billycar, self.ufo, self.laser]


screen cargame:
    default cargame = CarGameDisplayable()
    add "minigames/car/background.png" at transform:
        yanchor 0.5 ypos 0.0
        linear 1.0 ypos 1.0
        repeat
    add cargame

label play_cargame:
    window hide
    $ quick_menu = False
    call screen cargame
    $ quick_menu = True
    window show

    if _return == True:
        arceus "GG, dipshit."
        jump after_ufo
    else:
        arceus "You failed. What the fuck."
        jump iowa

label cargame_done:
    show arceus
    arceus ":3"
