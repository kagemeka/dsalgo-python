"""
Graph Theory
"""

import typing

from dsalgo.graph_theory.tree_algo.heavy_light_decomposition import (
    compute_roots,
    heavy_light_decompose,
)
from dsalgo.graph_theory.tree_algo.tree_bfs import tree_bfs


def lca_hld(
    tree_edges: list[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    parent, depth = tree_bfs(tree_edges, root)
    labels = heavy_light_decompose(tree_edges, root)
    roots = compute_roots(tree_edges, root, labels)
    roots = [roots[label] for label in labels]

    def get_lca(u: int, v: int) -> int:
        while True:
            if roots[u] == roots[v]:
                return u if depth[u] <= depth[v] else v
            if depth[roots[u]] > depth[roots[v]]:
                u, v = v, u
            v = parent[roots[v]]

    return get_lca
