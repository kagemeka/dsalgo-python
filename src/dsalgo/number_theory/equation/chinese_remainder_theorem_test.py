import unittest

from dsalgo.number_theory.equation.chinese_remainder_theorem import (
    chinese_remainder_theorem,
    chinese_remainder_theorem_coprime,
)


class Test(unittest.TestCase):
    def test_coprime(self) -> None:
        x = chinese_remainder_theorem_coprime(15, 2, 17, 8)
        self.assertEqual(x % 15, 2)
        self.assertEqual(x % 17, 8)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, 15 * 17)

    def test(self) -> None:
        x = chinese_remainder_theorem(10, 3, 14, 7)
        self.assertIsNotNone(x)
        self.assertEqual(x % 10, 3)
        self.assertEqual(x % 14, 7)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, 10 // 2 * 14)

        x = chinese_remainder_theorem(10, 3, 14, 6)
        self.assertIsNone(x)


if __name__ == "__main__":
    unittest.main()
