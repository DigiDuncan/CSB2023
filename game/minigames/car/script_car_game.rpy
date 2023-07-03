init python:

    LANE_X = [671, 880, 1107]
    CAR_Y = 784
    UFO_Y = 99

    MOVE_FREQUENCY = 5
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
            telegraph_cutoff = self.round_timer + TELEGRAPH_TIME
            danger_cutoff = telegraph_cutoff + DANGER_TIME
            # Move enemy
            if st - self.round_timer > MOVE_FREQUENCY:
                #Fire logic
                self.enemy_lane = renpy.random.randint(0, 2)
                self.fires += 1
                self.round_timer = st

            # Telegraphing period
            if st < telegraph_cutoff:
                # TODO: Show telegraph animation
                pass

            # Danger period
            if telegraph_cutoff < st < danger_cutoff:
                self.danger_lane = self.enemy_lane
                r.blit(laser_renderer, (LANE_X[self.enemy_lane], UFO_Y))

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
            r.blit(ufo_renderer, (LANE_X[self.enemy_lane], UFO_Y))

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
                return self.win
            if self.win is not None:
                return self.win

        def visit(self):
            return [self.billycar, self.ufo, self.laser]


screen cargame:
    default cargame = CarGameDisplayable()
    add "minigames/car/background.png"
    add cargame

label play_cargame:
    window hide
    $ quick_menu = False
    call screen cargame
    $ quick_menu = True
    window show

    if _return == True:
        arceus "Gg, dipshit."
    else:
        arceus "You failed at a WIP game. What the fuck."

label cargame_done:
    show arceus
    arceus "I want to fucking die."
