def invert_naive(mod: int, n: int) -> int:
    """Modular Inverse naive implementation.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, -1, mod)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
