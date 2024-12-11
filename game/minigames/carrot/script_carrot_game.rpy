# This game is a reference to Rhythm Heaven, or rather, my take on a Rhythm Heaven
# style game. CS chops carrots to the beat.

# BEAT 28: 3 2 1 GO

init python:
    import math

    FULL_CS_HEIGHT = 1446
    CS_HEIGHT = 863

    CARROT_WIDTH = 433
    CARROT_HEIGHT = 122
    BEAT_GAP = CARROT_WIDTH * 3 # Number of pixels between carrots
    CARROT_OFFSET = 300 # Number of pixels to offset where the hit window is (from the left side of the screen)

    class CarrotGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.last_tick = 0.0
            self.win = None

            self.bpm = 127
            self.bounce_pixels = 50
            self.start_beat = 32
            self.song_length = 60.5
            self.no_beats = self.song_length / 60 * self.bpm

            self.hit_window = 0.1  # 100ms
            self.successful_beats = set()
            self.missed_beats = set()
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
            self.glowing_carrot = Image("minigames/carrot/glowing_carrot.png")
            self.chopped_carrot = Image("minigames/carrot/chopped_carrot.png")
            self.c_render = renpy.render(self.carrot, 433, 122, 0.0, 0.0)
            self.gc_render = renpy.render(self.glowing_carrot, 433, 122, 0.0, 0.0)
            self.cc_render = renpy.render(self.chopped_carrot, 285, 123, 0.0, 0.0)

            self.carrots = [self.start_beat]
            self.next_carrot = self.start_beat + 1

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

        def beat_time(self, beat: int) -> int:
            return beat * (60 / self.bpm)

        @property
        def bounce_offset(self) -> float:
            """https://www.desmos.com/calculator/ycvu69xqeo"""
            # Stolen from Charm BPM Animator
            mag = abs((self.bpm * self.song_time / 60) % 1 - 0.5) * 2
            pix = 1 - math.pow(2, -10 * mag) # ease_expoout
            return pix

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            # Play the song if we haven't
            if not self.started_playing_song:
                renpy.music.play("minigames/carrot/hotel_disbelief.ogg", loop = False)
                self.started_playing_song = True

                global _current_internal_id, _current_artist, _current_song

                _current_internal_id = "hotel_disbelief"
                _current_song = "Can You Really Call This A Hotel, I Didn't Receive A Mint On My Pillow Or Anything"
                _current_artist = "Toby Fox"

            # Update song time
            dt = st - self.last_tick
            self.song_time += dt
            was_fcing = self.is_fcing

            r = renpy.Render(1920, 1080)

            # Render background
            bg_renderer = renpy.render(self.bg, 1920, 1080, st, at)
            
            x_bounce = 0.75 + self.bounce_offset * 0.25
            y_bounce = 1.0 - self.bounce_offset * 0.25
            csbg_renderer = renpy.render(Transform(self.csbg, yzoom = y_bounce, xzoom = x_bounce), 1920, 1080, st, at)
            
            fg_renderer = renpy.render(self.fg, 1920, 1080, st, at)

            r.blit(bg_renderer, (0, 0))

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

            last = self.last_beat
            current = self.current_beat
            nearest = self.nearest_beat
            hittable = abs(self.nearest_beat_time - self.song_time) <= self.hit_window

            for carrot_beat in self.carrots[:]:
                y = self.hand_position + 100 + CARROT_HEIGHT / 2.0
                x = (self.beat_time(carrot_beat) - self.song_time) * BEAT_GAP + CARROT_OFFSET
                if x <= -300:
                    self.carrots.remove(carrot_beat)

                if carrot_beat in self.successful_beats:
                    r.blit(self.cc_render, (x, y))
                elif carrot_beat == nearest and hittable:
                    r.blit(self.gc_render, (x, y))
                else: 
                    r.blit(self.c_render, (x, y))
 
            if self.next_carrot <= self.no_beats and (self.beat_time(self.next_carrot) - self.song_time) * BEAT_GAP + CARROT_OFFSET <= 1920:
                self.carrots.append(self.next_carrot)
                self.next_carrot += 1

            if self.current_beat < 8:
                music_renderer = renpy.render(Transform(DynamicDisplayable(_music_gen_text), zoom = 0.5), 1920, 1080, st, at)
                r.blit(music_renderer, (0, 0))

            # 3 2 1 Go
            if last != current and current == self.start_beat - 4:
                renpy.sound.play("minigames/carrot/3.ogg")
            elif last != current and current == self.start_beat - 3:
                renpy.sound.play("minigames/carrot/2.ogg")
            elif last != current and current == self.start_beat - 2:
                renpy.sound.play("minigames/carrot/1.ogg")
            elif last != current and current == self.start_beat - 1:
                renpy.sound.play("minigames/carrot/go.ogg")

            hit = False
            miss = False

            # Process input
            if self.hit_to_process and self.start_beat - 1 <= current:
                input_time = self.song_time

                # Find nearest beat
                if hittable:
                    if nearest not in self.successful_beats:
                        # Good hit!
                        self.successful_beats.add(nearest)
                        self.hits += 1

                        hit = True
                    else:
                        # Overhit!
                        self.misses += 1
                        self.is_fcing = False
                        miss = True
                else:
                    # Miss!
                    self.misses += 1
                    self.is_fcing = False
                    self.missed_beats.add(nearest)
                    miss = True

            if (
                    self.song_time - dt < self.beat_time(nearest) + self.hit_window < self.song_time and
                    nearest not in self.successful_beats and
                    nearest not in self.missed_beats and
                    self.start_beat <= nearest
                ): 
                # Miss!
                self.misses += 1
                self.is_fcing = False
                self.missed_beats.add(nearest)
                miss = True

            if was_fcing and not self.is_fcing:
                renpy.sound.play("minigames/carrot/perfect_fail.ogg")
            elif miss:
                renpy.sound.play("minigames/carrot/miss.ogg")
            elif hit:
                renpy.sound.play("minigames/carrot/hit.ogg")

            # hardcode win for now
            if self.song_time > self.song_length:
                self.win = True

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
