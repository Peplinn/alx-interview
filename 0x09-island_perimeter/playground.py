#!/usr/bin/python3
"""_summary_
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): Target amount.

    Returns:
        int: Fewest number of coins needed to meet the total, or -1 if impossible.
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    operation_count = 0
    amount_left = total

    for coin in sorted_coins:
        if amount_left == 0:
            break

        if coin <= amount_left:
            divisions = amount_left // coin
            amount_left -= divisions * coin
            operation_count += divisions

    return operation_count if amount_left == 0 else -1
