import typing

from dsalgo.number_theory.prime_number.find_prime_factors import (
    find_prime_factors,
)


def euler_totient(n: int) -> int:
    count = n
    for p in find_prime_factors(n):
        count = count // p * (p - 1)
    return count
