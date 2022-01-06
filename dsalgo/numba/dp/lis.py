import numba as nb
import numpy as np


@nb.njit
def longest_increasing_sequence(a: np.ndarray) -> np.ndarray:
    inf = 1 << 60
    assert inf > a.max()
    lis = np.full(len(a), inf, np.int64)
    for x in a:
        lis[np.searchsorted(lis, x)] = x
    return lis[: np.searchsorted(lis, inf)]
