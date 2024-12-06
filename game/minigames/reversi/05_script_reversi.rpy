# Can you believe it?

init python:
    import math
    from random import choice

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
            self.ai = reversi_difficulty
            self.turn = ReversiTile.WHITE

            self.wait_timer = 1.0

            self.player_name_text = Text("You", color = "#ff0000", size = 72)
            self.player_score_text = Text("2", color = "#ff0000", size = 72)
            self.enemy_name_text = Text(self.ai.name, color = "#0000ff", size = 72)
            self.enemy_score_text = Text("2", color = "#0000ff", size = 72)

            self.help_text = Text("Press H for help!", color = "#000000", size = 36)
            self.help_modal = renpy.get_registered_image("reversi_rules")
            self.showing_help = False

        def clink(self):
            sound = choice(["place1", "place2", "place3", "place4", "place5"])
            renpy.sound.play(f"minigames/reversi/{sound}.ogg", channel="sound")

        def render(self, width, height, st, at):
            if self.last_tick is None:
                self.last_tick = st
            dt = st - self.last_tick

            if self.game.is_game_over(self.turn):
                w, b = self.game.get_counts()
                self.win = w >= b

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

            w, b = self.game.get_counts()
            self.player_score_text = Text(str(w), color = "#ff0000", size = 72)
            self.enemy_score_text = Text(str(b), color = "#0000ff", size = 72)

            r.place(self.player_name_text, x = 5, y = 5)
            r.place(self.player_score_text, x = 5, y = 75)
            r.place(self.enemy_name_text, x = 5, y = 145)
            r.place(self.enemy_score_text, x = 5, y = 215)
            r.place(self.help_text, x = 1650, y = 5)

            if self.showing_help:
                r.place(self.help_modal, x = (1920 / 2), y = (1080 / 2))

            renpy.redraw(self, 0)

            if self.turn == ReversiTile.BLACK and not self.game.is_game_over(self.turn):
                if self.wait_timer > 0:
                    self.wait_timer -= dt
                else:
                    coords, bookends = self.ai.pick_move(self.game, self.turn)
                    self.game = self.game.update(self.turn, coords, bookends)
                    self.turn = self.turn.invert()
                    self.wait_timer = 1.0
                    self.clink()

            self.last_tick = st

            return r

        def event(self, ev, x, y, st):
            if self.turn == ReversiTile.WHITE and not self.showing_help:
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
                            self.clink()

            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if ev.type == pygame.KEYUP and ev.key == pygame.K_h:
                self.showing_help = not self.showing_help
            if self.win is not None:
                return self.game.get_counts()

        def visit(self):
            return [] # Assets needed to load

screen reversigame():
    default reversigamedisplay = ReversiGameDisplayable()
    # Add a background or any static images here.
    add "minigames/reversi/background.png"
    add reversigamedisplay

label play_reversigame:
    window hide
    $ quick_menu = False
    call screen reversigame
    $ quick_menu = True
    window show

    if _return:
        $ w,b = _return
        n "You scored [w], [reversi_difficulty.name] scored [b]."
        if w >= b:
            n "You win!"
            $ renpy.jump(minigame_win)
        else:
            n "[reversi_difficulty.name] wins!"
            $ renpy.jump(minigame_loss)

label reversigame_done:
    # Thing to do after the game if we reach here.
    pass
