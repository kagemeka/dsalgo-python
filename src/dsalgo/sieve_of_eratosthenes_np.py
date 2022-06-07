# mypy: ignore-errors

import numpy as np

import unittest


def sieve_of_eratosthenes(sieve_size: int) -> np.ndarray:
    if sieve_size <= 2:
        return np.array()
    is_prime = np.ones(sieve_size >> 1, dtype=bool)
    is_prime[0] = False
    for i in range(3, sieve_size, 2):
        if i * i >= sieve_size:
            break
        if is_prime[i >> 1]:
            is_prime[i * i >> 1 :: i] = False
    return np.hstack((np.array([2]), np.flatnonzero(is_prime) << 1 | 1))


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
