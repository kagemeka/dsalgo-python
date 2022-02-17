import unittest
import dsalgo.fenwick_tree
import dsalgo.abstract_structure


class TestFenwickTree2D(unittest.TestCase):
    def test(self) -> None:
        monoid = Monoid[int](lambda x, y: x + y, lambda: 0)
        fw = FenwickTree2D(monoid, (4, 5))
        fw.set(1, 2, 1)
        self.assertEqual(fw.get(2, 3), 1)
        fw.set(0, 3, -1)
        fw.set(2, 0, 3)
        self.assertEqual(fw.get(3, 3), 4)
        self.assertEqual(fw.get(2, 4), 0)


class TestFenwickTreeIntAdd2D(unittest.TestCase):
    def test(self) -> None:
        fw = FenwickTreeIntAdd2D((4, 5))
        fw.set(1, 2, 1)
        self.assertEqual(fw.get(2, 3), 1)
        fw.set(0, 3, -1)
        fw.set(2, 0, 3)
        self.assertEqual(fw.get(3, 3), 4)
        self.assertEqual(fw.get(2, 4), 0)


class TestDualFenwickTree(unittest.TestCase):
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


class TestDualFenwickTreeIntAdd(unittest.TestCase):
    def test(self) -> None:
        fw = DualFenwickTreeIntAdd(list(range(5)))
        self.assertEqual(fw[4], 4)
        fw.set(1, 3, 2)
        self.assertEqual(fw[2], 4)


if __name__ == "__main__":
    unittest.main()
