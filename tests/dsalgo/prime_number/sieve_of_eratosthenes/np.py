from kgmk.dsa.number_theory.sieve_of_eratosthenes.np import (
    SieveOfEratosthenes,
)
import numpy as np


def test():
    fn = SieveOfEratosthenes()
    a = fn(1000000)
    print(a)
    print(np.flatnonzero(a))
    a = fn.gpf(10000)
    print(a)
    a = fn.lpf(10000)
    print(a)


if __name__ == '__main__':
    test()
