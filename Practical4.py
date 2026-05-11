def issafe(arr, x, y, n):
    # Check column
    for row in range(x):
        if arr[row][y] == 1:
            return False

    # Check left diagonal
    row = x
    col = y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # Check right diagonal
    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def nQueen(arr, x, n):
    # Base case: all queens placed
    if x >= n:
        return True

    # Try placing queen in each column
    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = 1  # place queen

            if nQueen(arr, x + 1, n):
                return True

            arr[x][col] = 0  # backtrack

    return False


def main():
    n = int(input("Enter number of Queens: "))
    arr = [[0] * n for _ in range(n)]

    if nQueen(arr, 0, n):
        print("Solution:")
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
            print()
    else:
        print("No solution exists")


if __name__ == '__main__':
    main()