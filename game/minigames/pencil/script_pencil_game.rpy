init python:
    import math

    # Constants
    SHARPENER_MOUTH = 1430
    DIGI_SCORE = 250
    MAX_PENCIL_LENGTH = 20.0
    SHARPEN_AMOUNT = 0.5
    GAME_LENGTH = 60 + 3
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
            self.started = False
            self.three_played = False
            self.two_played = False
            self.one_played = False
            self.go_played = False
            self.fail_played = False
            self.start_time = None
            self.win = None
            self.score = 0
            self.pencil_sharpener = Image("minigames/pencil/sharpener.png")
            if fun_value(FUN_VALUE_COMMON):
                self.current_pencil = Image("secret/pencilcolor.png")
            else:           
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
            red_x_renderer = renpy.load_image(self.red_x)

            #Entry point
            if not self.started:
                if 0 < current_time < 1:
                    # Display 3
                    if not self.three_played:
                        renpy.sound.play("minigames/pencil/sfx_smash_3.ogg")
                        self.three_played = True
                    countdown_renderer = renpy.render(Text("3", color="FF0000", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif 1 < current_time < 2:
                    # Display 2
                    if not self.two_played:
                        renpy.sound.play("minigames/pencil/sfx_smash_2.ogg")
                        self.two_played = True
                    countdown_renderer = renpy.render(Text("2", color="FFFF00", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif 2 < current_time < 3:
                    # Display 1
                    if not self.one_played:
                        renpy.sound.play("minigames/pencil/sfx_smash_1.ogg")
                        self.one_played = True
                    countdown_renderer = renpy.render(Text("1", color="00FF00", size=200), 1920, 1080, st, at)
                    r.blit(countdown_renderer, (960, 540))
                elif current_time > 3:
                    # Yell Go at the player
                    if not self.go_played:
                        renpy.sound.play("minigames/pencil/sfx_smash_go.ogg")
                        self.go_played = True
                    self.started = True

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
            sharpener_transform = Transform(sharpener_displayable, zoom = 0.35)
            sharpener_renderer = renpy.render(sharpener_transform, 475, 597, st, at)
            r.blit(sharpener_renderer, (1300, 300))

            # Lockout logic
            if self.lock_out_time and current_time < self.lock_out_time:
                r.blit(red_x_renderer, (1200, 300))
                if not self.fail_played:
                    renpy.sound.play("minigames/pencil/sfx_fail.ogg")
                    self.fail_played = True

            elif self.lock_out_time and current_time >= self.lock_out_time:
                self.lock_out_time = None
                self.pencils += 1
                self.current_pencil_length = MAX_PENCIL_LENGTH
                self.fail_played = False

            # Rendering in the score
            score_renderer = renpy.render(Text(str(self.score) + " cm", color = "#0000FF", size = 100), 500, 100, st, at)
            r.blit(score_renderer, (1600, 0))

            # Rendering in the timer
            if not current_time < 3:
                if not (GAME_LENGTH - current_time < 0):
                    time_renderer = renpy.render(Text(str(GAME_LENGTH - math.ceil(current_time)), color = "#FF0000", size = 144), 150, 100, st, at)
                    r.blit(time_renderer, (0, 0))
                else:
                    time_renderer = renpy.render(Text("0", color = "#FF0000", size = 144), 100, 100, st, at)
                    r.blit(time_renderer, (50, 0))
                
            # Render the remaining pencils
            count_renderer = renpy.render(Text(str(PENCIL_LIMIT - self.pencils) + " pencils remaining", color = "#FF0000", size = 72), 1000, 100, st, at)
            r.blit(count_renderer, (50, 125))

            # Render in the keys
            q_key_displayable = renpy.displayable(self.keyboard_q)
            q_key_transform = Transform(q_key_displayable, alpha = 1.0 if self.current_key else 0.33, zoom = 0.5)
            q_key_renderer = renpy.render(q_key_transform, 1920, 1080, st, at)
            r.blit(q_key_renderer, (600, 780))

            e_key_displayable = renpy.displayable(self.keyboard_e)
            e_key_transform = Transform(e_key_displayable, alpha = 1.0 if not self.current_key else 0.33, zoom = 0.5)
            e_key_renderer = renpy.render(e_key_transform, 1920, 1080, st, at)
            r.blit(e_key_renderer, (1220, 780))

            # Check if time's up or pencils out
            if (GAME_LENGTH - current_time < 0) or (self.pencils >= PENCIL_LIMIT):
                self.win = self.score
                renpy.timeout(0)

            renpy.redraw(self, 0)
            return r
            
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and self.started:
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
                elif ev.key == pygame.K_END and preferences.developer_mode:
                    self.win = DIGI_SCORE + 1
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE and not self.lock_out_time:
                # New pencil
                self.current_pencil_length = MAX_PENCIL_LENGTH
                self.pencils += 1
            if self.win is not None:
                return self.win

        def visit(self):
            return [self.pencil_sharpener, self.current_pencil, self.keyboard_q, self.keyboard_e]


screen pencilgame():
    default pencilgame = PencilGameDisplayable()
    add "minigames/pencil/stage.png"
    add "minigames/pencil/table.png" at transform:
        yalign 1.0
    text "Press [[SPACE] to move on to the next pencil!":
        xalign 0.5
        yalign 0.0625
        size 60
        color "AAAAAA"
    add pencilgame

label minigame_pencil:
    window hide
    $ quick_menu = False
    play music rude_buster volume 0.5 if_changed
    $ persistent.heard.add("Rude Buster - Toby Fox")
    call screen pencilgame
    stop music
    $ quick_menu = True
    window show

    if _return >= 300:
        $ achievement_manager.unlock("Pencilovania")
    if archack:
        if _return > (DIGI_SCORE - 70):
            $ achievement_manager.unlock("Pencil Sharpening Day!")
            $ renpy.jump(minigame_win)
        else:
            $ renpy.jump(minigame_loss)
    else:
        if _return > DIGI_SCORE:
            $ achievement_manager.unlock("Pencil Sharpening Day!")
            $ renpy.jump(minigame_win)
        else:
            $ renpy.jump(minigame_loss)

label pencilgame_done:
    show arceus
    arceus ":3"
