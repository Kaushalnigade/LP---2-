def print_board(board, n):

    print("\nSolution:")

    for i in range(n):
        for j in range(n):

            print("Q" if board[i][j] == 1 else ".", end=" ")

        print()


def solve(board, row, n, columns, diag1, diag2):

    if row == n:
        return True

    for col in range(n):

        if col in columns or (row - col) in diag1 or (row + col) in diag2:
            continue

        board[row][col] = 1

        columns.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        if solve(board, row + 1, n, columns, diag1, diag2):
            return True

        board[row][col] = 0

        columns.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    return False


n = int(input("Enter value of N: "))

board = [[0] * n for _ in range(n)]

columns = set()
diag1 = set()
diag2 = set()

if solve(board, 0, n, columns, diag1, diag2):

    print_board(board, n)

else:
    print("Solution does not exist")




# Branch and Bound:
# Try a solution.
# If position is unsafe,
# reject it immediately.

# N-Queen Problem:
# Place N queens on N×N chessboard
# so no two queens attack each other.

# Uses:
# 1. Column Set
# 2. Left Diagonal Set
# 3. Right Diagonal Set

# Faster than normal Backtracking
# because checking is done in O(1).

# Time Complexity:
# Worst Case : O(N!)

# Space Complexity:
# O(N²)
