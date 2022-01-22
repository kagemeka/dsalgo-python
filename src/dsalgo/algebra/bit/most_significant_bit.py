import typing


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
    return n.bit_length() - 1


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
    return n.bit_length() - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
