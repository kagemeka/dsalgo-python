import numba as nb
import numpy as np


@nb.njit
def repeated_combinations(n: int, k: int) -> np.ndarray:
    assert k >= 1
    res = np.empty((1 << 20, k), np.int64)
    idx_to_add = 0

    def add_result(a):
        nonlocal idx_to_add
        res[idx_to_add] = a
        idx_to_add += 1

    que = [(np.zeros(k, np.int64), 0)]
    for a, i in que:
        if i == k:
            add_result(a)
            continue
        for j in range(a[i - 1], n):
            b = a.copy()
            b[i] = j
            que.append((b, i + 1))
    return res[:idx_to_add]
