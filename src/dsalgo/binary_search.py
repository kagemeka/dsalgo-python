from __future__ import annotations

import typing

from dsalgo.type import T


def binary_search(
    is_ok: typing.Callable[[T], bool],
    arr: list[T],
    lo: int = 0,
    hi: int | None = None,
) -> int:
    if hi is None:
        hi = len(arr)
    assert 0 <= lo <= hi <= len(arr)
    while hi - lo > 0:
        i = (lo + hi - 1) >> 1
        if is_ok(arr[i]):
            hi = i
        else:
            lo = i + 1
    return hi


def bisect_left(arr: list[int], x: int) -> int:
    return binary_search(lambda y: y >= x, arr)


def bisect_right(arr: list[int], x: int) -> int:
    return binary_search(lambda y: y > x, arr)
