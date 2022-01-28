import typing

from dsalgo.number_theory.prime_number.finding.least_prime_factor import (
    least_prime_factor,
)


# https://oeis.org/wiki/Greatest_prime_factor_of_n
def greatest_prime_factor(n: int) -> typing.List[int]:
    lpf = least_prime_factor(n)
    gpf = list(range(n))
    for i in range(2, n):
        if lpf[i] == i:
            continue
        gpf[i] = gpf[i // lpf[i]]
    return gpf
