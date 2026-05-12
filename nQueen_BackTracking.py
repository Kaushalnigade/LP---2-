def print_board(board, n):

    print("\nSolution:")

    for i in range(n):
        for j in range(n):

            print("Q" if board[i][j] == 1 else ".", end=" ")

        print()


def is_safe(board, row, col, n):

    for i in range(row):

        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    i, j = row - 1, col + 1

    while i >= 0 and j < n:

        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter value of N: "))

board = [[0] * n for _ in range(n)]

if solve(board, 0, n):

    print_board(board, n)

else:
    print("Solution does not exist")



# Backtracking:
# Try a solution.
# If it fails,
# undo it and try another solution.

# N-Queen Problem:
# Place N queens on N×N chessboard
# so no two queens attack each other.

# Checks:
# 1. Same Column
# 2. Left Diagonal
# 3. Right Diagonal

# Time Complexity:
# Worst Case : O(N!)

# Space Complexity:
# O(N²)