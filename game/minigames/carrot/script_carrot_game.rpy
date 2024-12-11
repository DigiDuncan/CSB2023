# This game is a reference to Rhythm Heaven, or rather, my take on a Rhythm Heaven
# style game. CS chops carrots to the beat.

# BEAT 28: 3 2 1 GO

init python:
    import math

    FULL_CS_HEIGHT = 1446
    CS_HEIGHT = 863

    class CarrotGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.last_tick = 0.0
            self.win = None

            self.bpm = 127
            self.bounce_pixels = 50
            self.start_beat = 32

            self.hit_window = 0.1  # 100ms
            self.successful_beats = []
            self.hits = 0
            self.misses = 0

            self.hit_to_process = False
            self.pressing_down = False
            self.last_beat = -1

            self.is_fcing = True
            self.song_time = 0.0
            self.started_playing_song = False

            self.bg = Image("minigames/carrot/bg.png")
            self.csbg = Image("minigames/carrot/csbg.png")
            self.hand = Image("minigames/carrot/hand.png")
            self.fg = Image("minigames/carrot/fg.png")

            self.carrot = Image("minigames/carrot/carrot.png")
            self.chopped_carrot = Image("minigames/carrot/chopped_carrot.png")

            self.perfect = Image("minigames/carrot/perfect.png")

            self.hand_position = 560

        @property
        def current_beat(self) -> int:
            return int(self.song_time * (self.bpm / 60))

        @property
        def nearest_beat(self) -> int:
            return int(round(self.song_time * (self.bpm / 60)))

        @property
        def nearest_beat_time(self) -> int:
            return self.nearest_beat * (60 / self.bpm)

        @property
        def bounce_offset(self) -> float:
            # BAD: FIX THIS DRAGON
            """https://www.desmos.com/calculator/ycvu69xqeo"""
            # pix = (self.song_time % (1 / (self.bpm / 2 / 60)) * -(self.bpm / 2 / 60) + 1)
            # Stolen from Charm BPM Animator
            mag = abs((self.bpm * self.song_time / 60) % 1 - 0.5) * 2
            pix = 1 - math.pow(2, -10 * mag) # ease_expoout
            return pix

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            dt = st - self.last_tick
            r = renpy.Render(1920, 1080)

            # Render background
            bg_renderer = renpy.render(self.bg, 1920, 1080, st, at)
            
            # DRAGON HEP
            x_bounce = 1.0 #  + self.bounce_offset
            y_bounce = 1.0 - self.bounce_offset * 0.25
            csbg_renderer = renpy.render(Transform(self.csbg, yzoom = y_bounce, xzoom = x_bounce), 1920, 1080, st, at)
            
            fg_renderer = renpy.render(self.fg, 1920, 1080, st, at)

            r.blit(bg_renderer, (0, 0))

            # DRAGON HEP
            down_amount = self.bounce_offset * 0.25
            r.blit(csbg_renderer, (0, CS_HEIGHT * (down_amount - 0.25)))

            r.blit(fg_renderer, (0, 0))

            # Render hand
            hand_renderer = renpy.render(self.hand, 1920, 1080, st, at)
            h_pos = self.hand_position + (100 * self.pressing_down)
            r.blit(hand_renderer, (0, h_pos))

            # Render perfect
            if self.current_beat % 4 in (0, 1) and self.is_fcing:
                perfect_renderer = renpy.render(self.perfect, 1920, 1080, st, at)
                r.blit(perfect_renderer, (0, 0))

            # Play the song if we haven't
            if not self.started_playing_song:
                renpy.music.play("minigames/carrot/hotel_disbelief.ogg")
                self.started_playing_song = True

            # 3 2 1 Go
            if self.last_beat != self.current_beat and self.current_beat == self.start_beat - 4:
                print("3!")
                renpy.sound.play("minigames/carrot/3.ogg")
            elif self.last_beat != self.current_beat and self.current_beat == self.start_beat - 3:
                print("2!")
                renpy.sound.play("minigames/carrot/2.ogg")
            elif self.last_beat != self.current_beat and self.current_beat == self.start_beat - 2:
                print("1!")
                renpy.sound.play("minigames/carrot/1.ogg")
            elif self.last_beat != self.current_beat and self.current_beat == self.start_beat - 1:
                print("Go!")
                renpy.sound.play("minigames/carrot/go.ogg")

            # Update song time
            self.song_time += dt
            was_fcing = self.is_fcing

            # Song time!
            if self.current_beat >= (self.start_beat - 1):
                # Process input
                if self.hit_to_process:
                    input_time = self.song_time

                    # Find nearest beat
                    beat = self.nearest_beat
                    if abs(input_time - self.nearest_beat_time) <= self.hit_window:
                        if beat not in self.successful_beats:
                            # Good hit!
                            self.successful_beats.append(beat)
                            self.hits += 1
                            renpy.sound.play("minigames/carrot/hit.ogg")
                        else:
                            # Overhit!
                            self.misses += 1
                            self.is_fcing = False
                            renpy.sound.play("minigames/carrot/miss.ogg")
                    
                if self.current_beat != self.last_beat:
                    if self.last_beat not in self.successful_beats:
                        # Miss!
                        self.misses += 1
                        self.is_fcing = False
                        renpy.sound.play("minigames/carrot/miss.ogg")

            if was_fcing and not self.is_fcing:
                renpy.sound.play("minigames/carrot/perfect_fail.ogg")

            renpy.redraw(self, 0)
            self.last_tick = st
            self.last_beat = self.current_beat
            self.hit_to_process = False
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_END:
                    self.win = True
                if ev.key == pygame.K_SPACE:
                    self.pressing_down = True
                    self.hit_to_process = True
            if ev.type == pygame.KEYUP:
                self.pressing_down = False
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load


screen carrotgame():
    default carrotgame = CarrotGameDisplayable()
    # Add a background or any static images here.
    add carrotgame

label play_carrotgame:
    window hide
    $ quick_menu = False
    call screen carrotgame
    $ quick_menu = True
    window show
    $ persistent.heard.add("hotel_disbelief")

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label carrotgame_done:
    # Thing to do after the game if we reach here.
    pass
