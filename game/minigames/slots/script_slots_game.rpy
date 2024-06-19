init python:
    import math
    from itertools import cycle

    PLAY_PRICE = 10
    WIN_DOLLARS = 200
    SLOT_ON_SCREEN = 0.1

    POS_1 = (550, 495)
    POS_2 = (863, 495)
    POS_3 = (1177, 495)


    class SlotsGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.last_frame_st = 0.0
            self.on_screen_time = 0.0
            self.win = None

            self.dollars = 100

            self.items = {
                "gold": Image("minigames/slots/item_gold.png"),
                "no": Image("minigames/slots/item_no.png"),
                "poop": Image("minigames/slots/item_poop.png"),
                "rosen": Image("minigames/slots/item_rosen.png"),
                "tape": Image("minigames/slots/item_tape.png")
            }

            self.item_cycle = cycle(self.items.keys())

            self.lane_1 = None
            self.lane_2 = None
            self.lane_3 = None

            self.lane = 0
            self.hit = False

            self.bg = Image("minigames/slots/slots_machine_bg.png")
            self.fg = Image("minigames/slots/slots_machine_fg.png")

        def score(self) -> int:
            if self.lane_1 == "gold" and self.lane_2 == "gold" and self.lane_3 == "gold":
                # ALL GOLD = 100
                renpy.sound.play("minigames/slots/sfx_woohoo.mp3", channel=0)
                return 100
            elif (self.lane_1 == "gold" and self.lane_2 == "gold") or \
                (self.lane_2 == "gold" and self.lane_3 == "gold") or \
                (self.lane_3 == "gold" and self.lane_1 == "gold"):
                # TWO GOLD = 50
                renpy.sound.play("minigames/slots/sfx_tada.wav", channel=0)
                return 50
            elif self.lane_1 == "poop" and self.lane_2 == "poop" and self.lane_3 == "poop":
                # ALL POOP = LOSE 10
                renpy.sound.play("minigames/slots/sfx_fart.wav", channel=0)
                return -10
            elif self.lane_1 == "rosen" and self.lane_2 == "rosen" and self.lane_3 == "rosen":
                # ALL ROSEN = 50
                renpy.sound.play("minigames/slots/sfx_rosen_noice.mp3", channel=0)
                return 50
            elif (self.lane_1 == "rosen" and self.lane_2 == "rosen") or \
                (self.lane_2 == "rosen" and self.lane_3 == "rosen") or \
                (self.lane_3 == "rosen" and self.lane_1 == "rosen"):
                # TWO ROSEN = 25
                renpy.sound.play("minigames/slots/sfx_rosen_pop.mp3", channel=0)
                return 25
            else:
                renpy.sound.play("minigames/slots/sfx_gamblecore_awwdangit.mp3", channel=0)
                return 0


        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            dt = st - self.last_frame_st
            r = renpy.Render(1920, 1080)

            # BG
            bg_renderer = renpy.load_image(self.bg)
            r.blit(bg_renderer, (0, 0))

            if self.lane == 0:
                if self.hit:
                    self.dollars -= PLAY_PRICE
                    self.lane += 1
            elif self.lane == 1:
                self.on_screen_time += dt
                if self.on_screen_time > SLOT_ON_SCREEN:
                    self.lane_1 = next(self.item_cycle)
                    self.on_screen_time = 0.0
                if self.hit:
                    self.lane += 1
            elif self.lane == 2:
                self.on_screen_time += dt
                if self.on_screen_time > SLOT_ON_SCREEN:
                    self.lane_2 = next(self.item_cycle)
                    self.on_screen_time = 0.0
                if self.hit:
                    self.lane += 1
            elif self.lane == 3:
                self.on_screen_time += dt
                if self.on_screen_time > SLOT_ON_SCREEN:
                    self.lane_3 = next(self.item_cycle)
                    self.on_screen_time = 0.0
                if self.hit:
                    self.lane += 1
            else:
                if self.hit:
                    self.dollars += self.score()
                    self.lane = 0
                    self.lane_1 = None
                    self.lane_2 = None
                    self.lane_3 = None

            # Render spinnies
            if self.lane_1:
                lane_1_renderer = renpy.load_image(self.items[self.lane_1])
                r.blit(lane_1_renderer, POS_1)
            if self.lane_2:
                lane_2_renderer = renpy.load_image(self.items[self.lane_2])
                r.blit(lane_2_renderer, POS_2)
            if self.lane_3:
                lane_3_renderer = renpy.load_image(self.items[self.lane_3])
                r.blit(lane_3_renderer, POS_3)

            # FG
            fg_renderer = renpy.load_image(self.fg)
            r.blit(fg_renderer, (0, 0))

            # Info
            middle_renderer = renpy.render(Text("Press [[SPACE] to spin!", size=72), 1920, 1080, st, at)
            r.blit(middle_renderer, (650, 1000))
            money_renderer = renpy.render(Text(f"${self.dollars}\nGOAL: ${WIN_DOLLARS}", color = "#00FF00", size=72), 1920, 1080, st, at)
            r.blit(money_renderer, (50, 50))

            # Clear hit flag
            if self.hit:
                self.hit = False

            # Win/Lose
            if self.dollars <= 0:
                self.win = False
            if self.dollars >= WIN_DOLLARS:
                self.win = True

            self.last_frame_st = st
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
    play music "<loop 0>minigames/slots/game_corner.mp3" if_changed
    play sound "minigames/slots/sfx_gamblecore_letsgogambling.mp3"
    call screen slotsgame
    $ quick_menu = True
    window show

    if _return:
        stop music fadeout 2.0
        $ renpy.jump(minigame_win)
    else:
        stop music fadeout 2.0
        $ renpy.jump(minigame_loss)
