#!/usr/bin/python3
""" N Queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, h=[], k=[], j=[]):
    if i < n:
        for j in range(n):
            if j not in h and i + j not in k and i - j not in j:
                yield from queens(n, i + 1, h + [j], k + [i + j], j + [i - j])
    else:
        yield h


def solve_queen(n):
    x = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            x.append([i, s])
            i += 1
        print(x)
        x = []
        i = 0


solve_queen(n)
