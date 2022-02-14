import unittest

from dsalgo.algebra.abstract.abstract_structure import Semigroup
from dsalgo.range_query.sparse_table.sparse_table import sparse_table


class Test(unittest.TestCase):
    def test_min(self) -> None:
        a = [3, 1, 2, 10, -1]
        semigroup = Semigroup[int](op=min)
        get_min = sparse_table(semigroup, a)
        self.assertEqual(get_min(0, 5), -1)
        self.assertEqual(get_min(0, 1), 3)
        self.assertEqual(get_min(0, 3), 1)


if __name__ == "__main__":
    unittest.main()
