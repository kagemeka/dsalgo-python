"""
Number Theory
Equation
"""

import unittest

from dsalgo.number_theory.equation.extended_euclidean import (
    extended_euclidean,
    extended_euclidean_recurse,
)


class Test(unittest.TestCase):
    def test_recurse(self) -> None:
        self.assertEqual(
            extended_euclidean_recurse(111, 30),
            (3, 3, -11),
        )

    def test(self) -> None:
        self.assertEqual(
            extended_euclidean(111, 30),
            (3, 3, -11),
        )


if __name__ == "__main__":
    unittest.main()
