import typing

import numba as nb
import numpy as np


@nb.njit
def combinations(n: int, r: int) -> np.ndarray:
    a = np.arange(n)
    ls = []
    if r < 0 or r > n:
        return np.array(ls)
    rng = np.arange(r)[::-1]
    i = np.arange(r)
    ls.append(list(a[:r]))
    while 1:
        for j in rng:
            if i[j] != j + n - r:
                break
        else:
            return np.array(ls)
        i[j] += 1
        for j in range(j + 1, r):
            i[j] = i[j - 1] + 1
        b = []
        for j in i:
            b.append(a[j])
        ls.append(b)
