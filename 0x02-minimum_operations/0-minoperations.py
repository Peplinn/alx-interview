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

    if n <= len(printedH):
        return operationsPerformed

    while len(printedH) <= n:
        if n % 2 and operationsPerformed == 2:
            printedH += "H"
            clipboard = "H"
            operationsPerformed += 1
            print("Clipboard : " + clipboard)
            print(printedH)
            print(operationsPerformed)

        if len(printedH) + len(clipboard) <= n:
            if len(clipboard) < len(printedH) and 2 * len(printedH) <= n:
                clipboard = printedH
                printedH += clipboard
                operationsPerformed += 2
                print("Clipboard : " + clipboard)
                print(printedH)
                print(operationsPerformed)
            elif (
                len(printedH) < len(clipboard) or
                len(printedH) + len(clipboard) == n or
                (len(printedH) + len(clipboard) <= n and
                 not (n % len(clipboard)))
            ):
                printedH += clipboard
                operationsPerformed += 1
                print("Clipboard : " + clipboard)
                print(printedH)
                print(operationsPerformed)
            else:
                break
        else:
            break
    
    print("PrintedH: " + printedH)
    print("Clipboard: " + clipboard)

    if len(printedH) != n:
        return 0

    return operationsPerformed
