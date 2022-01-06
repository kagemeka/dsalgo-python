from kgmk.dsa.number_theory.sieve_of_eratosthenes.jit import (
    sieve_of_eratosthenes,
    gpf,
    lpf,
)
import numpy as np
import numba as nb


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


if __name__ == '__main__':
    test()
