"""
Tag
- numbe theory
- divisor
"""


import unittest

from dsalgo.number_theory.divisor.find_divisors import find_divisors


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            find_divisors(100),
            [1, 2, 4, 5, 10, 20, 25, 50, 100],
        )


if __name__ == "__main__":
    unittest.main()
