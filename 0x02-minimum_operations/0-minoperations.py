#!/usr/bin/python3

"""
A method that calculate fewest number of operations
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates
    the fewest number of operations needed to result
    in exactly n H characters in the file.

    Returns an integer
    If n is impossible to achieve, return 0
    """
    if not isinstance(n, int):
        return 0

    op = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            op += i
            i = 1
        i += 1
    return op
