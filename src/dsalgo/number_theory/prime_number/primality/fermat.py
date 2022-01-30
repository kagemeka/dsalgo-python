import math
import random


def fermat_test(n: int, check_times: int = 100) -> bool:
    """Fermat Primality Test.

    Args:
        n (int): a natural number.
        check_times (int, optional):
            how many times it should be checked?
            (for detail https://en.wikipedia.org/wiki/Fermat_primality_test)
            Defaults to 100.

    Returns:
        bool:
            when False, n is a composite number.
            when True, n is a pseudo prime,
            which is almost prime but might not be.
            it return necessarily True for a prime number.

    References:
    - https://en.wikipedia.org/wiki/Fermat_primality_test
    - https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A7%E3%83%AB%E3%83%9E%E3%83%BC%E3%81%AE%E5%B0%8F%E5%AE%9A%E7%90%86#%E3%83%95%E3%82%A7%E3%83%AB%E3%83%9E%E3%83%BC%E3%83%86%E3%82%B9%E3%83%88
    - https://qiita.com/srtk86/items/609737d50c9ef5f5dc59
    - https://ja.wikipedia.org/wiki/%E3%82%AB%E3%83%BC%E3%83%9E%E3%82%A4%E3%82%B1%E3%83%AB%E6%95%B0
    """
    assert n >= 1  # input integer must be a natural number.
    if n == 1:
        return False
    if n == 2:
        return True

    def n_is_composite(base: int) -> bool:
        nonlocal n
        if math.gcd(n, base) != 1:
            return True
        if pow(base, n - 1, n) != 1:
            return True
        return False

    checked_bases = set()

    for _ in range(check_times):
        base = random.randint(2, n - 1)
        if base in checked_bases:
            continue
        if n_is_composite(base):  # the base is called witness.
            return False
        checked_bases.add(base)

    # might be pseudo prime like Carmichael number.
    # if not prime actually, each checked base is called liar.
    return True
