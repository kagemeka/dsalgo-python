import typing

from dsalgo.number_theory.prime_number.sieve_of_eratosthenes import (
    sieve_of_eratosthenes,
)


def is_prime_table(max_value: int) -> typing.List[bool]:
    return sieve_of_eratosthenes(max_value)
