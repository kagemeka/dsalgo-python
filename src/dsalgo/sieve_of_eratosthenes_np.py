# mypy: ignore-errors

import numpy as np

import unittest


def sieve_of_eratosthenes(sieve_size: int) -> np.ndarray:
    is_prime = np.ones(sieve_size, dtype=bool)
    is_prime[:2] = False
    is_prime[4::2] = False
    for i in range(3, sieve_size, 2):
        if i * i >= sieve_size:
            break
        if is_prime[i]:
            is_prime[i * i :: i << 1] = False
    return np.flatnonzero(is_prime)


class Test(unittest.TestCase):
    def test(self) -> None:
        sieve_size = 30
        ans = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        res = sieve_of_eratosthenes(sieve_size)
        print(res)
        assert np.all(res == ans)


if __name__ == "__main__":
    import unittest

    unittest.main()
