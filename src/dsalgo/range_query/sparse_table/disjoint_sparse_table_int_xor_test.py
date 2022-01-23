import unittest

from dsalgo.range_query.sparse_table.disjoint_sparse_table_int_xor import (
    disjoint_sparse_table_int_xor,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        a = [3, 1, 2, 10, 0]
        get_xor = disjoint_sparse_table_int_xor(a)
        self.assertEqual(get_xor(0, 5), 10)
        self.assertEqual(get_xor(0, 1), 3)
        self.assertEqual(get_xor(0, 3), 0)


if __name__ == "__main__":
    unittest.main()
