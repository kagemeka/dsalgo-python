import math


def least_common_multiple(a: int, b: int) -> int:
    return 0 if a == b == 0 else a // math.gcd(a, b) * b
