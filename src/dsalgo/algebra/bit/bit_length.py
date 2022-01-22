import typing


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


def bit_length_table(n: int) -> typing.List[int]:
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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
