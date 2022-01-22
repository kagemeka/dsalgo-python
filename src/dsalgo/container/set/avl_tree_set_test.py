import unittest

from dsalgo.container.set.avl_tree_set import AVLTreeSet


class Test(unittest.TestCase):
    def test_insert(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        self.assertEqual(
            list(s),
            [1],
        )
        s.insert(-1)
        self.assertEqual(
            list(s),
            [-1, 1],
        )
        s.insert(1)
        self.assertEqual(
            list(s),
            [-1, 1],
        )

    def test_iter(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        s.insert(0)
        s.insert(3)
        self.assertEqual(
            list(s),
            [0, 1, 3],
        )

    def test_remove(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        s.insert(0)
        s.insert(3)
        s.remove(1)
        self.assertEqual(
            list(s),
            [0, 3],
        )

    def test_min(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        s.insert(0)
        s.insert(3)
        self.assertEqual(
            s.min(),
            0,
        )

    def test_max(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        s.insert(0)
        s.insert(3)
        self.assertEqual(
            s.max(),
            3,
        )

    def test_lower_bound(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        s.insert(0)
        s.insert(3)
        s.insert(4)
        self.assertEqual(
            s.lower_bound(2),
            2,
        )
        self.assertEqual(
            s.lower_bound(5),
            4,
        )
        self.assertEqual(
            s.lower_bound(4),
            3,
        )
        self.assertEqual(
            s.lower_bound(-1),
            0,
        )

    def test_upper_bound(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        s.insert(0)
        s.insert(3)
        s.insert(4)
        self.assertEqual(
            s.upper_bound(2),
            2,
        )
        self.assertEqual(
            s.upper_bound(5),
            4,
        )
        self.assertEqual(
            s.upper_bound(4),
            4,
        )
        self.assertEqual(
            s.upper_bound(-1),
            0,
        )

    def test_getitem(self) -> None:
        s = AVLTreeSet[int]()
        s.insert(1)
        s.insert(0)
        s.insert(3)
        self.assertEqual(
            s[2],
            3,
        )
        with self.assertRaises(AssertionError):
            s[3]

    def test_len(self) -> None:
        s = AVLTreeSet[int]()
        for i in range(5):
            s.insert(i)
        self.assertEqual(
            len(s),
            5,
        )
        s.insert(4)
        self.assertEqual(
            len(s),
            5,
        )
        s.remove(1)
        self.assertEqual(
            len(s),
            4,
        )

    def test_contains(self) -> None:
        s = AVLTreeSet[int]()
        for i in range(5):
            s.insert(i)
        self.assertTrue(4 in s)
        s.insert(4)
        self.assertFalse(5 in s)
        s.remove(4)
        self.assertFalse(4 in s)


if __name__ == "__main__":
    unittest.main()
