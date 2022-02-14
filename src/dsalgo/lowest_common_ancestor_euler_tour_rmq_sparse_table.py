import typing

from dsalgo.algebra.abstract.abstract_structure import Semigroup
from dsalgo.graph_theory.tree_algo.euler_tour import (
    compute_depth,
    compute_first_index,
    euler_tour,
    to_nodes,
)
from dsalgo.range_query.sparse_table.sparse_table import sparse_table


def lca_euler_tour_rmq(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    tour = euler_tour(tree_edges, root)
    depth = compute_depth(tour)
    tour = to_nodes(tour)
    first_idx = compute_first_index(tour)
    semigroup = Semigroup[typing.Tuple[int, int]](op=min)
    get_min = sparse_table(semigroup, [(depth[i], i) for i in tour])

    def get_lca(u: int, v: int) -> int:
        left, right = first_idx[u], first_idx[v]
        if left > right:
            left, right = right, left
        return get_min(left, right + 1)[1]

    return get_lca
