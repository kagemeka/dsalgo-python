"""
Number Theory
Euclidean
"""

import unittest

from dsalgo.number_theory.euclidean.least_common_multiple import (
    least_common_multiple,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        self.assertEqual(least_common_multiple(0, 0), 0)
        self.assertEqual(least_common_multiple(0, 10), 0)
        self.assertEqual(least_common_multiple(10, 0), 0)
        self.assertEqual(least_common_multiple(9, 6), 18)


if __name__ == "__main__":
    unittest.main()
