import functools
import sys
import typing

import pytest

sys.setrecursionlimit(1 << 20)


def bit_length_naive(n: int) -> int:
    length = 0
    while 1 << length <= n:
        length += 1
    return length


def bit_length_table(n: int) -> list[int]:
    length = [0] * n
    for i in range(1, n):
        length[i] = length[i >> 1] + 1
    return length


def popcount_naive(n: int) -> int:
    r"""Popcount naive.

    O(\log{N})
    """
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt


@functools.lru_cache(maxsize=None)
def popcount_cached(n: int) -> int:
    if n == 0:
        return 0
    return popcount_cached(n >> 1) + (n & 1)


def popcount_table(n: int) -> typing.List[int]:
    r"""Popcount table.

    O(N)
    """
    cnt = [0] * n
    for i in range(n):
        cnt[i] = cnt[i >> 1] + (i & 1)
    return cnt


def popcount(n: int) -> int:
    r"""Popcount.

    O(1)
    """
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0F0F0F0F0F0F0F0F
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007F


@pytest.fixture
def test_popcount() -> typing.NoReturn:
    assert popcount(1) == 1
