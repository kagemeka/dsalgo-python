def invert_fermat(p: int, n: int) -> int:
    """Modular Inverse by Fermat's Little theorem.

    Args:
        p (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, p - 2, p)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
