'''TODO
- search highly composite numbers
'''

import numpy as np
import numba as nb


@nb.njit
def find_divisors(n: int) -> np.ndarray:
    i = np.arange(int(n ** .5)) + 1
    i = i[n % i == 0]
    return np.unique(np.hstack((i, n // i)))
