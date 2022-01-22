def invert_naive(mod: int, n: int) -> int:
    """Modular Inverse naive implementation.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, -1, mod)


def invert_fermat(p: int, n: int) -> int:
    """Modular Inverse by Fermat's Little theorem.

    Args:
        p (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, p - 2, p)


def invert_extended_gcd(mod: int, n: int) -> int:
    """Modular Inverse with extended eucledian GCD algorithm.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]

    Constraints:

    """
    ...


def invert_euler(mod: int, n: int) -> int:
    """Modular Inverse by Euler's theorem.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]

    Constraints:

    """
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
