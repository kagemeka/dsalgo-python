import numba as nb
import numpy as np
from kgmk.dsa.number_theory.sieve_of_eratosthenes.jit import (
    gpf, lpf, sieve_of_eratosthenes)


@nb.njit(
    cache=True,
)
def test():
    fn = sieve_of_eratosthenes
    a = fn(1000000)
    print(a)
    print(np.flatnonzero(a))
    a = gpf(10000)
    print(a)
    a = lpf(10000)
    print(a)


if __name__ == "__main__":
    test()
