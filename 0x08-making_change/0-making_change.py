#!/usr/bin/python3
"""_summary_
"""


def makeChange(coins, total):
    """_summary_

    Args:
                    coins (_type_): _description_
                    total (_type_): _description_
    """
    sorted_coins = sorted(coins, reverse=True)
    operation_count = 0
    amount_left = total

    while amount_left > 0:
        for coin in sorted_coins:
            if coin > amount_left and amount_left != 0:
                return -1
            else:
                divisions = amount_left // coin
                amount_left = amount_left - (divisions * coin)
                operation_count += divisions

    if amount_left > 0:
        return -1

    return operation_count
