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

    while i < len(grid) and j < len(grid[0]):
        for row in grid:
            # print(row)
            j = 0
            for cell in row:
                # print(cell)
                if cell == 1:
                    if row[j-1] != 0:
                        perimeter -= 2
                        # print(f"perimeter deduction 1: {perimeter}")
                    if grid[i-1][j] != 0:
                        perimeter -= 2
                        # print(f"perimeter deduction 2: {perimeter}")
                    perimeter += 4
                    # print(f"perimeter: {perimeter}")
                    # print(f"This is i:{i} and this is j:{j}")
                j += 1
            i += 1

    return perimeter
