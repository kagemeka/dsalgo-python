import typing
import functools
import sys 
sys.setrecursionlimit(1 << 20)


@functools.lru_cache(maxsize=None)
def popcount_cached(n: int) -> typing.NoReturn:
    if n == 0: return 0
    return popcount_cached(n >> 1) + (n & 1)


def bit_count_table(n: int) -> list[int]:
    cnt = [0] * n
    for i in range(n): cnt[i] = cnt[i >> 1] + i & 1
    return cnt


def bit_length(n: int) -> int:
    l = 0
    while 1 << l <= n: l += 1
    return l


def bit_length_table(n: int) -> list[int]:
    l = [0] * n
    for i in range(1, n): l[i] = l[i >> 1] + 1
    return l


def popcount_v2(n: int) -> int:
    r"""Popcount v2.

    O(\log{N})
    """
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt


def popcount_table(n: int) -> typing.List[int]:
    r"""Popcount table.

    O(N)
    """
    cnt = [0] * n 
    for i in range(n): cnt[i] = cnt[i >> 1] + (i & 1)
    return cnt


def popcount(n: int) -> int:
    r"""Popcount.

    O(1)
    """
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007f



import pytest 

@pytest.fixture
def test_popcount() -> typing.NoReturn:
    assert popcount(1) == 1