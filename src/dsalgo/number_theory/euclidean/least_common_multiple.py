from dsalgo.number_theory.euclidean.greatest_common_divisor import (
    gcd,
)


def lcm(a: int, b: int) -> int:
    return 0 if a == b == 0 else a // gcd(a, b) * b
