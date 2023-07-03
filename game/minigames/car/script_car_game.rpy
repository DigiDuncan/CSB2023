init python:

    current_lane = 0

    class CarGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            self.win = False
            self.billycar = Image("minigames/car/billy_car.png")
            self.ufo = Image("minigames/car/joj_ufo.png")
            self.laser = Image("minigames/car/laser.png")

        def render(self, width, height, st, at):
            r = renpy.Render(1920, 1080)
            if(current_lane==0):
                r.blit(renpy.load_image(self.billycar), (640, 500))
            elif(current_lane==1):
                r.blit(renpy.load_image(self.billycar), (1280, 500))
            else:
                r.blit(renpy.load_image(self.billycar), (1920, 500))

            renpy.redraw(self, 0)
            return r
            
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == "K_LEFT":
                current_lane-=1
                if current_lane == -1:
                    current_lane = 0
                renpy.restart_interaction()
            if ev.type == pygame.KEYDOWN and ev.key == "K_RIGHT":
                current_lane+=1
                if current_lane == 3:
                    current_lane = 2
                renpy.restart_interaction()
            if ev.type == pygame.KEYDOWN and ev.key == "K_END":
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
    pause
