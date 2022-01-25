import unittest

from dsalgo.number_theory.prime_number.prime_factorize_lpf import (
    prime_factorize_lpf,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        prime_factorize = prime_factorize_lpf(max_value=1000)
        self.assertEqual(
            prime_factorize(105),
            [(3, 1), (5, 1), (7, 1)],
        )
        self.assertEqual(
            prime_factorize(100),
            [(2, 2), (5, 2)],
        )


if __name__ == "__main__":
    unittest.main()
