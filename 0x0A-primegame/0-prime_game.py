#!/usr/bin/python3
"""
Module for the Prime Game problem

"""


def is_prime(n):
    """
    Return list of prime numbers between 1 and n inclusive
    Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    # Create a sieve list to mark numbers as prime or not
    sieve = [True] * (n + 1)
    prime_list = []
    for prime in range(2, n + 1):
        if sieve[prime]:  # If the number is marked as prime
            prime_list.append(prime)  # Add it to the prime_list
            # Mark all multiples of the prime number as not prime
            for i in range(prime * prime, n + 1, prime):
                sieve[i] = False
    return prime_list  # Return the list of prime numbers


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (list): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    
    Maria = Ben = 0
    for limit in nums:
        prime_count = len(is_prime(limit))  # Count the number of prime numbers within the limit
        if prime_count % 2 == 0:  # If the count is even
            Ben += 1  # Increment Ben's score
        else:
            Maria += 1  # Increment Maria's score
    
    if Maria > Ben:  # If Maria's score is higher
        return 'Maria'  # Maria wins
    elif Ben > Maria:  # If Ben's score is higher
        return 'Ben'  # Ben wins
    return None  # No winner found
