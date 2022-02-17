from __future__ import annotations

import math
import typing


def extended_euclidean_mod(mod: int, n: int) -> tuple[int, int]:
    assert mod > 1
    a, b = n % mod, mod
    x00, x01 = 1, 0  # first row of matrix identity element.
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        a, b = b, r
    gcd = a
    if x00 < 0:
        x00 += mod // gcd
    assert 0 <= x00 < mod // gcd
    return gcd, x00


def greatest_common_divisor_recurse(a: int, b: int) -> int:
    return greatest_common_divisor_recurse(b, a % b) if b else a


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def array_gcd(arr: typing.Sequence[int]) -> int | None:
    if len(arr) == 0:
        return None
    gcd = arr[0]
    for x in arr:
        gcd = math.gcd(gcd, x)
    return gcd


def least_common_multiple(a: int, b: int) -> int:
    return 0 if a == b == 0 else a // math.gcd(a, b) * b


import typing


def extended_euclidean_recurse(a: int, b: int) -> tuple[int, int, int]:
    """Compute Extended Euclidean Algorithm.

    Algorithm Summary:
        solve the equation ax + by = gcd(a, b).

        x := bq + r (0 <= r < |b|)
        g := gcd(a, b)
        (bq + r)x + by = g
        b(qx + y) + rx = g
        s := qx + y
        t := x
        bs + rt = g
        ... (recursively)
        when r is 0, then one of the solution is (g, s, t) = (b, 1, 0)
        retrieve (g, x, y) from (g, s, t)
        g = g
        x = t
        y = s - qx = s - qt

    Args:
        a (int): an integer.
        b (int): an integer.

    Returns:
        tuple[int, int, int]:
            return a tuple (gcd(a, b), x, y).
            x, y are not fixed values and also can be negative.
    """
    if not b:
        return a, 1, 0
    gcd, s, t = extended_euclidean_recurse(b, a % b)

    return gcd, t, s - a // b * t


def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    """Compute Extended Euclidean Algorithm.

    Algorithm Summary:
        solve the equation ax + by = gcd(a, b).

        consider matrix product.
        (x, y)^T = A_{k-1}...A_1A_0(1, 0)^T
        k >= 0
        if k == 0, then (x, y)^T = (1, 0)^T
        x_0, y_0 := 1, 0  # one of the solution
        x_k, y_k := x, y
        a_0, b_0 := gcd(a, b), 0  # final state
        a_k, b_k = a, b
        a_i := q_ib_i + r_i (0 <= r_i < |b_i|, 0 < i <= k)

        x_{i-1} := q_ix_i + y_i
        y_{i-1} := x_i
        x_i = 0 + y_{i-1}
        y_i = x_{i-1} - q_iy_{i-1}
        (x_i, y_i)^T := A_{i-1}(x_{i-1}, y_{i-1})^T
        A_{i - 1} = [
            [0, 1],
            [1, -q_i],
        ]

        (x_i, y_i)^T = A_{i-1}...A_1A_0(x_0, x_1)^T

    Args:
        a (int): an integer.
        b (int): an integer.

    Returns:
        tuple[int, int, int]:
            return a tuple (gcd(a, b), x, y).
            x, y are not fixed values and also can be negative.
    """
    x00, x01, x10, x11 = 1, 0, 0, 1  # matrix identity element.
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        x10, x11 = x11, x10 - q * x11
        a, b = b, r
    return a, x00, x10
