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
    FIRE_COUNT = 20

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

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            r = renpy.Render(1920, 1080)

            car_renderer = renpy.load_image(self.billycar)
            ufo_renderer = renpy.load_image(self.ufo)
            laser_renderer = renpy.load_image(self.laser)

            # ENEMY LOGIC
            telegraph_start = self.round_timer + TELEGRAPH_TIME
            telegraph_cutoff = telegraph_start  + TELEGRAPH_DELAY
            danger_cutoff = telegraph_cutoff + DANGER_TIME
            # Move enemy
            if st - self.round_timer > MOVE_FREQUENCY:
                #Fire logic
                self.enemy_lane = renpy.random.randint(0, 2)
                self.fires += 1
                self.round_timer = st

            # Danger period
            if telegraph_cutoff < st < danger_cutoff:
                self.danger_lane = self.enemy_lane
                r.blit(laser_renderer, (LANE_X[self.enemy_lane] - 15, UFO_Y+99))

            current_ufo_x = LANE_X[self.enemy_lane] + math.sin(st * SWAY_PERIOD) * SWAY_DISTANCE
            # Telegraphing period
            if telegraph_start < st < telegraph_cutoff:
                # TODO: Better telegraph animation
                r.blit(ufo_renderer, (LANE_X[self.enemy_lane], UFO_Y))
                # Logic for the energy ball
                laser_ball_displayable = renpy.displayable(self.laser_ball)
                t = Transform(laser_ball_displayable, zoom=st*((st-telegraph_start)/(telegraph_cutoff-telegraph_start)))

                laser_ball_renderer = renpy.render(t, 180, 180, st, at)
                #laser_ball_renderer.zoom(st*((st-telegraph_start)/(telegraph_cutoff-telegraph_start)), st*((st-telegraph_start)/(telegraph_cutoff-telegraph_start)))
                r.blit(laser_ball_renderer, (LANE_X[self.enemy_lane]-(180/2) - 15, (UFO_Y+99)-(180/2)))

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
                self.win = True
                renpy.timeout(0)

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
    else:
        arceus "You failed at a WIP game. What the fuck."

label cargame_done:
    show arceus
    arceus ":3"
