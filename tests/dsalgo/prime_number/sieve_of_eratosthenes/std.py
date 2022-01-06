from kgmk.dsa.number_theory.sieve_of_eratosthenes import (
    SieveOfEratosthenes,
)


def test():
    fn = SieveOfEratosthenes()
    a = fn(1000000)
    print(a[:10])
    a = fn.gpf(10000)
    print(a[:10])
    a = fn.lpf(10000)
    print(a[:10])


if __name__ == '__main__':
    test()
