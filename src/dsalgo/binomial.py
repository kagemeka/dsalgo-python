"""
Combinatorics
"""
from __future__ import annotations

import typing

import dsalgo.modular


def make_choose(p: int, n: int) -> typing.Callable[[int, int], int]:
    """Make choose function.

    Args:
        p (int): prime modulo.
        n (int): internal factorial table size.
                returned function can compute at most n-1 choose k.

    Returns:
        typing.Callable[[int, int], int]: choose function.
    """
    fact = dsalgo.modular.factorial(p, n)
    ifact = dsalgo.modular.factorial_inverse(p, n)

    def choose(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k:
            return 0
        return fact[n] * ifact[n - k] % p * ifact[k] % p

    return choose


def make_caching_pascal_choose(
    mod: int | None = None,
) -> typing.Callable[[int, int], int]:
    """Make chasing pascal choose.

    Args:
        mod (typing.Optional[int], optional):
            optional modulo.
            Defaults to None.

    Returns:
        typing.Callable[[int, int], int]: choose function.
    """
    import functools
    import sys

    sys.setrecursionlimit(1 << 20)
    if mod is not None:
        assert mod >= 1

    @functools.lru_cache(maxsize=None)
    def choose(n: int, k: int) -> int:
        if k < 0 or n < k:
            return 0
        if k == 0:
            return 1
        res = choose(n - 1, k) + choose(n - 1, k - 1)
        if mod is not None:
            res %= mod
        return res

    return choose


def n_choose_table(p: int, n: int, kmax: int) -> list[int]:
    """N choose k table for fixed N and small k.

    Args:
        p (int): prime modulo.
        n (int): fixed N.
        kmax (int): max k for N choose k.

    Returns:
        list[int]: result table.
    """
    assert 0 <= kmax <= n
    a = list(range(n + 1, n - kmax, -1))
    a[0] = 1
    a = dsalgo.modular.cumprod(p, a)
    b = dsalgo.modular.factorial_inverse(p, kmax + 1)
    for i in range(kmax + 1):
        a[i] *= b[i]
        a[i] %= p
    return a


def make_count_permutation(p: int, n: int) -> typing.Callable[[int, int], int]:
    """Make count permutation.

    Args:
        p (int): prime modulo.
        n (int): internal factorial table size.
                returned function can compute at most {n-1}P{k} mod p
                that is (n - 1)! / (n - k)! mod p.

    Returns:
        typing.Callable[[int, int], int]: count permutations function.
    """
    fact = dsalgo.modular.factorial(p, n)
    ifact = dsalgo.modular.factorial_inverse(p, n)

    def count_perm(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k:
            return 0
        return fact[n] * ifact[n - k] % p

    return count_perm
