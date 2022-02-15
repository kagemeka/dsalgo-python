import functools
import typing


def reverse_bit(n: int) -> int:
    ...


def reset_least_bit_naive(n: int) -> int:
    """
    Examples:
        >>> reset_least_bit_naive(0b0110) == 0b0100
        True
    """
    return n - (n & -n)


def reset_least_bit(n: int) -> int:
    """
    Examples:
        >>> reset_least_bit(0b0110) == 0b0100
        True
    """
    assert n >= 0
    return n & (n - 1)


def bit_length_std(n: int) -> int:
    return n.bit_length()


def bit_length_naive(n: int) -> int:
    assert n >= 0
    length = 0
    while 1 << length <= n:
        length += 1
    return length


def bit_length(n: int) -> int:
    assert n >= 0
    if n == 0:
        return 0
    length = 1
    for i in range(5, -1, -1):
        i = 1 << i
        if n >> i == 0:
            continue
        length += i
        n >>= i
    return length


def bit_length_table(n: int) -> list[int]:
    length = [0] * n
    for i in range(1, n):
        length[i] = length[i >> 1] + 1
    return length


def invert_bit(n: int) -> int:
    ...


def popcount_naive(n: int) -> int:
    """
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
    assert n >= 0, "n must be unsinged integer."
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt


@functools.lru_cache(maxsize=None)
def popcount_cached(n: int) -> int:
    r"""Popcount Cashed.

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
    assert n >= 0, "n must be unsinged integer."
    if n == 0:
        return 0
    return popcount_cached(n >> 1) + (n & 1)


def popcount_table(n: int) -> list[int]:
    cnt = [0] * n
    for i in range(n):
        cnt[i] = cnt[i >> 1] + (i & 1)
    return cnt


def popcount(n: int) -> int:
    """
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


def define_popcount(mask_size: int = 8) -> typing.Callable[[int], int]:
    count_table = popcount_table(1 << mask_size)
    mask = (1 << mask_size) - 1

    def popcount(n: int) -> int:
        count = 0
        while n:
            count += count_table[n & mask]
            n >>= mask_size
        return count

    return popcount


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
