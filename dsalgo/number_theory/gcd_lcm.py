def gcd(a: int, b: int) -> int:
    return gcd(b, a % b) if b else a


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b
