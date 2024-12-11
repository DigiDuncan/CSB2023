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

            self.is_fcing = True
            self.song_time = 0.0
            self.started_playing_song = False

            self.bg = Image("minigames/carrot/bg.png")
            self.csbg = Image("minigames/carrot/csbg.png")
            self.hand = Image("minigames/carrot/hand.png")
            self.fg = Image("minigames/carrot/fg.png")

            self.carrot = Image("minigames/carrot/carrot.png")
            self.chopped_carrot = Image("minigames/carrot/chopped_carrot.png")

            self.hand_position = 560

        @property
        def current_beat(self) -> int:
            return int(self.song_time * (self.bpm / 60))

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
            h_pos = self.hand_position
            r.blit(hand_renderer, (0, h_pos))

            # Play the song if we haven't
            if not self.started_playing_song:
                renpy.music.play("minigames/carrot/hotel_disbelief.ogg")
                self.started_playing_song = True

            # Update song time
            self.song_time += dt

            renpy.redraw(self, 0)
            self.last_tick = st
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
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

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label carrotgame_done:
    # Thing to do after the game if we reach here.
    pass
