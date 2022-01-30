import unittest

from dsalgo.number_theory.euclidean.greatest_common_divisor import (
    array_gcd,
    greatest_common_divisor,
)


class Test(unittest.TestCase):
    def test_gcd(self) -> None:
        self.assertEqual(greatest_common_divisor(5, 7), 1)
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(4, 0), 4)
        self.assertEqual(
            greatest_common_divisor(4, 0), greatest_common_divisor(0, 4)
        )
        self.assertEqual(greatest_common_divisor(9, 6), 3)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_array_gcd(self) -> None:
        self.assertEqual(
            array_gcd([15, 35, 21]),
            1,
        )


if __name__ == "__main__":
    unittest.main()
