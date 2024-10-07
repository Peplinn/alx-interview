#!/usr/bin/python3
"""A script to determine pascal's triangle for anvalue number"""


def pascal_triangle(num):
    """
    returns list of lists containing Pascal’s Triangle integers of n
    """
    pasc = []

    if num <= 0:
        return pasc

    if num == 1:
        pasc.append([1])
        return pasc

    for row in range(num):
        # print("This iteration, row is ", row)
        row_list = []

        for value in range(row+1):
            if value in (0, row):
                row_list.append(1)
            else:
                row_list.append(pasc[row-1][value-1] + pasc[row-1][value])

        pasc.append(row_list)

    return pasc
