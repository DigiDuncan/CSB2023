init python:

    class CarGameDisplayable(renpy.Displayable):

        def __init__(self):

            super().__init__(self)

            self.TIME_PER_BLAST = 5.0
            self.TELEGRAPH_TIME = 0.5
            self.DANGER_TIME = 0.5

            self.time_started = None
            self.last_fire = None
            self.danger_lane = None

            self.LANES = 3
            self.current_lane_player = 1
            self.current_lane_enemy = 1

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

            if self.last_fire is None and st > self.time_started + self.TIME_PER_BLAST:
                self.last_fire = st
            elif st > self.last_fire + self.TIME_PER_BLAST:
                self.last_fire = st
            
            


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
