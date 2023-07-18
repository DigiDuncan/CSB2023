init python:
    import math

    # Constants
    SHARPENER_MOUTH = 1430
    DIGI_SCORE = 270
    MAX_PENCIL_LENGTH = 20.0
    SHARPEN_AMOUNT = 0.5
    GAME_LENGTH = 60
    PENCIL_WIDTH_PX = int(41.2 * 20)
    ERASER_SIZE = 200
    PENCIL_LIMIT = 15

    class PencilGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            # I'm using a boolean statement here, Q needing to be pressed is True, E needing to be pressed is false. Reason for this is just so I can be lazy.
            self.current_key = True
            # All pencils start at 20 cm, it will be a floating point, unless told otherwise
            self.current_pencil_length = MAX_PENCIL_LENGTH
            self.start_time = None
            self.win = None
            self.score = 0
            self.pencil_sharpener = Image("minigames/pencil/sharpener.png")
            self.current_pencil = Image("minigames/pencil/pencil.png")
            self.keyboard_q = Image("minigames/pencil/key_q.png")
            self.keyboard_e = Image("minigames/pencil/key_e.png")
            self.red_x = Image("minigames/pencil/red_x.png")

            self.pencils = 0
            self.lock_out_time = None

        def render(self, width, height, st, at):
            # Set start time if it isn't (frame 0)
            if self.start_time is None:
                self.start_time = st
            
            current_time = st - self.start_time
            # Render object we return at the end
            r = renpy.Render(1920, 1080)

            # Load assets
            q_keyboard_renderer = renpy.load_image(self.keyboard_q)
            e_keyboard_renderer = renpy.load_image(self.keyboard_e)
            red_x_renderer = renpy.load_image(self.red_x)

            # Main game loop
            if self.current_pencil_length < 0 and not self.lock_out_time:
                self.lock_out_time = current_time + 3

            #Visuals for making the pencil
            pencil_size = int(lerp(ERASER_SIZE, PENCIL_WIDTH_PX, self.current_pencil_length / MAX_PENCIL_LENGTH))
            pencil_crop = Crop((0, 0, pencil_size, 50), self.current_pencil)
            pencil_renderer = renpy.render(pencil_crop, 1920, 1080, st ,at)
            r.blit(pencil_renderer, (SHARPENER_MOUTH - pencil_size, 475))

            # Current state of the pencil sharpener
            sharpener_displayable = renpy.displayable(self.pencil_sharpener)
            t = Transform(sharpener_displayable, zoom = 0.35)
            sharpener_renderer = renpy.render(t, 475, 597, st, at)
            r.blit(sharpener_renderer, (1300, 300))

            # Lockout logic
            if self.lock_out_time and current_time < self.lock_out_time:
                r.blit(red_x_renderer, (1200, 300))
            elif self.lock_out_time and current_time >= self.lock_out_time:
                self.lock_out_time = None
                self.pencils += 1
                self.current_pencil_length = MAX_PENCIL_LENGTH

            # Rendering in the score
            score_renderer = renpy.render(Text(str(self.score) + " cm", color = "#0000FF", size = 100), 500, 100, st, at)
            r.blit(score_renderer, (1600, 0))

            # Rendering in the timer
            if not (GAME_LENGTH - current_time < 0):
                time_renderer = renpy.render(Text(str(GAME_LENGTH - math.ceil(current_time)), color = "#FF0000", size = 144), 150, 100, st, at)
                r.blit(time_renderer, (50, 0))
            else:
                time_renderer = renpy.render(Text("0", color = "#FF0000", size = 144), 100, 100, st, at)
                r.blit(time_renderer, (50, 0))
            count_renderer = renpy.render(Text(str(PENCIL_LIMIT - self.pencils) + " pencils remaining", color = "#FF0000", size = 72), 1000, 100, st, at)
            r.blit(count_renderer, (50, 125))

            # Check if time's up
            if (GAME_LENGTH - current_time < 0) or (self.pencils >= PENCIL_LIMIT):
                self.win = self.score
                renpy.timeout(0)

            renpy.redraw(self, 0)
            return r
            
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and (ev.key == pygame.K_q or ev.key == pygame.K_e):
                if ev.key == pygame.K_q and self.current_key and not self.lock_out_time:
                    # Progress the pencil.
                    self.pencil_sharpener = Image("minigames/pencil/sharpener2.png")
                    self.current_pencil_length -= SHARPEN_AMOUNT
                    self.current_key = False
                    if self.current_pencil_length >= 0:
                        self.score += SHARPEN_AMOUNT
                elif ev.key == pygame.K_e and not self.current_key and not self.lock_out_time:
                    # Progress the pencil
                    self.pencil_sharpener = Image("minigames/pencil/sharpener.png")
                    self.current_pencil_length -= SHARPEN_AMOUNT
                    self.current_key = True
                    if self.current_pencil_length >= 0:
                        self.score += SHARPEN_AMOUNT
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and not self.lock_out_time:
                # New pencil
                self.current_pencil_length = MAX_PENCIL_LENGTH
                self.pencils += 1
            if self.win is not None:
                return self.win

        def visit(self):
            return [self.pencil_sharpener, self.current_pencil, self.keyboard_q, self.keyboard_e]


screen pencilgame:
    default pencilgame = PencilGameDisplayable()
    add "minigames/pencil/stage.png"
    add "minigames/pencil/table.png" at transform:
        yalign 1.0
    # add "minigames/pencil/sharpener.png" at transform:
    #     zoom 0.35
    #     xalign 0.95
    #     yalign 0.68
    text "Press [[SPACE] to move on to the next pencil!":
        xalign 0.5
        yalign 0.0625
        size 60
        color "AAAAAA"
    add pencilgame

label play_pencilgame:
    window hide
    $ quick_menu = False
    call screen pencilgame
    $ quick_menu = True
    window show

    if _return > DIGI_SCORE:
        jump win_pencil
    else:
        arceus "You dumb foreskin."
        jump play_pencilgame

label pencilgame_done:
    show arceus
    arceus ":3"
