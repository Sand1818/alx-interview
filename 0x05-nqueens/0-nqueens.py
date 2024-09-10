#!/usr/bin/python3
""" N Queens """
import sys


def isSafe(Board, Row, Column):
    """ Checks if queen can move into column on the board"""
    for j in range(Row):
        if (Board[j] == Column or
                Board[j] + Row - j == Column or
                Board[j] + j - Row == Column):
            return False
    return True


def populate_row(Board, Line):
    """ Populates the chess board """
    for i in range(len(Board)):
        if isSafe(Board, Line, i):
            Board[Line] = i
            if Line < len(Board) - 1:
                populate_row(Board, Line + 1)
            else:
                print([[i, Board[i]] for i in range(len(Board))])

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except:
    print("N must be an interger (number)")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

Board = [-1 for i in range(n)]
populate_row(Board, 0)
