import typing
import unittest

from dsalgo.graph_theory.components.strongly_connected_components.strongly_connected_components_kosaraju import (
    scc_kosaraju,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        graph: list[list[int]] = [[1, 3], [2], [3], []]
        labels = scc_kosaraju(graph)
        self.assertEqual(
            labels,
            [0, 1, 2, 3],
        )


if __name__ == "__main__":
    unittest.main()
