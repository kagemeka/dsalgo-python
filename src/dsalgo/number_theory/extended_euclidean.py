import typing


def extended_gcd_recurse(a: int, b: int) -> tuple[int, int, int]:
    if not b:
        return a, 1, 0
    g, s, t = extended_gcd_recurse(b, a % b)
    return g, t, s - a // b * t
