import unittest

from dsalgo.graph_theory.shortest_path.shortest_path_error import (
    NegativeCycleError,
)
from dsalgo.graph_theory.shortest_path.shortest_path_floyd_warshall import (
    floyd_warshall,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        graph = [
            [None, 12, None, None, 18],
            [12, None, 14, None, None],
            [None, 14, None, 7, None],
            [None, None, 7, None, 9],
            [18, None, None, 9, None],
        ]
        dists = floyd_warshall(graph)
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
        graph = [[None, -1, None], [None, None, -1], [-1, None, None]]
        with self.assertRaises(NegativeCycleError):
            floyd_warshall(graph)


if __name__ == "__main__":
    unittest.main()
