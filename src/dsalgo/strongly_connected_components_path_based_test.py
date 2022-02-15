import typing
import unittest

from dsalgo.graph_theory.components.strongly_connected_components.strongly_connected_components_path_based import (
    scc_path_based,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        graph: list[list[int]] = [[1, 3], [2], [3], []]
        labels = scc_path_based(graph)
        self.assertEqual(
            labels,
            [3, 2, 1, 0],
        )


if __name__ == "__main__":
    unittest.main()
