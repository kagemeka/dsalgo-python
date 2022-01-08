import typing
from dsalgo.algebra.modular import (
    factorial,
    factorial_inverse,
    cumprod,
)


def make_choose(p: int, n: int) -> typing.Callable[[int, int], int]:
    fact = factorial(p, n)
    ifact = factorial_inverse(p, n)

    def choose(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k:
            return 0
        return fact[n] * ifact[n - k] % p * ifact[k] % p

    return choose



def make_caching_pascal_choose(
    mod: typing.Optional[int]=None,
) -> typing.Callable[[int, int], int]:
    import sys
    import functools 
    sys.setrecursionlimit(1 << 20)
    assert mod >= 1
    
    @functools.lru_cache(maxsize=None)
    def choose(n: int, k: int) -> int:
        if k < 0 or n < k: return 0
        if k == 0: return 1
        res = choose(n - 1, k) + choose(n - 1, k - 1)
        if mod is not None: res %= mod
        return res

    return choose


def n_choose_table(p: int, n: int, kmax: int) -> typing.List[int]:
    assert 0 <= kmax <= n
    a = list(range(n + 1, n - kmax, -1))
    a[0] = 1
    a = cumprod(p, a)
    b = factorial_inverse(p, kmax + 1)
    for i in range(kmax + 1):
        a[i] *= b[i]
        a[i] %= p
    return a



def make_count_permutation(p: int, n: int) -> typing.Callable[[int, int], int]:
    fact = factorial(p, n)
    ifact = factorial_inverse(p, n)

    def count_perm(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k:
            return 0
        return fact[n] * ifact[n - k] % p

    return count_perm