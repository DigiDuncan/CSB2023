init python:
    import math
    import pygame

    class ControllerTestDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

            self.controller_count = pygame.joystick.get_count()

            if persistent.controller_id > self.controller_count - 1:
                persistent.controller_id = 0

            self.controller_names = []
            pygame.joystick.init()

            self.joysticks = []
            for i in range(self.controller_count):
                j = pygame.joystick.Joystick(i)
                j.init()
                self.joysticks.append(j)
                self.controller_names.append(j.get_name())

            self.controller_base_img = Image("minigames/controllertest/base.png")
            self.image_pos = (594, 484)

            self.hats = ["left", "right", "up", "down"]
            self.hat_imgs = {hat: Image(f"minigames/controllertest/dpad_{hat}.png") for hat in self.hats}
            self.buttons = ["a", "b", "x", "y", "l1", "r1",  "start", "select", "l3", "r3"]
            self.button_imgs = {button: Image(f"minigames/controllertest/{button}.png") for button in self.buttons}

        @property
        def current_controller(self) -> str:
            return self.controller_names[persistent.controller_id] if self.controller_count else "No Controller"

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            if self.controller_count:
                bg = Solid("#111")
                bg_renderer = renpy.render(bg, 1920, 1080, st, at)
                r.blit(bg_renderer, (0, 0))

                base_renderer = renpy.load_image(self.controller_base_img)
                r.blit(base_renderer, self.image_pos)

                joystick = self.joysticks[persistent.controller_id]
                for i, button in enumerate(self.buttons):
                    v = joystick.get_button(i)
                    if v:
                        button_renderer = renpy.load_image(self.button_imgs[button])
                        r.blit(button_renderer, self.image_pos)
                hat_x, hat_y = joystick.get_hat(0)
                if hat_x == -1:
                    left_renderer = renpy.load_image(self.hat_imgs["left"])
                    r.blit(left_renderer, self.image_pos)
                if hat_x == 1:
                    right_renderer = renpy.load_image(self.hat_imgs["right"])
                    r.blit(right_renderer, self.image_pos)
                if hat_y == -1:
                    down_renderer = renpy.load_image(self.hat_imgs["down"])
                    r.blit(down_renderer, self.image_pos)
                if hat_y == 1:
                    up_renderer = renpy.load_image(self.hat_imgs["up"])
                    r.blit(up_renderer, self.image_pos)

                t = Text(self.current_controller, size=72, textalign=0.5)
                middle_renderer = renpy.render(t, 1920, 1080, st, at)
                r.blit(middle_renderer, (1920 / 2 - (middle_renderer.width / 2), 200))
            else:
                nc_txt = "No controller detected.\nPlug your controller in, restart the game, and try again."
                nc_txt_render = renpy.render(Text(nc_txt, color = "#FFFFFF", size = 50, text_align = 0.5), 1920, 500, st, at)
                r.blit(nc_txt_render, (475, 500))

            # Do some fancy things here!

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_EQUALS:
                persistent.controller_id = min(self.controller_count - 1, persistent.controller_id + 1)
            elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_MINUS:
                persistent.controller_id = max(0, persistent.controller_id - 1)
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load


screen controllertest():
    default controllertest = ControllerTestDisplayable()
    # Add a background or any static images here.
    add controllertest

    # TODO: we need a way to return to the previous menu that is compatible with all types of controls. i got nothing - tate
    textbutton "Return to Extras":
        xoffset 25 yoffset 950
        action ShowMenu("category_welcome")
    textbutton "Main Menu":
        xoffset 25 yoffset 1000
        action Return()

label play_controllertest:
    window hide
    $ quick_menu = False
    call screen controllertest
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label controllertest_done:
    # Thing to do after the game if we reach here.
    pass
