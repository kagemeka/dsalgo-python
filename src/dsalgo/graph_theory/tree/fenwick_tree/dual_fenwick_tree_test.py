import unittest
from dsalgo.graph_theory.tree.fenwick_tree.dual_fenwick_tree import (
    DualFenwickTree,
)
from dsalgo.algebra.abstract.structure import Group


class Test(unittest.TestCase):
    def test(self) -> None:
        group = Group[int](
            lambda x, y: x + y,
            lambda: 0,
            lambda x: -x,
        )
        fw = DualFenwickTree[int](group, list(range(5)))
        self.assertEqual(fw[4], 4)
        fw.set(1, 3, 2)
        self.assertEqual(fw[2], 4)


if __name__ == "__main__":
    unittest.main()
