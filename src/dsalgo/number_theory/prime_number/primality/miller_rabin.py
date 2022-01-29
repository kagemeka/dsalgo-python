import random
import typing


def _is_trivial_composite(n: int) -> bool:
    assert n >= 1
    return n == 1 or n & 1 == 0 and n != 2


def _is_composite(n: int, base: int) -> bool:
    assert n >= 3
    r, d = 0, n - 1
    while d & 1 == 0:
        r += 1
        d >>= 1
    # n - 1 = d2^r
    x = pow(base, d, n)
    for _ in range(r):
        y = x * x % n
        if y == 1:
            return x != 1 and x != n - 1
        x = y
    return True


def _miller_rabin_fixed_bases(n: int, bases: typing.List[int]) -> bool:
    assert n >= 1
    if _is_trivial_composite(n):
        return False
    if n == 2:
        return True
    for base in bases:
        if _is_composite(n, base):
            return False
    return True


def miller_rabin_test(n: int, check_times: int = 20) -> bool:
    """Miller Rabin Primality Test.

    Args:
        n (int): an natural number.
        check_times (int, optional):
            how many times it shoud be checked?
            Defaults to 20.

    Returns:
        bool: True if n is a pseudo prime else False.
    """
    assert n >= 1
    if n == 1:
        return False
    bases = list(set(random.randint(1, n - 1) for _ in range(check_times)))
    return _miller_rabin_fixed_bases(n, bases)


def miller_rabin_test_32(n: int) -> bool:
    """Miller Rabin Primality Test for 32 bit natural number.

    Args:
        n (int): 32 bit natural number.

    Returns:
        bool: True if n is prime else False.

    References:
    - https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
    """
    BASES: typing.Final[
        typing.Tuple[
            typing.Literal[2],
            typing.Literal[7],
            typing.Literal[61],
        ]
    ] = (2, 7, 61)
    return _miller_rabin_fixed_bases(n, list(BASES))


def miller_rabin_test_64(n: int) -> bool:
    """Miller Rabin Primality Test for 64 bit natural number.

    Args:
        n (int): 64 bit natural number.

    Returns:
        bool: True if n is prime else False.

    References:
    - https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
    """
    BASES: typing.Final[typing.List[int]] = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
    ]
    return _miller_rabin_fixed_bases(n, BASES)


def miller_rabin_test_64_v2(n: int) -> bool:
    """Miller Rabin Primality Test for 64 bit natural number.

    Args:
        n (int): 64 bit natural number.

    Returns:
        bool: True if n is prime else False.

    References:
    - http://miller-rabin.appspot.com/
    """
    BASES: typing.Final[typing.List[int]] = [
        2,
        325,
        9375,
        28178,
        450775,
        9780504,
        1795265022,
    ]
    return _miller_rabin_fixed_bases(n, BASES)
