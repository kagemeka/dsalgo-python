import unittest

from dsalgo.number_theory.euclidean.greatest_common_divisor import (
    array_gcd,
    gcd,
)


class Test(unittest.TestCase):
    def test_gcd(self) -> None:
        self.assertEqual(gcd(5, 7), 1)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(4, 0), 4)
        self.assertEqual(gcd(4, 0), gcd(0, 4))
        self.assertEqual(gcd(9, 6), 3)
        self.assertEqual(gcd(0, 0), 0)

    def test_array_gcd(self) -> None:
        self.assertEqual(
            array_gcd([15, 35, 21]),
            1,
        )


if __name__ == "__main__":
    unittest.main()
