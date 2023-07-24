init python:
    import math

    class EditGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.displayable.__init__(self)
            self.start_time = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)

            # Do some fancy things here!

            renpy.redraw(self, 0)
            return r


screen edit_game:
    default edit_game = EditGameDisplayable()
    # Add a background or any static images here.
    add edit_game

label play_edit_game:
    window hide
    $ quick_menu = False
    call screen edit_game
    $ quick_menu = True
    window show

    if _return == True:
        # Thing for win condition
    else:
        # Thing for lose condition

label edit_game_done:
    # Thing to do after the game if we reach here.