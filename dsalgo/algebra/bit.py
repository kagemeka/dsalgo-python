import functools
import sys
import typing


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
    r"""Popcount Naive.

    Args:
        n (int): an unsigned integer.

    Returns:
        int: popcount := count of active binary bits.

    Complexity:
        time: O(\log{N})
        space: O(1)

    Examples:
        >>> popcount_naive(0b1010)
        2
        >>> popcount_naive(0b1100100)
        3
        >>> popcount_naive(-1)
        Traceback (most recent call last):
        ...
        AssertionError: n must be unsinged integer.
    """
    assert n >= 0, 'n must be unsinged integer.'
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt


@functools.lru_cache(maxsize=None)
def popcount_cached(n: int) -> int:
    r"""Popcount Cashed.

    Args:
        n (int): an unsigned integer.

    Returns:
        int: popcount := count of active binary bits.

    Complexity:
        time: O(1) amortized.
            best: O(1)
            worst: O(\log{n})
        space: O(max(n))

    Examples:
        >>> popcount_naive(0b1010)
        2
        >>> popcount_naive(0b1100100)
        3
        >>> popcount_naive(-1)
        Traceback (most recent call last):
        ...
        AssertionError: n must be unsinged integer.
    """
    assert n >= 0, 'n must be unsinged integer.'
    if n == 0:
        return 0
    return popcount_cached(n >> 1) + (n & 1)


def popcount_table(n: int) -> typing.List[int]:
    """Popcount table.

    Args:
        n (int): an unsigned integer.

    Returns:
        typing.List[int]: popcount table.
    """
    cnt = [0] * n
    for i in range(n):
        cnt[i] = cnt[i >> 1] + (i & 1)
    return cnt


def popcount(n: int) -> int:
    """Popcount.

    Args:
        n (int): an 64-bit signed or unsigned integer.

    Returns:
        int: popcount := count of active binary bits.

    Complexity:
        time: O(1)
        space: O(1)

    Examples:
        >>> popcount(0b1010)
        2
        >>> popcount(0b1100100)
        3
        >>> popcount(-1)
        64
    """
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0F0F0F0F0F0F0F0F
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007F


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
