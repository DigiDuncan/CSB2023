# This game is a reference to Rhythm Heaven, or rather, my take on a Rhythm Heaven
# style game. CS chops carrots to the beat.

# BEAT 28: 3 2 1 GO

init python:
    import math
    import pygame

    # DISPLAY VARIABLES
    CS_HEIGHT = 863
    CARROT_WIDTH = 433
    CARROT_HEIGHT = 122
    BEAT_GAP = CARROT_WIDTH * 3 # Number of pixels between carrots
    CARROT_OFFSET = 300 # Number of pixels to offset where the hit window is (from the left side of the screen)
    BOUNCE_PIXELS = 50
    HAND_POSITION = 560
    FINISH_EVENT = pygame.event.register('MinigameDone')

    # ENGINE VARIABLES
    INPUT_SYNC_OFFSET = 0.000
    AUDIO_SYNC_OFFSET = 0.000
    HIT_WINDOW = 0.150  # 150ms
    BPM = 127
    START_BEAT = 32
    SONG_LENGTH = 60.5
    NUMBER_OF_BEATS = SONG_LENGTH / 60 * BPM
    BEATS_TO_DROP = 4

    # GAME VARIABLES
    ACCURACY_TO_WIN = 0.75

    class CarrotGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.last_tick = 0.0
            self.win = None

            self.successful_beats = set()
            self.missed_beats = set()
            self.hits = 0
            self.misses = 0

            self.hit_to_process = False
            self.pressing_down = False
            self.pressed_space_once = False
            self.last_beat = -1
            self.last_audio_beat = -1

            self.is_fcing = True
            self._song_time = 0.0
            self.started_playing_song = False

            self.bg = Image("minigames/carrot/bg.png")
            self.csbg = Image("minigames/carrot/csbg.png")
            self.hand = Image("minigames/carrot/hand.png")
            self.space = Image("minigames/carrot/space.png")
            self.fg = Image("minigames/carrot/fg.png")
            self.perfect = Image("minigames/carrot/perfect.png")

            self.carrot = Image("minigames/carrot/carrot.png")
            self.glowing_carrot = Image("minigames/carrot/glowing_carrot.png")
            self.chopped_carrot = Image("minigames/carrot/chopped_carrot.png")

            # Precache sounds
            renpy.sound.play("minigames/carrot/hotel_disbelief.ogg", relative_volume=0.0)
            renpy.sound.play("minigames/carrot/3.ogg", relative_volume=0.0)
            renpy.sound.play("minigames/carrot/2.ogg", relative_volume=0.0)
            renpy.sound.play("minigames/carrot/1.ogg", relative_volume=0.0)
            renpy.sound.play("minigames/carrot/go.ogg", relative_volume=0.0)
            renpy.sound.play("minigames/carrot/hit.ogg", relative_volume=0.0)
            renpy.sound.play("minigames/carrot/miss.ogg", relative_volume=0.0)
            renpy.sound.play("minigames/carrot/perfect_fail.ogg", relative_volume=0.0)

        @property
        def song_time(self) -> float:
            return self._song_time + INPUT_SYNC_OFFSET

        @property
        def song_audio_time(self) -> float:
            return self._song_time + AUDIO_SYNC_OFFSET

        @property
        def current_beat(self) -> int:
            return int(self.song_time * (BPM / 60))

        @property
        def current_audio_beat(self) -> int:
            return int(self.song_audio_time * (BPM / 60))

        @property
        def nearest_beat(self) -> int:
            return int(round(self.song_time * (BPM / 60)))

        @property
        def nearest_beat_time(self) -> int:
            return self.nearest_beat * (60 / BPM)

        @property
        def accuracy(self) -> float:
            if self.hits == 0:
                return 0
            return self.hits / (self.hits + self.misses)

        def beat_time(self, beat: int) -> int:
            return beat * (60 / BPM) + INPUT_SYNC_OFFSET

        @property
        def bounce_offset(self) -> float:
            """https://www.desmos.com/calculator/ycvu69xqeo"""
            # Stolen from Charm BPM Animator
            mag = abs((BPM * self.song_audio_time / 60) % 1 - 0.5) * 2
            pix = 1 - math.pow(2, -10 * mag) # ease_expoout
            return pix

        def reset(self):
            self.start_time = None
            self.last_tick = 0.0
            self.win = None

            self.successful_beats = set()
            self.missed_beats = set()
            self.hits = 0
            self.misses = 0

            self.hit_to_process = False
            self.pressing_down = False
            self.pressed_space_once = False
            self.last_beat = -1
            self.last_audio_beat = -1

            self.is_fcing = True
            self._song_time = 0.0
            self.started_playing_song = False

        def render(self, width, height, st, at):
            # Play the song if we haven't
            if not self.started_playing_song:
                renpy.music.play("minigames/carrot/hotel_disbelief.ogg", loop = False)
                self.start_time = st

                # Set music popup variables for later, also makes pause screen work
                global _current_internal_id, _current_artist, _current_song
                _current_internal_id = "hotel_disbelief"
                _current_song = "Can You Really Call This A Hotel, I Didn't Receive A Mint On My Pillow Or Anything"
                _current_artist = "Toby Fox"

            if renpy.music.get_pos() is not None:
                self.started_playing_song = True

            # Update song time
            t = renpy.music.get_pos()
            t = t if t is not None else SONG_LENGTH
            dt = t - self.last_tick
            self._song_time = t
            was_fcing = self.is_fcing

            r = renpy.Render(1920, 1080)

            # Render background
            bg_renderer = renpy.render(self.bg, 1920, 1080, st, at)
            

            x_bounce = 1.0 # - self.bounce_offset * 0.25
            y_bounce = 0.75 + self.bounce_offset * 0.25
            csbg_renderer = renpy.render(Transform(self.csbg, yzoom = y_bounce, xzoom = x_bounce), 1920, 1080, st, at)
            
            fg_renderer = renpy.render(self.fg, 1920, 1080, st, at)

            r.blit(bg_renderer, (0, 0))

            down_amount = self.bounce_offset * 0.25
            r.blit(csbg_renderer, (0, -CS_HEIGHT * (down_amount)))

            r.blit(fg_renderer, (0, 0))

            # Render hand
            hand_renderer = renpy.render(self.hand, 1920, 1080, st, at)
            h_pos = HAND_POSITION + (100 * self.pressing_down)
            r.blit(hand_renderer, (0, h_pos))

            # Render space
            if not self.pressed_space_once or st - self.start_time > SONG_LENGTH + 0.5:
                space_renderer = renpy.render(self.space, 240, 70, st, at)
                r.blit(space_renderer, (CARROT_OFFSET, HAND_POSITION - 80))

            # Render perfect
            if self.current_beat % 4 in (0, 1) and self.is_fcing:
                perfect_renderer = renpy.render(self.perfect, 1920, 1080, st, at)
                r.blit(perfect_renderer, (1466, 10))

            last = self.last_beat
            current = self.current_beat
            last_audio = self.last_audio_beat
            current_audio = self.current_audio_beat
            nearest = self.nearest_beat
            hittable = abs(self.nearest_beat_time - self.song_time) <= HIT_WINDOW

            c_render = renpy.render(self.carrot, CARROT_WIDTH, CARROT_HEIGHT, 0.0, 0.0)
            gc_render = renpy.render(self.glowing_carrot, CARROT_WIDTH, CARROT_HEIGHT, 0.0, 0.0)
            cc_render = renpy.render(self.chopped_carrot, 285, 123, 0.0, 0.0)

            start = max(current - 2, START_BEAT)
            end = min(current + 4, int(NUMBER_OF_BEATS - BEATS_TO_DROP + 1))
            for carrot_beat in range(start, end):
                y = HAND_POSITION + 100 + CARROT_HEIGHT / 2.0
                x = (self.beat_time(carrot_beat) - self.song_time) * BEAT_GAP + CARROT_OFFSET

                if carrot_beat in self.successful_beats:
                    r.blit(cc_render, (x, y))
                elif carrot_beat == nearest and hittable:
                    r.blit(gc_render, (x, y))
                else: 
                    r.blit(c_render, (x, y))

            if self.current_beat < 8:
                a = 1.0 if self.current_beat < 7 else 1 - (self.song_time - self.beat_time(7))
                music_renderer = renpy.render(Transform(DynamicDisplayable(_music_gen_text), zoom = 0.5, alpha = a), 1920, 1080, st, at)
                r.blit(music_renderer, (0, 0))

            # 3 2 1 Go
            if last_audio != current_audio and current_audio == START_BEAT - 4:
                renpy.sound.play("minigames/carrot/3.ogg")
            elif last_audio != current_audio and current_audio == START_BEAT - 3:
                renpy.sound.play("minigames/carrot/2.ogg")
            elif last_audio != current_audio and current_audio == START_BEAT - 2:
                renpy.sound.play("minigames/carrot/1.ogg")
            elif last_audio != current_audio and current_audio == START_BEAT - 1:
                renpy.sound.play("minigames/carrot/go.ogg")

            hit = False
            miss = False

            # Process input
            if self.hit_to_process and START_BEAT - 1 <= current and current <= (NUMBER_OF_BEATS - BEATS_TO_DROP):
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
                    self.song_time - dt < self.beat_time(nearest) + HIT_WINDOW < self.song_time and
                    nearest not in self.successful_beats and
                    nearest not in self.missed_beats and
                    START_BEAT <= current and
                    current < (NUMBER_OF_BEATS - BEATS_TO_DROP)
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

            if renpy.music.get_pos() is None and self.started_playing_song:
                if self.is_fcing:
                    self.win = "superb"
                elif self.accuracy >= ACCURACY_TO_WIN:
                    self.win = "ok"
                else:
                    self.win = "try_again"
                pygame.event.post(pygame.event.Event(FINISH_EVENT))

            self.last_tick = t
            self.last_beat = self.current_beat
            self.last_audio_beat = self.current_audio_beat
            self.hit_to_process = False
            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            print('I hate you and everyone you love', self.win, ev, x, y, st)
            import pygame
            if ev.type == pygame.KEYDOWN and not self.pressing_down:
                if ev.key == pygame.K_END:
                    self.win = "ok"
                if ev.key == pygame.K_SPACE:
                    self.pressing_down = True
                    self.hit_to_process = True
                    self.pressed_space_once = True
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_SPACE:
                    self.pressing_down = False
            # This *should* return the frame that self.win is set, but it's requiring a button input
            # Why? `redraw` is an event that calls this function, and we call of one those every frame, necessarily.
            # ow
            if self.win is not None:
                win = self.win
                self.reset()
                return win

        def visit(self):
            return [] # Assets needed to load


screen carrotgame():
    default carrotgame = CarrotGameDisplayable()
    # Add a background or any static images here.
    add carrotgame

screen carrotresults(a):
    text a:
        align (0.5, 0.5)
        font "minigames/carrot/Storm Sans Std.ttf"
        size 48
        textalign 0.5
        color "#ffffff"

label play_carrotgame:
    window hide
    $ quick_menu = False
    call screen carrotgame
    $ quick_menu = True
    window show
    $ persistent.heard.add("hotel_disbelief")

    if _return == "superb":
        stop music
        window hide
        scene black
        pause 1.0
        show obama_says at manual_pos(0.5, 0.25, 0.5)
        play sound "minigames/carrot/step1.ogg"
        pause 1.0
        show screen carrotresults("Amazing work, CS!\nYou made America proud.\nIt's a Christmas miracle!")
        play sound "minigames/carrot/step2.ogg"
        pause 1.0
        show rating_superb at manual_pos(0.8, 0.8, 1.0)
        play music "minigames/carrot/superb_music.ogg"
        $ achievement_manager.unlock("shitdown")
        $ achievement_manager.unlock("paradise")
        pause
        hide screen carrotresults
        $ renpy.jump(minigame_win)
    elif _return == "ok":
        stop music
        window hide
        scene black
        pause 1.0
        show obama_says at manual_pos(0.5, 0.25, 0.5)
        play sound "minigames/carrot/step1.ogg"
        pause 1.0
        show screen carrotresults("Great chopping, CS!\nYou were on beat!\nWe'll feed the unchopped ones to the reindeer.")
        play sound "minigames/carrot/step2.ogg"
        pause 1.0
        show rating_ok at manual_pos(0.8, 0.8, 1.0)
        play music "minigames/carrot/ok_music.ogg"
        $ achievement_manager.unlock("shitdown")
        pause
        hide screen carrotresults
        $ renpy.jump(minigame_win)
    else:
        # try_again
        stop music
        window hide
        scene black
        pause 1.0
        show obama_says at manual_pos(0.5, 0.25, 0.5)
        play sound "minigames/carrot/step1.ogg"
        pause 1.0
        show screen carrotresults("You can do better than that.\nI don't want to have to pardon you!\nTry to stay on beat!")
        play sound "minigames/carrot/step2.ogg"
        pause 1.0
        show rating_try_again at manual_pos(0.8, 0.8, 1.0)
        play music "minigames/carrot/try_again_music.ogg"
        pause
        hide screen carrotresults
        $ renpy.jump(minigame_loss)

label carrotgame_done:
    # Thing to do after the game if we reach here.
    pass
