import numba as nb
import numpy as np


@nb.njit((nb.i8, nb.i8), cache=True)
def repeated_permutations(n: int, k: int) -> np.ndarray:
    res = np.empty((n ** k, k), np.int64)
    idx_to_add = 0

    def add_result(a):
        nonlocal idx_to_add
        res[idx_to_add] = a
        idx_to_add += 1

    st = [(np.empty(k, np.int64), 0)]
    while st:
        a, i = st.pop()
        if i == k:
            add_result(a)
            continue
        for j in range(n):
            b = a.copy()
            b[i] = j
            st.append((b, i + 1))
    return res[::-1]
