#!/usr/bin/python3
"""
Method that calculates fewest number of operations needed
to result in
"""


def minOperations(n):
    """
    In a text file with a single character,
    this checks whether only Copy All and Paste can yield
    exactly n 'H' characters in a given file.
    """
    printedH = "H"
    clipboard = ""
    operationsPerformed = 0

    while len(printedH) <= n:
        if n % 2 and operationsPerformed == 2:
            printedH += "H"
            clipboard = "H"
            operationsPerformed += 1

        if len(printedH) + len(clipboard) <= n:
            if len(clipboard) < len(printedH) and 2 * len(printedH) <= n:
                clipboard = printedH
                printedH += clipboard
                operationsPerformed += 2
            elif (
                len(printedH) < len(clipboard) or
                len(printedH) + len(clipboard) == n
            ):
                printedH += clipboard
                operationsPerformed += 1
        else:
            break

    return operationsPerformed
