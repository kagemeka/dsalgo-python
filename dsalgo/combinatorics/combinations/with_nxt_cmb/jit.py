import numba as nb
import numpy as np

from ...next_combination.jit import next_combination

# TODO cut below


@nb.jit
def combinations(
    n: int,
    r: int,
) -> np.array:
    ls = []
    if r < 0 or r > n:
        return np.array(ls)
    lim = 1 << n
    s = (1 << r) - 1
    i = np.arange(n)
    while s < lim:
        j = np.flatnonzero(
            s >> i & 1,
        )
        ls.append(list(j))
        if s == 0:
            break
        s = next_combination(s)
    return np.array(ls)
