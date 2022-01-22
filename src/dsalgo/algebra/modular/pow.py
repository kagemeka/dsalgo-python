def pow_recurse(mod: int, x: int, n: int) -> int:
    if n == 0:
        return 1
    y = pow_recurse(mod, x, n >> 1)
    y = y * y % mod
    if n & 1:
        y = y * x % mod
    return y


def pow(mod: int, x: int, n: int) -> int:
    y = 1
    while n:
        if n & 1:
            y = y * x % mod
        x = x * x % mod
        n >>= 1
    return y


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
