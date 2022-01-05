from kagemeka.dsa.jit.graph_theory.euler_tour import (
    euler_tour_edge,
)
import numpy as np
import numba as nb


@nb.njit
def path_on_tree(
    g: np.ndarray,
    edge_idx: np.ndarray,
    src: int,
    dst: int,
) -> np.ndarray:
    _, parent, depth = euler_tour_edge(g, edge_idx, src)
    u = dst
    d = depth[u]
    path = np.empty(d + 1, np.int64)
    for i in range(d + 1):
        path[~i] = u
        u = parent[u]
    return path
