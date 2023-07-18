init python:
    import math

    # Constants

    class PencilGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.current_key = True
            # I'm using a boolean statement here, Q needing to be pressed is True, E needing to be pressed is false. Reason for this is just so I can be lazy.
            self.current_pencil_length = 20.0
            # All pencils start at 20 cm, it will be a floating point, unless told otherwise
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            # Set start time if it isn't (frame 0)
            if self.start_time is None:
                self.start_time = st

            # Render object we return at the end
            r = renpy.Render(1920, 1080)

            # Main game loop
            pass

            renpy.redraw(self, 0)
            return r
            
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and (ev.key == pygame.K_q or ev.key == pygame.k_e):
                if ev.key == pygame.K_q and self.current_key:
                    # Progress the pencil.
                    self.current_key = False
                elif ev.key == pygame.K_e and not self.current_key:
                    # Progress the pencil
                    self.current_key = True
                pass
            if ev.type = pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                # Calculate new score
                # TODO: Score calculation
                # New pencil
                self.current_pencil_length = 20.0
                pass
            if self.win is not None:
                return self.win

        def visit(self):
            return []


screen pencilgame:
    default pencilgame = PencilGameDisplayable()
    add pencilgame

label play_pencilgame:
    window hide
    $ quick_menu = False
    call screen pencilgame
    $ quick_menu = True
    window show

    if _return == True:
        jump win_pencil
    else:
        arceus "You dumb foreskin."
        jump play_pencilgame

label pencilgame_done:
    show arceus
    arceus ":3"
