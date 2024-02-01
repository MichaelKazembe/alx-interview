#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """ Main file for testing """
    # if total is 0 or less, return 0
    if total <= 0:
        return 0
    ''' initialize an array to store the minimum number of coins
    for each amount the size of the array is total + 1, and the
    initial value is total + 1 this is because the maximum number
    of coins needed to make any amount is total and we want to
    find a smaller value than that '''
    min_coins = [total + 1] * (total + 1)

    ''' the minimum number of coins to make 0 is 0'''
    min_coins[0] = 0

    ''' loop through the coins '''
    for coin in coins:
        # loop through the amounts from coin to total
        for amount in range(coin, total + 1):
            '''update the minimum number of coins for the current amount
            by comparing the previous value and the value obtained by
            using the current coin the value obtained by using the
            current coin is the minimum number of coins for the amount
            minus the coin value plus one (for the current coin)'''
            min_coins[amount] = min(min_coins[amount],
                                    min_coins[amount - coin] + 1)

    '''return the minimum number of coins for the target amount
    if it is equal to total + 1, it means that the amount cannot
    be made by any combination of coins so return -1'''
    return min_coins[total] if min_coins[total] != total + 1 else -1
