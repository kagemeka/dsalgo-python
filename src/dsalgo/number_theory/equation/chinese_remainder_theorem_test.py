import unittest
from dsalgo.number_theory.equation.chinese_remainder_theorem import (
    chinese_remainder_theorem_coprime,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        x = chinese_remainder_theorem_coprime(15, 2, 17, 8)
        self.assertEqual(x % 15, 2)
        self.assertEqual(x % 17, 8)
        self.assertGreaterEqual(x, 0)
        self.assertLess(x, 15 * 17)


if __name__ == "__main__":
    unittest.main()
