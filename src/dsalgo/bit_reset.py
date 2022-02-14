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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
