#!/usr/bin/python3
"""A script to determine pascal's triangle for anvalue number"""


def pascal_triangle(num) :
    """
    returns list of lists containing Pascal’s triangle integers of n
    """
    triangle = []

    if num <= 0 :
        return triangle

    if num == 1 :
        triangle.append(1)


    for row in range(num) :
        # print("This iteration, row is ", row)
        row_list = []

        for value in range(row+1):
            if value in (0, row):
                row_list.append(1)
            else:
                row_list.append(triangle[row-1][value-1] + triangle[row-1][value])

        triangle.append(row_list)

    return triangle
