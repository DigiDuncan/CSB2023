init python:

    class CarGameDisplayable(renpy.Displayable):

        def __init__(self):

            super().__init__(self)

            self.TIME_PER_BLAST = 5.0
            self.TELEGRAPH_TIME = 0.5
            self.DANGER_TIME = 0.5
            self.ENEMY_MOVE_TIME = 1.0
            self.FIRE_COUNT = 20

            self.time_started = None
            self.last_fire = None
            self.danger_lane = None

            self.LANES = 3
            self.current_lane_player = 1
            self.current_lane_enemy = 1
            self.enemy_last_move = 0.0
            self.enemy_frozen = False

            self.fires = 0

            # Some displayables we use.
            self.car = Image("minigames/car/billy_car.png")
            self.ufo = Image("minigames/car/joj_ufo.png")
            self.laser = Image("minigames/car/laser.png")

        def visit(self):
            # A list of all used displayables
            return [ self.car, self.ufo, self.laser ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            if self.time_started is None:
                self.time_started = st

            # Get firing times
            if self.last_fire is None and st > self.time_started + self.TIME_PER_BLAST:
                self.last_fire = st
            elif st > self.last_fire + self.TIME_PER_BLAST:
                self.last_fire = st

            # Move enemy
            self.enemy_frozen = self.last_fire < st < self.last_fire + self.TELEGRAPH_TIME + self.DANGER_TIME
            if not self.enemy_frozen:
                if self.enemy_last_move + self.ENEMY_MOVE_TIME > st:
                    self.current_lane_enemy = renpy.random.rand_int(0, 2)
                    self.enemy_last_move = st
            
            # Dangerous lanes
            if self.last_fire + self.TELEGRAPH_TIME < st < self.last_fire + self.TELEGRAPH_TIME + self.DANGER_TIME:
                self.danger_lane = self.current_lane_enemy
                self.last_fire = st
                self.fires += 1

            # Undangerous lanes
            if st > self.last_fire + self.TELEGRAPH_TIME + self.DANGER_TIME:
                self.danger_lane = None

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.KEYDOWN:
                pass # kill me

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen cargame():

    default cargame = CarGameDisplayable()

    add "minigames/car/background.png"
    add cargame

label play_cargame:

    window hide  # Hide the window and quick menu while in pong
    $ quick_menu = False

    call screen cargame

    $ quick_menu = True
    window show

    show digi

    if _return == "digi":

        digi "I win!"

    else:

        digi "You win! Congratulations."

label cargame_done:

    show digi

    menu:
        e "Would you like to play again?"

        "Sure.":

            jump play_cargame

        "No thanks.":

            pass
