import unittest
from dsalgo.graph_theory.tree.fenwick_tree.fenwick_tree import (
    FenwickTreeIntAdd2D,
)


class TestFenwickTreeIndAdd2D(unittest.TestCase):
    def test(self) -> None:
        fw = FenwickTreeIntAdd2D((4, 5))
        fw.set(1, 2, 1)
        self.assertEqual(fw.get(2, 3), 1)
        fw.set(0, 3, -1)
        fw.set(2, 0, 3)
        self.assertEqual(fw.get(3, 3), 4)
        self.assertEqual(fw.get(2, 4), 0)


if __name__ == "__main__":
    unittest.main()
