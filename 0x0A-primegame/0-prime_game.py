#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of each game optimally.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n.

    Returns:
        str or None: The name of the player who won the most rounds.
                     Returns "Maria" if Maria wins, "Ben" if Ben wins,
                     or None if the winner cannot be determined.
    """
    def generate_primes_sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        primes = []

        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False

        return primes

    primes = generate_primes_sieve(max(max(nums), 2))
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for p in primes if p <= n)

        # If the number of primes is odd, Maria wins; otherwise, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
