# Can you believe it?

init python:
    import math

    board_length = 720
    canv_x = 960
    canv_y = 540
    board_x = canv_x - (board_length/2)
    board_y = canv_y - (board_length/2)

    class ReversiGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)
            s = r.canvas()
            # Draw the reversi board
            # First the background
            s.rect(color=(52,157,52), rect=pygame.Rect(board_x, board_y, board_length, board_length), width=0)
            s.rect(color=(0,0,0), rect = pygame.Rect(board_x, board_y, board_length, board_length), width=5)
            # Next the gridlines
            for line in range(0, board_length, int(board_length/8)):
                s.rect(color=(0,0,0), rect = pygame.Rect(board_x+line, board_y, 5, board_length), width=0)
                s.rect(color=(0,0,0), rect = pygame.Rect(board_x, board_y+line, board_length, 5), width=0)

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP:
                # Check if the mouse is in bounds of the board first:
                if renpy.get_mouse_pos()[0] > board_x and renpy.get_mouse_pos()[0] < board_x+board_length and renpy.get_mouse_pos()[1] > board_y and renpy.get_mouse_pos()[1] < board_y+board_length:
                    # Now we calculate what box in the grid was clicked
                    grid_x = math.floor((renpy.get_mouse_pos()[0]-board_x)/(board_length/8))
                    grid_y = math.floor((renpy.get_mouse_pos()[1]-board_y)/(board_length/8))
                    renpy.notify(str(grid_x)+" "+str(grid_y))
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load

screen reversigame():
    default templategame = ReversiGameDisplayable()
    # Add a background or any static images here.
    add templategame

label play_reversigame:
    window hide
    $ quick_menu = False
    call screen reversigame
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label reversigame_done:
    # Thing to do after the game if we reach here.
    pass