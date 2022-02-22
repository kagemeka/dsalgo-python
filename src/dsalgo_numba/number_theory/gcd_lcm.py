import numba as nb


@nb.njit
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


@nb.njit
def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b
