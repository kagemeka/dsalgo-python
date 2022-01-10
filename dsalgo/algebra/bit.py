import functools
import typing


def reverse_bit(n: int) -> int:
    """Reverse bit.

    coming soon.

    Args:
        n (int): [description]

    Returns:
        int: [description]
    """
    ...


def invert_bit(n: int) -> int:
    ...


def reset_least_bit_naive(n: int) -> int:
    """Reset least bit naive.

    Args:
        n (int): an unsined integer.

    Returns:
        int: new bit.

    Examples:
        >>> reset_least_bit_naive(0b0110) == 0b0100
        True

    Complexity:
        time: O(1)
        space: O(1)
    """
    return n - (n & -n)


def reset_least_bit(n: int) -> int:
    """Reset least bit.

    Args:
        n (int): an unsined integer.

    Returns:
        int: new bit.

    Examples:
        >>> reset_least_bit(0b0110) == 0b0100
        True

    Complexity:
        time: O(1)
        space: O(1)
    """
    assert n >= 0
    return n & (n - 1)


def most_significant_bit_naive(n: int) -> typing.Optional[int]:
    """MSB naive.

    Args:
        n (int): an 64bit unsined integer.

    Returns:
        typing.Optional[int]: msb

    Examples:
        >>> most_significant_bit_naive(0b01010)
        3

    Complexity:
        time: O(1)
        space: O(1)
    """
    assert n >= 0
    if n == 0:
        return None
    return bit_length(n) - 1


def most_significant_bit(n: int) -> typing.Optional[int]:
    """MSB.

    Args:
        n (int): an 64bit unsined integer.

    Returns:
        typing.Optional[int]: msb

    Examples:
        >>> most_significant_bit(0b01010)
        3

    Complexity:
        time: O(1)
        space: O(1)
    """
    assert n >= 0
    if n == 0:
        return None
    if n & 0xFFFFFFFF00000000 > 0:
        n &= 0xFFFFFFFF00000000
    if n & 0xFFFF0000FFFF0000 > 0:
        n &= 0xFFFF0000FFFF0000
    if n & 0xFF00FF00FF00FF00 > 0:
        n &= 0xFF00FF00FF00FF00
    if n & 0xF0F0F0F0F0F0F0F0 > 0:
        n &= 0xF0F0F0F0F0F0F0F0
    if n & 0xCCCCCCCCCCCCCCCC > 0:
        n &= 0xCCCCCCCCCCCCCCCC
    if n & 0xAAAAAAAAAAAAAAAA > 0:
        n &= 0xAAAAAAAAAAAAAAAA
    return bit_length(n) - 1


def least_significant_bit(n: int) -> typing.Optional[int]:
    """LSB.

    Args:
        n (int): an 64bit unsined integer.

    Returns:
        typing.Optional[int]: lsb

    Examples:
        >>> least_significant_bit(0b01010)
        1

    Complexity:
        time: O(1)
        space: O(1)
    """
    assert n >= 0
    if n == 0:
        return None
    return bit_length(n & -n) - 1


def bit_length_naive(n: int) -> int:
    r"""Bit length naive.

    Args:
        n (int): an unsigned integer.

    Returns:
        int: bit length.

    Complexity:
        time: O(\log{N})
        space: O(1)
    """
    assert n >= 0
    length = 0
    while 1 << length <= n:
        length += 1
    return length


def bit_length(n: int) -> int:
    r"""Bit length.

    Args:
        n (int): an 64bit unsigned integer.

    Returns:
        int: bit length.

    Complexity:
        time: O(1)
        space: O(1)
    """
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
    """Bit length table.

    Args:
        n (int): an unsigned integer.

    Returns:
        list[int]: bit length table.

    Complexity:
        time: O(N)
        space: O(N)
    """
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
    assert n >= 0, "n must be unsinged integer."
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
    assert n >= 0, "n must be unsinged integer."
    if n == 0:
        return 0
    return popcount_cached(n >> 1) + (n & 1)


def popcount_table(n: int) -> typing.List[int]:
    """Popcount table.

    Args:
        n (int): an unsigned integer.

    Returns:
        typing.List[int]: popcount table.

    Complexity:
        time: O(N)
        space: O(N)
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
