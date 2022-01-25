import typing
import unittest

from dsalgo.graph_theory.shortest_path.error import NegativeCycleError
from dsalgo.graph_theory.shortest_path.johnson_sparse import johnson_sparse


class Test(unittest.TestCase):
    def test(self) -> None:
        graph = [
            [(1, 12), (4, 18)],
            [(0, 12), (2, 14)],
            [(1, 14), (3, 7)],
            [(2, 7), (4, 9)],
            [(0, 18), (3, 9)],
        ]
        dists = johnson_sparse(graph)
        self.assertEqual(
            dists,
            [
                [0, 12, 26, 27, 18],
                [12, 0, 14, 21, 30],
                [26, 14, 0, 7, 16],
                [27, 21, 7, 0, 9],
                [18, 30, 16, 9, 0],
            ],
        )

    def test_negative_cycle(self) -> None:
        graph = [
            [(1, -1)],
            [(2, -1)],
            [(0, -1)],
        ]
        with self.assertRaises(NegativeCycleError):
            johnson_sparse(graph)


if __name__ == "__main__":
    unittest.main()
