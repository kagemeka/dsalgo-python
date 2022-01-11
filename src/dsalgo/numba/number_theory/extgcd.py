"""TODO
- non recusive implementation
"""
import typing

import numba as nb


@nb.njit
def extgcd_recurse(a: int, b: int) -> tuple[int, int, int]:
    if not b:
        return a, 1, 0
    g, s, t = extgcd_recurse(b, a % b)
    return g, t, s - a // b * t


@nb.njit
def extgcd(a: int, b: int) -> tuple[int, int, int]:
    x0, x1, x2, x3 = 1, 0, 0, 1
    """
    reference: https://suisen-kyopro.hatenablog.com/entry/2021/04/14/203210

    [x0, x1,
     x2, x3] * [0, 1,
                1, -(a // b)]
    = [x1, x0 - q * x1,
       x3, x2 - q * x3]
    """
    while b:
        q, r = divmod(a, b)
        x0, x1 = x1, x0 - x1 * q
        x2, x3 = x3, x2 - x3 * q
        a, b = b, r
    return a, x0, x2
