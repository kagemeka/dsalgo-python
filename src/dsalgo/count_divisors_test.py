"""
Tag
- numbe theory
- divisor
"""


import unittest

from dsalgo.number_theory.divisor.count_divisors import count_divisors


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            count_divisors(20),
            [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2],
        )


if __name__ == "__main__":
    unittest.main()
