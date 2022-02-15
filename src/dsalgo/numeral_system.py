"""
Numeral System
"""

import typing


def base_convert_to_ten(
    base: int,
    digits: list[int],
) -> int:
    """Convert digits to base ten integer.

    Args:
        base (int): original base.
        digits (list[int]): digits.

    Returns:
        int: base ten integer.


    Examples:
        >>> digits = [0, 1, 1]
        >>> base_convert_to_ten(2, digits)
        6
    """
    assert abs(base) >= 2
    p = 1
    n = 0
    for d in digits:
        n += d * p
        p *= base
    return n


def base_convert_from_ten(
    base: int,
    n: int,
) -> list[int]:
    """Convert base ten integer to arbitral base digits.

    Args:
        base (int): target base.
        n (int): base ten integer.

    Returns:
        list[int]: result digits.

    Examples:
        >>> base_convert_from_ten(-2, 10)
        [0, 1, 1, 1, 1]
    """
    assert abs(base) >= 2
    if n == 0:
        return [0]
    digits = []
    while n:
        n, r = divmod(n, base)
        if r < 0:
            r -= base
            n += 1
        digits.append(r)
    return digits


def base_convert(
    b0: int,
    b1: int,
    digits: list[int],
) -> list[int]:
    """Convert digits base from b0 to b1.

    Args:
        b0 (int): original base.
        b1 (int): target base.
        digits (list[int]): original digits.

    Returns:
        list[int]: target digits.
    """
    return base_convert_from_ten(
        b1,
        base_convert_to_ten(b0, digits),
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
