from __future__ import annotations

import dataclasses
import typing

import dsalgo.fenwick_tree
from dsalgo.type import T


def argmax(arr: list[int]) -> int | None:
    if len(arr) == 0:
        return None
    idx, max_value = 0, arr[0]
    for i, x in enumerate(arr):
        if x > max_value:
            idx, max_value = i, x
    return idx


def bincount(arr: list[int]) -> list[int]:
    cnt = [0] * (max(arr) + 1)
    for x in arr:
        cnt[x] += 1
    return cnt


@dataclasses.dataclass
class CompressionResult:
    compressed: list[int]
    retrieve: list[int]


def compress(arr: list[int]) -> CompressionResult:
    import bisect

    v = sorted(set(arr))
    return CompressionResult(
        [bisect.bisect_left(v, x) for x in arr],
        v,
    )


def compute_inversion_number(arr: list[int]) -> int:
    arr = compress(arr).compressed
    fw = dsalgo.fenwick_tree.FenwickTreeIntAdd([0] * len(arr))
    count = 0
    for i, x in enumerate(arr):
        count += i - fw[x]
        fw[x] = 1
    return count


def flatnonzero(arr: list[bool]) -> list[int]:
    return [i for i, x in enumerate(arr) if x]


def accumulate(
    identity_element: T,
) -> typing.Callable[
    [typing.Callable[[T, T], T]],
    typing.Callable[[typing.Iterable[T]], T],
]:
    def decorate(
        op: typing.Callable[[T, T], T],
    ) -> typing.Callable[[typing.Iterable[T]], T]:
        import functools

        def wrapped(arr: typing.Iterable[T]) -> T:
            return functools.reduce(op, arr, identity_element)

        return wrapped

    return decorate


# @accumulate(0)
# def xor(a: int, b: int) -> int:
#     return a ^ b
