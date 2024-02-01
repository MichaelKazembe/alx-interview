#!/usr/bin/python3
"""

"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.

    :param coins: List of coin values
    :param total: Target total amount
    :return: Fewest number of coins needed to meet the total
             or -1 if it cannot be met
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make change for amount 0

    # Update the minimum number of coins for each amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), the total cannot be met by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1
