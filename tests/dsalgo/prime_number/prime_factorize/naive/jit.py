import collections
import sys
import typing

import numba as nb
import numpy as np
from kgmk.dsa.number_theory.prime_factorize.naive.jit import (
    prime_factorize, prime_factorize_factorial)


@nb.njit(
    cache=True,
)
def test():
    f = prime_factorize_factorial(1000000)
    print(f)


if __name__ == "__main__":
    test()
