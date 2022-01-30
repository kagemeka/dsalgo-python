import typing

from dsalgo.number_theory.equation.extended_euclidean import (
    extended_euclidean_recurse,
)


def invert_extended_euclidean(mod: int, n: int) -> typing.Optional[int]:
    r"""Modular Inverse with extended eucledian GCD algorithm.

    Args:
        mod (int): an modulo.
        n (int): arbitral integer.

    Returns:
        typing.Optional[int]:
            modular inverse of n.
            if the inverse does not exist, return None.

    Algorithm Summary:
        definition of modular inver of n
        x := inverse of n.
        nx \equiv 1 \mod m
        nx - 1 = qm (q is arbitral)
        nx - qm = 1
        y := -q
        nx + my = 1 (Bezout identity)
        this equation can be solved by extendex euclidean algorithm.
    """
    assert mod > 1
    gcd, x, _ = extended_euclidean_recurse(n % mod, mod)
    if gcd != 1:
        return None
    if x < 0:
        x += mod
    assert 0 <= x < mod
    return x


def invert_extended_euclidean_direct(mod: int, n: int) -> typing.Optional[int]:
    """Compute Modular inverse directly with Extended Euclidean Algorithm.

    Args:
        mod (int): an modulo.
        n (int): arbitral integer.

    Returns:
        typing.Optional[int]:
            modular inverse of n.
            if the inverse does not exist, return None.

    Algorithm Summary:
        consider for the equation nx + my = 1.
        (x_i, y_i)^T = [
            [0, 1],
            [1, -q_i],
        ](x_{i-1}, y_{i-1})^T

        (x_0, y_0)^T = (1, 0)^T  # one of the solution.

        finally, y is not needed to be computed.
        it's only enough to store only first row's data.
    """
    assert mod > 1
    a, b = n % mod, mod
    x00, x01 = 1, 0  # first row of matrix identity element.
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        a, b = b, r
    if a != 1:
        return None
    if x00 < 0:
        x00 += mod
    assert 0 <= x00 < mod
    return x00


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
