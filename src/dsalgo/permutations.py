"""
Combinatorics
"""

import typing

from dsalgo.combinatorics.next_permutation import next_permutation


def permutations(
    n: int,
    k: typing.Optional[int] = None,
) -> typing.Iterator[typing.Tuple[int, ...]]:
    if k is None:
        k = n
    if k < 0 or n < k:
        return
    indices = list(range(n))
    cycles = list(range(k))
    yield tuple(indices[:k])
    while True:
        for i in reversed(range(k)):
            cycles[i] += 1
            if cycles[i] == n:
                indices[i:] = indices[i + 1 :] + indices[i : i + 1]
                cycles[i] = i
                continue
            j = cycles[i]
            indices[i], indices[j] = indices[j], indices[i]
            yield tuple(indices[:k])
            break
        else:
            return


def permutations_dfs(
    n: int,
    k: typing.Optional[int] = None,
) -> typing.Iterator[typing.Tuple[int, ...]]:
    if k is None:
        k = n
    indices = list(range(n))

    def dfs(left: int) -> typing.Iterator[typing.Tuple[int, ...]]:
        nonlocal indices, n, k
        if left == k:
            yield tuple(indices[:k])
            return
        for i in range(left, n):
            indices[left], indices[i] = indices[i], indices[left]
            yield from dfs(left + 1)
            indices[left], indices[i] = indices[i], indices[left]

    return dfs(0)


def permutations_next_perm(n: int) -> typing.Iterator[typing.Tuple[int, ...]]:
    arr: typing.Optional[typing.List[int]] = list(range(n))
    while arr is not None:
        yield tuple(arr)
        arr = next_permutation(arr)
