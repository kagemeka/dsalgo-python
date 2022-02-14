"""
Number Theory
Prime Number
Prime Factors
"""

import typing

from dsalgo.number_theory.prime_number.finding.find_prime_numbers import (
    find_prime_numbers,
)


def count_prime_factors(max_value: int) -> typing.List[int]:
    count = [0] * max_value
    for p in find_prime_numbers(max_value):
        for i in range(p, max_value, p):
            count[i] += 1
    return count
