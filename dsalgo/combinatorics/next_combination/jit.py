import numba as nb


@nb.njit
def next_combination(s: int) -> int:
    i = s & -s
    j = s + i
    return (s & ~j) // i >> 1 | j
