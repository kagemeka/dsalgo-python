def gcd_recurse(a: int, b: int) -> int:
    return gcd_recurse(b, a % b) if b else a


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
