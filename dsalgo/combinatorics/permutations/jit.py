import typing

import numba as nb
import numpy as np


@nb.njit
def permutations(
    n: int,
    r: typing.Optional[int] = None,
) -> np.array:
    if r is None:
        r = n
    ls = []
    if r < 0 or r > n:
        return np.array(ls)
    i = np.arange(n)
    rng = np.arange(r)[::-1]
    c = np.arange(r)
    ls.append(list(i[:r]))
    while 1:
        for j in rng:
            c[j] += 1
            if c[j] == n:
                x = i[j]
                i[j:-1] = i[j + 1 :]
                i[-1] = x
                c[j] = j
                continue
            k = c[j]
            i[j], i[k] = i[k], i[j]
            ls.append(list(i[:r]))
            break
        else:
            return np.array(ls)
