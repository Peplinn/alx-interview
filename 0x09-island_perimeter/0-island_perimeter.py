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

    # while i < len(grid) and j < len(grid[0]):
    #     for row in grid:
    #         # print(row)
    #         j = 0
    #         for cell in row:
    #             # print(cell)
    #             if cell != 0 and cell != 1:
    #                 return 0
    #             if cell == 1:
    #                 if row[j-1] != 0:
    #                     perimeter -= 2
    #                     # print(f"perimeter deduction 1: {perimeter}")
    #                 if grid[i-1][j] != 0:
    #                     perimeter -= 2
    #                     # print(f"perimeter deduction 2: {perimeter}")
    #                 perimeter += 4
    #                 # print(f"perimeter: {perimeter}")
    #                 # print(f"This is i:{i} and this is j:{j}")
    #             j += 1
    #         i += 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
