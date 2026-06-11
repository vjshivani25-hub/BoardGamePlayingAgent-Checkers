from dataclasses import dataclass
import math
import copy

BOARD_SIZE = 8

# ----------------------------
# Game State
# ----------------------------

@dataclass
class Move:
    start_row: int
    start_col: int
    end_row: int
    end_col: int

class CheckersGame:

    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        # AI pieces
        for r in range(3):
            for c in range(BOARD_SIZE):
                if (r + c) % 2 == 1:
                    board[r][c] = 'A'

        # Human pieces
        for r in range(5, 8):
            for c in range(BOARD_SIZE):
                if (r + c) % 2 == 1:
                    board[r][c] = 'H'

        return board

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

# ----------------------------
# Move Generation
# ----------------------------

def get_valid_moves(board, player):

    moves = []

    direction = 1 if player == 'A' else -1

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):

            if board[r][c] == player:

                for dc in [-1, 1]:

                    nr = r + direction
                    nc = c + dc

                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                        if board[nr][nc] == '.':
                            moves.append(Move(r, c, nr, nc))

    return moves

# ----------------------------
# Apply Move
# ----------------------------

def apply_move(board, move):

    new_board = copy.deepcopy(board)

    piece = new_board[move.start_row][move.start_col]

    new_board[move.start_row][move.start_col] = '.'
    new_board[move.end_row][move.end_col] = piece

    return new_board

# ----------------------------
# Evaluation Function
# ----------------------------

def evaluate(board):

    ai_count = 0
    human_count = 0

    for row in board:
        ai_count += row.count('A')
        human_count += row.count('H')

    return ai_count - human_count

# ----------------------------
# Terminal State
# ----------------------------

def game_over(board):

    ai_count = 0
    human_count = 0

    for row in board:
        ai_count += row.count('A')
        human_count += row.count('H')

    return ai_count == 0 or human_count == 0

# ----------------------------
# Minimax + Alpha Beta
# ----------------------------

def minimax(board, depth, alpha, beta, maximizing):

    if depth == 0 or game_over(board):
        return evaluate(board), None

    if maximizing:

        max_eval = -math.inf
        best_move = None

        moves = get_valid_moves(board, 'A')

        for move in moves:

            child = apply_move(board, move)

            eval_score, _ = minimax(
                child,
                depth - 1,
                alpha,
                beta,
                False
            )

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move

            alpha = max(alpha, eval_score)

            if beta <= alpha:
                break

        return max_eval, best_move

    else:

        min_eval = math.inf
        best_move = None

        moves = get_valid_moves(board, 'H')

        for move in moves:

            child = apply_move(board, move)

            eval_score, _ = minimax(
                child,
                depth - 1,
                alpha,
                beta,
                True
            )

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move

            beta = min(beta, eval_score)

            if beta <= alpha:
                break

        return min_eval, best_move

# ----------------------------
# Explainability
# ----------------------------

def explain_move(move):

    if move:
        print(
            f"AI selected move: "
            f"({move.start_row},{move.start_col}) "
            f"-> "
            f"({move.end_row},{move.end_col})"
        )

# ----------------------------
# Main Program
# ----------------------------

def main():

    game = CheckersGame()

    print("Initial Board:")
    game.print_board()

    score, best_move = minimax(
        game.board,
        depth=4,
        alpha=-math.inf,
        beta=math.inf,
        maximizing=True
    )

    explain_move(best_move)

    if best_move:
        game.board = apply_move(game.board, best_move)

    print("\nBoard After AI Move:")
    game.print_board()

    print("Evaluation Score:", score)

if __name__ == "__main__":
    main()