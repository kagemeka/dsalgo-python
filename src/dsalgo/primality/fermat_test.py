import typing
import unittest

from dsalgo.number_theory.prime_number.primality.fermat import fermat_test


class Test(unittest.TestCase):
    def test(self) -> None:
        for _ in range(100):
            self.assertTrue(fermat_test(998244353))
            self.assertFalse(fermat_test(561, check_times=100))
            self.assertFalse(fermat_test(512461, check_times=200))


if __name__ == "__main__":
    unittest.main()
