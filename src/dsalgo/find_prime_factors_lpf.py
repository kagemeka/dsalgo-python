"""
Number Theory
Prime Number
Prime Factors
"""

import typing

from dsalgo.number_theory.prime_number.finding.least_prime_factor import (
    least_prime_factor,
)


def find_prime_factors_lpf(
    max_value: int,
) -> typing.Callable[[int], typing.List[int]]:
    lpf = least_prime_factor(max_value)

    def find_prime_factors(n: int) -> typing.List[int]:
        primes = [0]
        while n > 1:
            prime = lpf[n]
            n //= prime
            if prime != primes[-1]:
                primes.append(prime)
        return primes[1:]

    return find_prime_factors
