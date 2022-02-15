"""
Combinatorics
"""

import typing


def repeated_permutations_dfs(
    n: int,
    repeat: int,
) -> typing.Iterator[typing.Tuple[int, ...]]:
    p: list[int] = [n] * repeat

    def dfs(fixed_count: int) -> typing.Iterator[typing.Tuple[int, ...]]:
        nonlocal p
        if fixed_count == repeat:
            yield tuple(p)
            return
        for i in range(n):
            p[fixed_count] = i
            yield from dfs(fixed_count + 1)

    return dfs(0)
