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
    If n is impossible to achieve, it returns 0
    """
    if n <= 1:
        return 0

    operationsPerformed = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operationsPerformed += factor
            n //= factor
        factor += 1

    return operationsPerformed
