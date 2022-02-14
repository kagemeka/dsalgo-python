"""
Number Theory
Equation
"""

import unittest

from dsalgo.number_theory.equation.garner import garner_form, garner_form_mod


class Test(unittest.TestCase):
    def test_form(self) -> None:
        pairs = [
            (15, 2),
            (17, 8),
        ]
        self.assertEqual(
            garner_form(pairs),
            212,
        )

    def test_form_mod(self) -> None:
        pairs = [
            (15, 2),
            (17, 8),
        ]
        self.assertEqual(
            garner_form_mod(998_244_353, pairs),
            212,
        )
        self.assertEqual(
            garner_form_mod(100, pairs),
            12,
        )


if __name__ == "__main__":
    unittest.main()
