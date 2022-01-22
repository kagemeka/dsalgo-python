import typing


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
    return (n & -n).bit_length() - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
