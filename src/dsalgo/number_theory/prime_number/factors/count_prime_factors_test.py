import unittest

from dsalgo.number_theory.prime_number.factors.count_prime_factors import (
    count_prime_factors,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            count_prime_factors(20),
            [0, 0, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1],
        )


if __name__ == "__main__":
    unittest.main()
