import unittest

from dsalgo.number_theory.prime_number.factors.prime_factorize import (
    prime_factorize,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            prime_factorize(105),
            [(3, 1), (5, 1), (7, 1)],
        )


if __name__ == "__main__":
    unittest.main()
