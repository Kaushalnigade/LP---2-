def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print("\n")


def check_winner(board):
    wins = [[0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]]

    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] != ' ':
            return board[w[0]]

    if ' ' not in board:
        return 'Draw'

    return None


def heuristic(board):
    # h(n): number of winning chances
    score = 0
    wins = [[0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]]

    for w in wins:
        line = [board[w[0]], board[w[1]], board[w[2]]]

        if line.count('X') == 2 and line.count(' ') == 1:
            score += 10
        elif line.count('O') == 2 and line.count(' ') == 1:
            score -= 10

    return score


def get_moves(board):
    return [i for i in range(9) if board[i] == ' ']


def minimax(board, depth, is_max):
    winner = check_winner(board)

    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return depth - 10
    elif winner == 'Draw':
        return 0

    if is_max:
        best = -1000
        for move in get_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best = max(best, score)
        return best
    else:
        best = 1000
        for move in get_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best = min(best, score)
        return best


def find_best_move(board):
    best_score = -1000
    best_move = None

    for move in get_moves(board):
        board[move] = 'X'

        score = minimax(board, 0, False)
        h = heuristic(board)
        f = score + h   # A* idea

        board[move] = ' '

        print(f"Position {move}: g={score}, h={h}, f={f}")

        if f > best_score:
            best_score = f
            best_move = move

    return best_move


# Main game
board = [' '] * 9

print("Tic-Tac-Toe with A* Algorithm")
print("Positions: 0-8 (left to right, top to bottom)")

print_board(board)

while True:
    winner = check_winner(board)
    if winner:
        print(f"Result: {winner}")
        break

    # Computer (X)
    print("Computer's turn (X):")
    move = find_best_move(board)
    board[move] = 'X'

    print(f"Computer chose position {move}")
    print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"Result: {winner}")
        break

    # Player (O)
    while True:
        try:
            move = int(input("Your turn (O), enter position (0-8): "))
            if board[move] == ' ':
                board[move] = 'O'
                break
            else:
                print("Position taken!")
        except:
            print("Invalid input!")

    print_board(board)


# ============================================================
# Tic-Tac-Toe using Minimax + Heuristic (A* Idea)
# ============================================================

# Main Concepts Used:
# 1. Minimax Algorithm
# 2. Heuristic Function
# 3. A* Idea
# 4. Recursion
# 5. Backtracking

# Minimax:
# Computer tries to maximize score.
# Player tries to minimize score.

# Heuristic Function:
# Estimates board quality
# and winning chances.

# A* Formula:
# f(n) = g(n) + h(n)

# g(n) -> Minimax Score
# h(n) -> Heuristic Score

# Important Functions:
# print_board()     -> Displays board
# check_winner()   -> Checks winner/draw
# heuristic()      -> Evaluates board
# get_moves()      -> Finds empty positions
# minimax()        -> AI decision making
# find_best_move() -> Selects best move

# Backtracking:
# Undo move after checking future possibilities.

# Time Complexity : O(9!)
# Space Complexity : O(9)

# ============================================================