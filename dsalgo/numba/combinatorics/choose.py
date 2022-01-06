import numba as nb
import numpy as np
from kagemeka.dsa.jit.algebra.modular import (cumprod, factorial,
                                              factorial_inverse)


@nb.njit
def mod_choose(
    mod: int, fact: np.ndarray, ifact: np.ndarray, n: int, k: int
) -> int:
    ok = (0 <= k) & (k <= n)
    return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok


@nb.njit
def mod_choose_inverse(
    mod: int, fact: np.ndarray, ifact: np.ndarray, n: int, k: int
) -> int:
    ok = (0 <= k) & (k <= n)
    return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok


@nb.njit
def mod_nHk(
    mod: int, fact: np.ndarray, ifact: np.ndarray, n: int, k: int
) -> int:
    return mod_choose(n + k - 1, k, mod, fact, ifact)


# nonlocal
def __solve():
    mod = 10 ** 9 + 7
    n = 100
    fact = factorial(mod, n)
    ifact = factorial_inverse(mod, n)

    def mod_choose(n, k):
        nonlocal mod, fact, ifact
        ok = (0 <= k) & (k <= n)
        return fact[n] * ifact[k] % mod * ifact[n - k] % mod * ok

    def mod_choose_inverse(n, k):
        nonlocal mod, fact, ifact
        ok = (0 <= k) & (k <= n)
        return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok

    def mod_nHk(n, k):
        return mod_choose(n + k - 1, k)


import typing


@nb.njit
def pascal_triangle(
    op: typing.Callable[[int, int], int], n: int
) -> np.ndarray:
    choose = np.zeros((n + 1, n + 1), np.int64)
    choose[:, 0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            choose[i, j] = op(choose[i - 1, j], choose[i - 1, j - 1])
    return choose


@nb.njit
def choose_pascal(n: int) -> np.ndarray:
    op = lambda a, b: a + b
    return pascal_triangle(op, n)


@nb.njit
def mod_nchoose_table(mod: int, n: int, k: int) -> np.ndarray:
    a = np.arange(n + 1, n - k, -1)
    a[0] = 1
    cumprod(mod, a)
    return a * inv_factorial(mod, r + 1) % mod


@nb.njit
def nchoose2(n: int) -> int:
    return n * (n - 1) // 2 if n >= 2 else 0
