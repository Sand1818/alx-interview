#!/usr/bin/python3
""" N Queens """
import sys


def isSafe(Board, Row, Column):
    """ Checks if queen can move into column on the board"""
    for j in range(Row):
        if Board[j] == Column or abs(Board[j] - Column) == Row - j:
            return False
    return True

def solve_nqueens(N, board, row, sol):
    if row == N:
        sol.append(board[:])
        return

    for col in range(N):
        if isSafe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1, sol)

def print_Solution(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    print_Solution(N)
