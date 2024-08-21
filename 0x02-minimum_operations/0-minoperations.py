#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """
    Calculates min number of operatons that result
    in exate n & H char in a files
    """
    if (n < 2):
        return 0
    ops, divs = 0, 2
    while divs <= n:
        if n % divs == 0:
            ops += divs
            n = n / divs
            divs -= 1
        divs += 1
    return ops
