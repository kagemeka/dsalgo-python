import typing

from dsalgo.number_theory.prime_number.sieve_of_eratosthenes import (
    sieve_of_eratosthenes,
)


def find_prime_numbers(max_value: int) -> typing.List[int]:
    is_prime = sieve_of_eratosthenes(max_value)
    return [i for i in range(max_value) if is_prime[i]]
