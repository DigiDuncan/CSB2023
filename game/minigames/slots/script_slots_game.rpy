init python:
    import math
    from itertools import cycle

    PLAY_PRICE = 10
    WIN_DOLLARS = 300


    class SlotsGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

            self.dollars = 100

            self.items = {
                "item": Image("minigames/slots/item_.png")
            }

            self.lane = 0
            self.hit = False

            self.bg = Image("minigames/slots/slots_machine_bg.png")
            self.fg = Image("minigames/slots/slots_machine_fg.png")

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # BG
            bg_renderer = renpy.load_image(self.bg)
            r.blit(bg_renderer, (0, 0))

            if self.lane == 0:
                if self.hit:
                    self.dollars -= PLAY_PRICE
                    self.lane += 1
            elif self.lane == 1:
                ...
            elif self.lane == 2:
                ...
            elif self.lane == 3:
                ...
            else:
                self.lane = 0

            # FG
            fg_renderer = renpy.load_image(self.fg)
            r.blit(fg_renderer, (0, 0))

            # Info
            middle_renderer = renpy.render(Text("Press [[SPACE] to spin!", size=72), 1920, 1080, st, at)
            r.blit(middle_renderer, (900, 1000))

            # Clear hit flag
            if self.hit:
                self.hit = False

            # Win/Lose
            if self.dollars <= 0:
                self.win = False
            if self.dollars >= WIN_DOLLARS:
                self.win = True

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_END and preferences.developer_mode:
                    self.win = 1
                elif ev.key == pygame.K_SPACE:
                    self.hit = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [self.bg, self.fg] # Assets needed to load


screen slotsgame:
    default slotsgame = SlotsGameDisplayable()
    # Add a background or any static images here.
    add slotsgame

label minigame_slots:
    window hide
    $ quick_menu = False
    call screen slotsgame
    $ quick_menu = True
    window show

    if _return:
        stop music fadeout 2.0
        $ renpy.jump(minigame_win)
    else:
        stop music fadeout 2.0
        $ renpy.jump(minigame_loss)
