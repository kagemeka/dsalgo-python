import unittest

from dsalgo.algebra.numeral_system import (
    base_convert_from_ten,
    base_convert_to_ten,
)


class TestClass(unittest.TestCase):
    def test_base_convert_from_ten(self) -> None:
        self.assertEqual(
            base_convert_from_ten(2, 10),
            [0, 1, 0, 1],
        )
        self.assertEqual(
            base_convert_from_ten(-2, 10),
            [0, 1, 1, 1, 1],
        )
        with self.assertRaises(AssertionError):
            base_convert_from_ten(-1, 10)

    def test_base_convert_to_ten(self) -> None:
        self.assertEqual(
            base_convert_to_ten(2, [0, 1, 0, 1]),
            10,
        )
        self.assertEqual(
            base_convert_to_ten(-2, [0, 1, 1, 1, 1]),
            10,
        )
        with self.assertRaises(AssertionError):
            base_convert_to_ten(-1, [0, 1, 0, 1])


if __name__ == "__main__":
    unittest.main()
