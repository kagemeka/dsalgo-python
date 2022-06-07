import unittest
import typing
from dsalgo.floor_sqrt import floor_sqrt
from dsalgo.sieve_of_eratosthenes import sieve_of_eratosthenes


def range_sieve_of_eratosthenes(
    less_than: int,
) -> typing.Callable[[int, int], list[int]]:
    primes = sieve_of_eratosthenes(floor_sqrt(less_than) + 1)

    def query(lo: int, hi: int) -> list[int]:
        assert lo <= hi <= less_than
        res: list[int] = []
        if hi <= 2:
            return res
        if lo < 2:
            lo = 2
        if lo & 1 == 0:
            if lo == 2:
                res.append(2)
            lo += 1
        if lo == hi:
            return res
        if hi & 1 == 0:
            hi += 1
        size = hi - lo
        size2 = size >> 1
        if_prime = [True] * size2
        for i in primes[1:]:
            mn = i * i
            if mn >= hi:
                break
            mn = max(mn, (lo + i - 1) // i * i)
            if mn & 1 == 0:
                mn += i
            for j in range((mn - lo) >> 1, size2, i):
                if_prime[j] = False
        for i in range(size2):
            if if_prime[i]:
                res.append(lo + (i << 1))
        return res

    return query


# TODO:
class Tests(unittest.TestCase):
    def test(self) -> None:
        ...


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
