import typing

import numba as nb
import numpy as np


@nb.njit
def uf_build(n: int) -> np.ndarray:
    return np.full(n, -1, np.int64)


@nb.njit
def uf_find(uf: np.ndarray, u: int) -> int:
    if uf[u] < 0:
        return u
    uf[u] = uf_find(uf, uf[u])
    return uf[u]


@nb.njit
def uf_unite(uf: np.ndarray, u: int, v: int) -> NoReturn:
    u, v = uf_find(uf, u), uf_find(uf, v)
    if u == v:
        return
    if uf[u] > uf[v]:
        u, v = v, u
    uf[u] += uf[v]
    uf[v] = u
