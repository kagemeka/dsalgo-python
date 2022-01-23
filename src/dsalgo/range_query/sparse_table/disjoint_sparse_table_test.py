import operator
import unittest

from dsalgo.algebra.abstract.structure import Semigroup
from dsalgo.range_query.sparse_table.disjoint_sparse_table import (
    disjoint_sparse_table,
)


class Test(unittest.TestCase):
    def test_min(self) -> None:
        a = [3, 1, 2, 10, -1]
        semigroup = Semigroup[int](op=min)
        get_min = disjoint_sparse_table(semigroup, a)
        self.assertEqual(get_min(0, 5), -1)
        self.assertEqual(get_min(0, 1), 3)
        self.assertEqual(get_min(0, 3), 1)

    def test_sum(self) -> None:
        a = [3, 1, 2, 10, -1]
        semigroup = Semigroup[int](op=operator.add)
        get_sum = disjoint_sparse_table(semigroup, a)
        self.assertEqual(get_sum(0, 5), 15)
        self.assertEqual(get_sum(0, 1), 3)
        self.assertEqual(get_sum(0, 3), 6)

    def test_xor(self) -> None:
        a = [3, 1, 2, 10, 0]
        semigroup = Semigroup[int](op=operator.xor)
        get_xor = disjoint_sparse_table(semigroup, a)
        self.assertEqual(get_xor(0, 5), 10)
        self.assertEqual(get_xor(0, 1), 3)
        self.assertEqual(get_xor(0, 3), 0)


if __name__ == "__main__":
    unittest.main()
