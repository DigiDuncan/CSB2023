init python:

    LANE_X = [671, 880, 1107]
    CAR_Y = 784
    UFO_Y = 99
    JOJ_FREQUENCY = 5

    class CarGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.win = False
            self.billycar = Image("minigames/car/billy_car.png")
            self.ufo = Image("minigames/car/joj_ufo.png")
            self.laser = Image("minigames/car/laser.png")

            self.start_time = None
            self.joj_timer = 0  # Time since last UFO move
            self.enemy_lane = 0
            self.current_lane = 0

        def render(self, width, height, st, at):
            if self.start_time = None:
                self.start_time = st

            r = renpy.Render(1920, 1080)
            if st - self.joj_timer > JOJ_FREQUENCY:
                #Fire logic
                joj_timer = st

            r.blit(renpy.load_image(self.billycar), (LANE_X[self.current_lane], CAR_Y))
            r.blit(renpy.load_image(self.ufo), (LANE_X[self.enemy_lane], UFO_Y))

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

    if _return == "win":
        arceus "Gg, dipshit."
    else:
        arceus "You failed at a WIP game. What the fuck."

label cargame_done:
    show arceus
    arceus "I want to fucking die."
