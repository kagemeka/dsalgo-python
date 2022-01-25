import unittest

from dsalgo.algebra.abstract.structure import Monoid
from dsalgo.combinatorics.pascal import pascal_triangle

CHOOSE_TABLE_5 = [
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 2, 1, 0, 0],
    [1, 3, 3, 1, 0],
    [1, 4, 6, 4, 1],
]


class Test(unittest.TestCase):
    def test(self) -> None:
        monoid = Monoid[int](lambda x, y: x + y, lambda: 0)
        self.assertEqual(
            pascal_triangle(monoid, lambda: 1, 5),
            CHOOSE_TABLE_5,
        )


if __name__ == "__main__":
    unittest.main()
