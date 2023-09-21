#!/usr/bin/python3
"""
Making changes comes from within
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each amount
    # Initialize it with a value that represents infinity (unreachable)
    dp = [float('inf')] * (total + 1)

    # The minimum number of coins needed to make change for 0 is 0
    dp[0] = 0

    # Iterate through all coin values
    for coin in coins:
        # Update dp[i] for all values i from coin to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
