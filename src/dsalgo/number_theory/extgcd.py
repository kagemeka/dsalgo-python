import typing


def extgcd(a: int, b: int) -> tuple[int, int, int]:
    if not b:
        return a, 1, 0
    g, s, t = extgcd(b, a % b)
    return g, t, s - a // b * t
