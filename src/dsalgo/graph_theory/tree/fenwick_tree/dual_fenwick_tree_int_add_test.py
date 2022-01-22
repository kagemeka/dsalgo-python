import unittest
from dsalgo.graph_theory.tree.fenwick_tree.dual_fenwick_tree_int_add import (
    DualFenwickTreeIntAdd,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        fw = DualFenwickTreeIntAdd(list(range(5)))
        self.assertEqual(fw[4], 4)
        fw.set(1, 3, 2)
        self.assertEqual(fw[2], 4)


if __name__ == "__main__":
    unittest.main()
