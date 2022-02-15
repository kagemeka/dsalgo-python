"""
Number Theory
Prime Number
Prime Factors
"""

import typing


def find_prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    i = 1
    while i * i < n:
        i += 1
        if n % i:
            continue
        factors.append(i)
        while n % i == 0:
            n //= i
    if n > 1:
        factors.append(n)
    return factors
