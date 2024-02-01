#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """ Main file for testing """
    # if total is 0 or less, return 0
    if total < 1:
        return 0

    # initialize an array to store the minimum number of coins
    min_coins = [float('inf')] * (total + 1)

    # the minimum number of coins to make 0 is 0
    min_coins[0] = 0

    # loop through the coins
    for coin in coins:
        # loop through the amounts from coin to total
        for amount in range(coin, total + 1):
            # update the minimum number of coins for the current amount
            # by comparing the previous value and the value obtained by
            # using the current coin
            min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    # return the minimum number of coins for the target amount
    return min_coins[total] if min_coins[total] != float('inf') else -1
