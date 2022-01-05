import typing
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8[:]), cache=True)
def next_repeated_permutation(
    n: int,
    a: np.ndarray,
) -> NoReturn:
    for i in range(a.size - 1, -1, -1):
        a[i] += 1
        if a[i] < n:
            return
        a[i] = 0
    a[:] = -1
