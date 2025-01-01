"""renpy
rpy python annotations
python early:
"""

import random

WeightTable = tuple[tuple[float, ...], ...]

class OrthelloAI:

    def __init__(self, name: str, pickyness: float, chaos: float, depth: int, weights: WeightTable):
        self.name: str = name
        self.pickyness: float = pickyness
        self.chaos: float = chaos
        self.depth: int = depth
        self.weights: WeightTable = weights

    def pick_move(self, board: Board, turn: ReversiTile) -> tuple[tuple[int, int], list[list[tuple[int, int]]]]:
        moves = board.get_available_moves(turn)
        # We assume that the interface will call a game before we get to pick a move

        # Evaluate every possible move
        evaluations = {}
        for coord, move in moves.items():
            evaluations[coord] = self.search(board.update(turn, coord, move), turn.invert, -100000, 100000)

        ranked = sorted(moves.keys(), key=lambda c: evaluations[c], reverse=True)
        if self.chaos < random.random():
            # The AI has locked in
            coord = ranked[0]
            return coord, moves[coord]
    
        cap = max(1, int((1.0 - self.pickyness) * len(ranked)))
        picks = ranked[:cap]
        offset = min(evaluations.values())

        pick = random.choices(picks, [evaluations[tile] - offset + 1 for tile in picks])[0]
        return pick, moves[pick]

    def search(self, board: Board, turn: ReversiTile, alpha: float, beta: float, depth: int = 0) -> float:
        if depth == 0:
            return self.evaluate(board, turn)
        
        moves = board.get_available_moves(turn)
        if not moves:
            a, b = board.get_counts
            if turn == ReversiTile.BLACK:
                a, b = b, a
            if a < b:
                return -20000 # loses
            elif b < a:
                return 20000 # Wins
            else: 
                 return 0
        
        for coord, move in moves.items():
            new = board.update(turn, coord, move)
            result = -self.search(new, turn.invert(), -beta, -alpha, depth-1)
            if result >= beta:
                # The move is too good so let's prune it
                return beta
            alpha = max(result, alpha)

        return alpha

    def evaluate(self, board: Board, turn: ReversiTile) -> float:
        tiles = board.tiles
        weights = self.weights

        white_score = 0
        black_score = 0

        for col in range(board.size):
            for row in range(board.size):
                t = tiles[col][row]
                if t == ReversiTile.WHITE:
                    white_score += weights[col][row]
                elif t == ReversiTile.BLACK:
                    black_score += weights[col][row]

        perspective = 1 if turn == ReversiTile.WHITE else -1
        return (white_score - black_score) * perspective

peak_weights = (
    (10000, -3000, 1000, 800, 800, 1000, -3000, 10000),
    (-3000, -5000, -450, -500, -500, -450, -5000, -3000),
    (1000, -450, 30, 10, 10, 30, -450, 1000),
    (800, -500, 10, 50, 50, 10, -500, 800),
    (800, -500, 10, 50, 50, 10, -500, 800),
    (1000, -450, 30, 10, 10, 30, -450, 1000),
    (-3000, -5000, -450, -500, -500, -450, -5000, -3000),
    (10000, -3000, 1000, 800, 800, 1000, -3000, 10000)
)

radial_weights = (
    (10, 5, 5, 5, 5, 5, 5, 10),
    (5,  3, 3, 3, 3, 3, 3, 5),
    (5,  3, 1, 1, 1, 1, 3, 5),
    (5,  3, 1, 0, 0, 1, 3, 5),
    (5,  3, 1, 0, 0, 1, 3, 5),
    (5,  3, 1, 1, 1, 1, 3, 5),
    (5,  3, 3, 3, 3, 3, 3, 5),
    (10, 5, 5, 5, 5, 5, 5, 10)
)

plain_weights = (
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1)
)

random_weights = (
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0)
)

# --- AI ----
class ReversiAI:
    GOBLIN = OrthelloAI("Goblin", 0.0, 1.0, 0, random_weights) # Randomly chooses a move
    NOVICE = OrthelloAI("Novice", 0.0, 1.0, 0, plain_weights) # More likely to pick a move gives them more pieces
    INTERMEDIATE = OrthelloAI("Intermediate", 0.4, 0.9, 0, radial_weights) # Prioritises the outer edge over the center, but doesn't have the best weighting
    MASTER = OrthelloAI("Master", 1.0, 0.0, 2, peak_weights) # Uses the best weight table, and looks 3 moves into the future

    TATE = OrthelloAI("Tate", 0.0, 1.0, 0, random_weights)
    DIGI = OrthelloAI("Digi", 0.0, 1.0, 0, plain_weights)
    PAKOO = OrthelloAI("K-22", 0.4, 0.9, 0, radial_weights)
    ARCEUS = OrthelloAI("Arceus", 0.5, 0.5, 1, peak_weights)
    ARIA = OrthelloAI("Aria", 1.0, 0.0, 2, peak_weights)

    BILLY = OrthelloAI("Billy", 0.7, 0.7, 1, radial_weights)
    ELIZABETH = OrthelloAI("Elizabeth", 0.5, 0.5, 1, radial_weights)
    TERRY = OrthelloAI("Terry", 0.2, 1.0, 0, plain_weights)
    SCOTT = OrthelloAI("Scott", 0.0, 1.0, 0, peak_weights)
    REX = OrthelloAI("Rex", 0.0, 1.0, 1, plain_weights)
    POMNI = OrthelloAI("Pomni", 1.0, 1.0, 5, random_weights)
    LUKE = OrthelloAI("Luke", 0.5, 0.6, 1, plain_weights)
    GES = OrthelloAI("Ges", 0.4, 0.9, 0, radial_weights)
    BUBBLE = OrthelloAI("Bubble", 0.3, 0.9, 0, peak_weights)
    ANNE = OrthelloAI("Anne", 0.7, 0.3, 2, peak_weights)
    GRACE = OrthelloAI("Grace", 0.1, 1.0, 0, random_weights)