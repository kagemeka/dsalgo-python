import numba as nb
import numpy as np

from ...next_permutation.jit import next_permutation

# TODO cut below


@nb.njit
def permutations(
    n: int,
) -> np.array:
    a = np.arange(n)
    m = np.prod(a + 1)
    b = np.zeros(
        shape=(m, n),
        dtype=np.int64,
    )
    for i in range(m):
        b[i] = a
        a = next_permutation(a)
    return b
