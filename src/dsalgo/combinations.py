"""
Combinatorics
"""

import typing

from dsalgo.combinatorics.next_combination import next_combination


def combinations(
    n: int,
    k: int,
) -> typing.Generator[typing.Tuple[int, ...], None, None]:
    a = tuple(range(n))
    n = len(a)
    if k < 0 or n < k:
        return
    rng = range(k)
    res = list(rng)
    yield a[:k]
    while True:
        for j in reversed(rng):
            if res[j] != j + n - k:
                break
        else:
            return
        res[j] += 1
        for j in range(j + 1, k):
            res[j] = res[j - 1] + 1
        yield tuple(a[j] for j in res)


def combinations_next_comb(
    n: int,
    k: int,
) -> typing.Generator[typing.Tuple[int, ...], None, None]:
    a = tuple(range(n))
    n = len(a)
    if k < 0 or n < k:
        return
    if k == 0:
        yield ()
        return
    limit = 1 << n
    s = (1 << k) - 1
    while s < limit:
        yield tuple(a[i] for i in range(n) if s >> i & 1)
        s = next_combination(s)
