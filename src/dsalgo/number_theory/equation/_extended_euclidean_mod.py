import typing


def extended_euclidean_mod(mod: int, n: int) -> typing.Tuple[int, int]:
    r"""Compute gcd(mod, n) and Modular Inverse of n / gcd(mod, n).

    Args:
        mod (int): an modulo.
        n (int): arbitral integer.

    Returns:
        typing.Tuple[int, int]:
            return (gcd(mod, n), x).
            such that xn \equiv gcd(mod, n) \mod mod.

    Algorithm Summary:
        let g := gcd(mod, n).
        consider xn \equiv g \mod mod.
        (1 <= n, x < mod)

        n := g * u
        mod := g * m
        xgu \equiv g \mod (gm)
        <-> xu \equiv 1 \mod m
        that is, x is a modular inverse of u = n / g on \mod m.
        it's gonna be satisfied that 0 <= x < m = mod / g.
    """
    assert mod > 1
    a, b = n % mod, mod
    x00, x01 = 1, 0  # first row of matrix identity element.
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        a, b = b, r
    gcd = a
    if x00 < 0:
        x00 += mod // gcd
    assert 0 <= x00 < mod // gcd
    return gcd, x00
