#!/usr/bin/python3
"""
0 Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if (grid[i][k] == 1):
                if (i - 1 < 0 or grid[i - 1][k] == 0):
                    perimeter += 1
                if (k - 1 < 0 or grid[i][k - 1] == 0):
                    perimeter += 1
                if (k + 1 >= len(grid[i]) or grid[i][k + 1] == 0):
                    perimeter += 1
                if (i + 1 >= len(grid) or grid[i + 1][k] == 0):
                    perimeter += 1
    return perimeter
