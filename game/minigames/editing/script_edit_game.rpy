init python:
    import math

    TOTAL_ROUNDS = 20
    SCISSOR_SPEED = 800 # px/s
    WIN_PERCENTAGE = 0.75
    SCISSOR_WIDTH = 158
    START_BOX_WIDTH = 200
    BOX_SHRINK_FACTOR = 2

    class EditGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None
            self.started = False
            self.three_played = False
            self.two_played = False
            self.one_played = False
            self.scissors = Image("minigames/editing/scissors.png")
            self.hit_width = START_BOX_WIDTH
            self.hit_position = START_BOX_WIDTH
            self.scissors_place = 1000
            self.successes = 0
            self.attempts = 0

            self.last_frame_time = 0
            self.scissors_direction = False

            self.hit = False
            self.cut_positions = []

            self.control_pressed = False

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
                self.hit_position = renpy.random.randint(self.hit_width, 1920 - self.hit_width)
                self.last_frame_time = st
                dt = 1 / 60
            else:
                dt = st - self.last_frame_time
            current_time = st - self.start_time
            r = renpy.Render(1920, 1080)

            #Entry point
            if not self.started:
                if 0 < current_time < 1:
                    # Display 3
                    if not self.three_played:
                        renpy.sound.play("minigames/editing/sfx_count_beep.ogg")
                        self.three_played = True
                    countdown_renderer = renpy.render(Text("3", color = "FF0000", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif 1 < current_time < 2:
                    # Display 2
                    if not self.two_played:
                        renpy.sound.play("minigames/editing/sfx_count_beep.ogg")
                        self.two_played = True
                    countdown_renderer = renpy.render(Text("2", color = "FFFF00", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif 2 < current_time < 3:
                    # Display 1
                    if not self.one_played:
                        renpy.sound.play("minigames/editing/sfx_count_beep.ogg")
                        self.one_played = True
                    countdown_renderer = renpy.render(Text("1", color = "00FF00", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif current_time > 3:
                    # Yell Go at the player
                    renpy.sound.play("minigames/editing/sfx_start_beep.ogg")
                    self.started = True

            # Hit the space bar
            if self.hit:
                # In box
                if self.hit_position <= self.scissors_place <= self.hit_position + self.hit_width:
                    self.successes += 1
                    self.hit_width = int(lerp(START_BOX_WIDTH, START_BOX_WIDTH / BOX_SHRINK_FACTOR, self.successes / TOTAL_ROUNDS))
                else:
                    renpy.sound.play("minigames/editing/sfx_ohno.ogg", channel="sound")
                self.attempts += 1
                self.hit_position = renpy.random.randint(self.hit_width, 1920 - self.hit_width)
                self.hit = False
                self.cut_positions.append(self.scissors_place)
                renpy.sound.play("minigames/editing/sfx_cut.ogg", channel="sound2")

            # Move scissors back and forth
            if self.scissors_direction:
                self.scissors_place += (SCISSOR_SPEED * dt)
                if self.scissors_place >= 1920:
                    self.scissors_direction = False
            else:
                self.scissors_place -= (SCISSOR_SPEED * dt)
                if self.scissors_place < 0:
                    self.scissors_direction = True

            # Cuts
            for p in self.cut_positions:
                rr = renpy.render(Solid("#313131", xysize = (2, 115)), 1920, 1080, st, at)
                r.blit(rr, (p, 454))
                rr = renpy.render(Solid("#FFFFFF4D", xysize = (2, 115)), 1920, 1080, st, at)
                r.blit(rr, (p + 2, 454))

            # Green hitbox rectangle visual
            rectangle_renderer = renpy.render(Solid("#00FF00", xysize = (self.hit_width, 115)), 1920, 1080, st, at)
            r.blit(rectangle_renderer, (self.hit_position, 454))

            # Scissor visual
            scissor_renderer = renpy.load_image(self.scissors)
            r.blit(scissor_renderer, (self.scissors_place - (SCISSOR_WIDTH / 2), 154))

            # Score visual
            score_renderer = renpy.render(Text(str(self.successes) + " / " + str(TOTAL_ROUNDS), size=72), 1920, 1080, st, at)
            r.blit(score_renderer, (50, 950))
            left_renderer = renpy.render(Text(str(TOTAL_ROUNDS - self.attempts) + " cuts left!", size=72), 1920, 1080, st, at)
            r.blit(left_renderer, (50, 1000))
            middle_renderer = renpy.render(Text("Press [[SPACE] to cut!", size=72), 1920, 1080, st, at)
            r.blit(middle_renderer, (900, 1000))

            # Return if game over
            if self.attempts >= TOTAL_ROUNDS:
                self.win = self.successes / self.attempts

            renpy.redraw(self, 0)
            self.last_frame_time = st
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and self.started:
                if ev.key == pygame.K_SPACE:
                    self.hit = True
                if ev.key == pygame.K_LCTRL:
                    self.control_pressed = True
                if ev.key == pygame.K_k and self.control_pressed:
                    if not "editor" in persistent.unlocked_achievements:
                        chievos = (a for a in achievement_manager.achievements
                        if a == "editor")
                        renpy.show_screen("popup", next(chievos))
                        achievement_manager.unlock("editor", show_screen = False)
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LCTRL:
                    self.control_pressed = False
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END and preferences.developer_mode:
                self.win = 1
            if self.win is not None:
                return self.win

        def visit(self):
            return [self.scissors]

screen editgame():
    default editgame = EditGameDisplayable()
    # Add a background or any static images here.
    add "minigames/editing/bg.png"
    add editgame

label minigame_editing:
    window hide
    $ quick_menu = False
    play music supernova volume 0.25 if_changed
    $ persistent.heard.add("supernova")
    call screen editgame
    $ quick_menu = True
    window show

    if _return >= WIN_PERCENTAGE:
        stop music fadeout 2.0
        $ renpy.jump(minigame_win)
    else:
        stop music fadeout 2.0
        $ renpy.jump(minigame_loss)
