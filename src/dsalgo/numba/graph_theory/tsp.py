import numba as nb
import numpy as np


@nb.njit
def tsp_dense(g: np.ndarray, src: int) -> int:
    n = len(g)
    assert g.shape == (n, n)
    inf = 1 << 60
    assert inf > g.sum()
    dist = np.full((1 << n, n), inf, np.int64)
    dist[1 << src, src] = 0
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            for j in range(n):
                if s >> j & 1:
                    continue
                u = s | 1 << j
                dist[u, j] = min(dist[u, j], dist[s, i] + g[i, j])
    return np.amin(dist[-1] + g[:, src])


@nb.njit
def tsp_sparse(n: int, g: np.ndarray, src: int) -> int:
    m = len(g)
    assert g.shape == (m, 3)
    inf = 1 << 60
    assert inf > g[:, 2].sum()
    sort_idx = np.argsort(g[:, 0], kind="mergesort")
    g = g[sort_idx]
    idx = np.searchsorted(g[:, 0], np.arange(n + 1))
    dist = np.full((1 << n, n), inf, np.int64)
    dist[1 << src, src] = 0
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            for k in range(idx[i], idx[i + 1]):
                _, j, w = g[k]
                if s >> j & 1:
                    continue
                u = s | 1 << j
                dist[u, j] = min(dist[u, j], dist[s, i] + w)
    mn = inf
    for i in range(n):
        if i == src:
            continue
        for k in range(idx[i], idx[i + 1]):
            _, j, w = g[k]
            if j != src:
                continue
            mn = min(mn, dist[-1, i] + w)
    return mn
