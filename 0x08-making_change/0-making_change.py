#!/usr/bin/python3
"""
Making changes
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins
    """
    if total <= 0:
        return 0
    remaining = total
    count_coins = 0
    j = 0
    k = sorted(coins, reverse=True)
    i = len(coins)
    while remaining > 0:
        if j >= i:
            return -1
        if remaining - k[j] >= 0:
            remaining -= k[j]
            count_coins += 1
        else:
            j += 1
    return count_coins
