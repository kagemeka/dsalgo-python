import typing

from dsalgo.number_theory.prime_number.find_prime_factors_lpf import (
    find_prime_factors_lpf,
)


def euler_totient_lpf(
    max_value: int,
) -> typing.Callable[[int], int]:
    find_prime_factors = find_prime_factors_lpf(max_value)

    def euler_totient(n: int) -> int:
        count = n
        for p in find_prime_factors(n):
            count = count // p * (p - 1)
        return count

    return euler_totient
