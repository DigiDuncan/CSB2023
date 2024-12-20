# TODO: this is gonna be a clone of UFO game except harder and uh i'd like it to read a clone hero chart for timing only
# instead of hitting notes you'd be dodging projectiles to the beat
# the position is still somewhat randomly generated but the timing should be read from a file
# CS' position should be tracked, give tate the appearance of ACTUALLY trying to target him
# no the chart does not exist yet oops
# also there are five lanes now
# these sections of the song should be charted (approximate):
# 0m32s to 1m11s (shoot 1 projectile)
# 1m30s to 1m48s (shoot 2 projectiles)
# 1m59s to 2m07s (shoot 3 projectiles but one has a chance of being a genergy to restore health.)
# 2m18s to 2m40s (shoot 4 projectiles, it's a bit faster, increased genergy chance)
# 2m59s to 3m47s (shoot 4 projectiles but since this section is very fast, even higher genergy chance)
# when the metal pipe hits, cut the music, i have a cutscene planned
# music position 22.8 to 32.381 seconds is intro
# 32.381, tate starts blasting IMMEDIATELY on that first drop
# on second thought maybe no healing items depending on how well we can balance difficulty w damage

# TODO: CS is off-center and lane math needs totally redone

init python:
    import math
    import store

    # Graphics
    # TODO: these lanes are no longer correct, and also we need to adjust the math on projectiles since the highway is angled now
    PT_LANE_X = [445, 670, 885, 1100, 1315]
    CS_Y = 800
    TATE_Y = 465
    SWAY_PERIOD = 1
    SWAY_DISTANCE = 10

    # Difficulty
    # TODO: i doubt any of this is staying once it can read the CH chart
    # i just need the battle to last long enough to test my timings
    MOVE_FREQUENCY = 2.5
    TELEGRAPH_DELAY = 1
    TELEGRAPH_TIME = 0.5
    DANGER_TIME = 0.05
    FIRE_COUNT = 61

    # Disable pause menu because it'll ruin audio sync
    # TODO: also disable controller bindings
    if 'K_ESCAPE' in config.keymap:
        config.keymap['game_menu'].remove('K_ESCAPE')
    if 'mouseup_3' in config.keymap:
        config.keymap['game_menu'].remove('mouseup_3')
    renpy.clear_keymap_cache()

    class PerfectTateGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            # TODO: besides replacing the assets, the "laser" needs to be a small projectile instead
            # no idea how the hitbox will work

            self.win = None

            self.cs = renpy.get_registered_image("cs_run")
            self.tate = Image("minigames/perfecttate/perfecttate_small.png")
            self.laser = Image("minigames/perfecttate/laser.png")
            self.laser_ball = Image("minigames/perfecttate/energy_ball.png")
            self.arrows = Image("minigames/perfecttate/arrows.png")

            self.start_time = None
            self.round_timer = -3  # Time since last Tate move
            self.enemy_lane = 2
            self.current_lane = 2

            self.danger_lane = None
            self.fires = 0
            self.played_charge = False
            self.played_fire = False

            self.entered = False
            self.exited = False

            self.health = 100

            self.tate_last_move = 0
            self.tate_move_time = 0
            self.tate_last_x = 0

        def render(self, width, height, st, at):
            # Set start time if it isn't (frame 0)
            if self.start_time is None:
                self.start_time = st
                # Difficulty reset
                global MOVE_FREQUENCY, TELEGRAPH_DELAY
                MOVE_FREQUENCY = 5
                TELEGRAPH_DELAY = 1

            # Render object we return at the end
            r = renpy.Render(1920, 1080)

            # Load players
            cs_renderer = renpy.render(self.cs, self.current_lane, CS_Y, st, at)
            tate_renderer = renpy.load_image(self.tate)
            arrow_renderer = renpy.load_image(self.arrows)

            # TODO: it's also a long shot but it might be cool if the heart can beat with the bpm of the song
            health_renderer = renpy.render(Fixed("/minigames/perfecttate/heart.png", Text(str(self.health), size=69, xanchor=0.5, yanchor=0.5, xalign=0.5, yalign=0.4, text_align=0.5), xysize=(128,128)), 0, 0, st, at)

            # Shoot projectile
            laser_renderer = renpy.load_image(self.laser)

            # Enter animation/logic
            if not self.entered:
                if (st - self.start_time < 9.581):
                    pass
                else:
                    self.entered = True

            # Exit animation/logic
            # TODO: instead of having the enemy exit, the plan will be to turn the background white and play an animation
            # this will be synced up with the metal pipe sound in the song
            elif self.exited:
                if (st - self.round_timer > 205.721): # amount of time the song actually plays 205.721 secs
                # TODO: THIS DOESNT WORK YET, THE GAME CRASHES HALFWAY

                    # kill the background/music for the cutscene
                    renpy.music.stop(fadeout=None)

                    renpy.notify("you made it to the end")

                    #curr_y = ease_linear(TATE_Y, -TATE_Y, self.round_timer+2, self.round_timer+3.5, st)
                    #r.blit(tate_renderer, (PT_LANE_X[2], curr_y))
                else:
                    self.win = True
                    renpy.timeout(0)

            # Main game loop
            else:
                # Timestamps
                telegraph_start = self.round_timer + TELEGRAPH_TIME
                telegraph_cutoff = telegraph_start  + TELEGRAPH_DELAY
                danger_cutoff = telegraph_cutoff + DANGER_TIME

                # Arrows flashing
                if (st - self.start_time > 9.581 and st - self.start_time < 15):
                    if math.sin(30*st) > 0:
                        r.blit(arrow_renderer, (PT_LANE_X[2]-165, 700))

                # Move enemy
                if st - self.round_timer > MOVE_FREQUENCY:
                    # Fire laser logic
                    if self.enemy_lane is not None:
                        self.tate_last_x = PT_LANE_X[self.enemy_lane]
                    else:
                        self.tate_last_x = 0

                    # More aggressive targeting that'll probably look better once the rhythm game part is implemented
                    self.enemy_lane = renpy.random.choice([
                        self.current_lane,
                        self.current_lane,
                        self.current_lane,
                        self.current_lane,
                        renpy.random.randint(0, 4)
                        ])

                    self.tate_last_move = st
                    self.tate_move_time = st + 0.5
                    self.fires += 1
                    self.round_timer = st
                    self.played_charge = False
                    self.played_fire = False

                # Danger period
                if telegraph_cutoff < st < danger_cutoff:
                    self.danger_lane = self.enemy_lane
                    if not self.played_fire:
                        self.played_fire = True
                    # Render laser
                    r.blit(laser_renderer, (PT_LANE_X[self.enemy_lane] - 16, TATE_Y+70))

                # TATE X
                if telegraph_start < st < danger_cutoff:
                    cx = PT_LANE_X[self.enemy_lane] + 45
                else:
                    cx = PT_LANE_X[self.enemy_lane] + 45 + math.sin(st * SWAY_PERIOD) * SWAY_DISTANCE
                current_tate_x = ease_linear(self.tate_last_x, cx, self.tate_last_move, self.tate_move_time, st)

                # Telegraphing period
                if telegraph_start < st < telegraph_cutoff:
                    if not self.played_charge:
                        self.played_charge = True
                    # Logic for the energy ball
                    laser_ball_displayable = renpy.displayable(self.laser_ball)
                    l = (st - telegraph_start) / (telegraph_cutoff - telegraph_start)
                    t = Transform(laser_ball_displayable, xysize=(l, l), anchor=(0.5, 0.5))

                    # Render energy ball
                    laser_ball_renderer = renpy.render(t, 180, 180, st, at)
                    xo = (abs(l-1) * 180) / 2
                    yo = (abs(l-1) * 180) / 2
                    r.blit(laser_ball_renderer, ((PT_LANE_X[self.enemy_lane] + xo) - 15, TATE_Y + yo))

                # Render Tate
                r.blit(tate_renderer, (current_tate_x, TATE_Y))

                # Render CS' health
                r.blit(health_renderer, (8, 8))

                # No more danger
                if danger_cutoff < st:
                    self.danger_lane = None

            # PLAYER LOGIC
            # TODO: cs will have a nicer health bar later
            if self.current_lane == self.danger_lane:
                renpy.sound.play("audio/sfx/sfx_hurt1.ogg")
                self.health -= 1
                if self.health < 0:
                    renpy.notify("you lost")
                    self.win = False
                    renpy.timeout(0)
            if self.fires >= FIRE_COUNT:
                self.exited = True

            # Render player character, but only if intro is over
            if self.entered == True:
                r.blit(cs_renderer, (PT_LANE_X[self.current_lane], CS_Y))

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
                if self.current_lane == 5:
                    self.current_lane = 4
                renpy.restart_interaction()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END and preferences.developer_mode:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [self.cs, self.tate, self.laser]

screen PerfectTateGame():
    default PerfectTateGame = PerfectTateGameDisplayable()
    add Movie(play="minigames/perfecttate/Tate2.webm", loop=False)
    add PerfectTateGame

label play_perfecttate_game:
    play music nyan_fight noloop if_changed
    $ persistent.heard.add("nyan_of_a_lifetime")
    window hide
    $ quick_menu = False
    call screen PerfectTateGame
    $ quick_menu = True
    window show

    if _return == True:
        $ renpy.jump(minigame_win)
    else:
        $ renpy.jump(minigame_loss)
