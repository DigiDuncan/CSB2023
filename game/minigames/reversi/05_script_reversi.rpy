# Can you believe it?

init python:
    import time
    import math

    board_length = 720
    canv_x = 960
    canv_y = 540
    board_x = canv_x - (board_length/2)
    board_y = canv_y - (board_length/2)

    class ReversiGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.last_tick = None
            self.win = None
            self.game = Board(8)
            self.ai = ReversiAI.GOBLIN
            self.turn = ReversiTile.WHITE

        def render(self, width, height, st, at):
            if self.last_tick is None:
                self.last_tick = st
            dt = st - self.last_tick

            if self.game.is_game_over(self.turn):
                renpy.notify("Game ended, but I haven't implemented this yet. - Arc")

            if self.turn == ReversiTile.BLACK:
                time.sleep(1)
                coords, bookends = self.ai.pick_move(self.game, self.turn)
                self.game = self.game.update(self.turn, coords, bookends)
                self.turn = self.turn.invert()

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
            # Next get the game state and update it
            for row in range(self.game.size):
                for column in range(self.game.size):
                    curr_tile = self.game.tiles[column][row]
                    if curr_tile == ReversiTile.NONE:
                        continue
                    elif curr_tile == ReversiTile.BLACK:
                        # Draw a black circle
                        # First calculate where the top left of the circle will be
                        circ_x = (((column) * (board_length/8))+board_x)+((board_length/8)/2)
                        circ_y = (((row) * (board_length/8))+board_y)+((board_length/8)/2)
                        s.circle((0,0,0), (circ_x, circ_y), board_length/16)
                    elif curr_tile == ReversiTile.WHITE:
                        # Draw a white circle
                        circ_x = (((column) * (board_length/8))+board_x)+((board_length/8)/2)
                        circ_y = (((row) * (board_length/8))+board_y)+((board_length/8)/2)
                        s.circle((255,255,255), (circ_x, circ_y), board_length/16)
            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            if self.turn == ReversiTile.WHITE:
                if ev.type == pygame.MOUSEBUTTONUP:
                    # Check if the mouse is in bounds of the board first:
                    if renpy.get_mouse_pos()[0] > board_x and renpy.get_mouse_pos()[0] < board_x+board_length and renpy.get_mouse_pos()[1] > board_y and renpy.get_mouse_pos()[1] < board_y+board_length:
                        # Now we calculate what box in the grid was clicked
                        grid_x = math.floor((renpy.get_mouse_pos()[0]-board_x)/(board_length/8))
                        grid_y = math.floor((renpy.get_mouse_pos()[1]-board_y)/(board_length/8))
                        coords = (grid_x, grid_y)
                        # Check if the move was LEGAL
                        bookends = self.game.get_bookends(coords, self.turn)
                        if not bookends:
                            renpy.notify("Move is not legal!")
                        else:
                            self.game = self.game.update(self.turn, coords, bookends)
                            self.turn = self.turn.invert()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load

screen reversigame():
    default reversigamedisplay = ReversiGameDisplayable()
    # Add a background or any static images here.
    add reversigamedisplay

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