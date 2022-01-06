import numba as nb
import numpy as np


@nb.njit
def bit_length(n: int) -> int:
    r"""Bit Length.

    O(\log{N})
    """
    l = 0
    while 1 << l <= n:
        l += 1
    return l


@nb.njit
def bit_length_table(n: int) -> np.ndarray:
    r"""Bit Length table.

    O(N)
    """
    l = np.zeros(n, np.int64)
    for i in range(1, n):
        l[i] = l[i >> 1] + 1
    return l


@nb.njit
def popcount_v2(n: int) -> int:
    r"""Popcount v2.

    O(\log{N})
    """
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt


@nb.njit
def popcount_table(n: int) -> np.ndarray:
    r"""Popcount table.

    O(N)
    """
    cnt = np.zeros(n, np.int64)
    for i in range(n):
        cnt[i] = cnt[i >> 1] + i & 1
    return cnt


@nb.njit
def popcount(n: int) -> int:
    r"""Popcount.

    O(1)
    """
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0F0F0F0F0F0F0F0F
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007F
