#!/usr/bin/python3
"""_summary_
"""


def island_perimeter(grid):
    """_summary_

    Args:
                    grid (list): grid denoting island
    """
    perimeter = 0
    i = 0
    j = 0

    if len(grid) > 100 or len(grid[0]) > 100:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
