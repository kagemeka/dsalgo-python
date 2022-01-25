import unittest

from dsalgo.number_theory.prime_number.find_prime_factors import (
    find_prime_factors,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            find_prime_factors(105),
            [3, 5, 7],
        )


if __name__ == "__main__":
    unittest.main()
