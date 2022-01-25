import typing

from dsalgo.number_theory.prime_number.sieve_of_eratosthenes import (
    sieve_of_eratosthenes,
)


# https://oeis.org/wiki/Least_prime_factor_of_n
def least_prime_factor(max_value: int) -> typing.List[int]:
    is_prime = sieve_of_eratosthenes(max_value)
    lpf = list(range(max_value))
    for i in range(2, max_value):
        if i * i >= max_value:
            break
        if not is_prime[i]:
            continue
        for j in range(i * i, max_value, i):
            if lpf[j] == j:
                lpf[j] = i
    return lpf
