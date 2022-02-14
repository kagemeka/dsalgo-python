import unittest

from dsalgo.range_query.sparse_table.disjoint_sparse_table_int_sum import (
    disjoint_sparse_table_int_sum,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        a = [3, 1, 2, 10, -1]
        get_sum = disjoint_sparse_table_int_sum(a)
        self.assertEqual(get_sum(0, 5), 15)
        self.assertEqual(get_sum(0, 1), 3)
        self.assertEqual(get_sum(0, 3), 6)


if __name__ == "__main__":
    unittest.main()
