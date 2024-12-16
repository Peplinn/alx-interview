#!/usr/bin/python3
"""
Prime Game: Determines the winner after multiple rounds.
"""

def isWinner(x, nums):
    """
    Determines the overall winner of the Prime Game.

    Args:
        x (int): Total number of rounds played.
        nums (list[int]): List containing the upper bounds for each round.

    Returns:
        str: Name of the player who wins the most rounds ('Maria' or 'Ben'),
        or None if there is no clear winner.
    """
    if x < 1 or not nums:
        return None

    maria_score = 0
    ben_score = 0

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False

    for n in nums:
        prime_count = sum(sieve[2:n+1])
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score == ben_score:
        return None
    return 'Maria' if maria_score > ben_score else 'Ben'
