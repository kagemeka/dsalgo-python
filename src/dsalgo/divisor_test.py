"""
Tag
- numbe theory
- divisor
"""


import unittest

from dsalgo.number_theory.divisor.count_divisors import count_divisors


class TestCountDivisors(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            count_divisors(20),
            [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2],
        )


if __name__ == "__main__":
    unittest.main()


"""
Tag
- numbe theory
- divisor
"""


import unittest

from dsalgo.number_theory.divisor.find_divisors import find_divisors


class TestFindDivisors(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(
            find_divisors(100),
            [1, 2, 4, 5, 10, 20, 25, 50, 100],
        )


if __name__ == "__main__":
    unittest.main()
