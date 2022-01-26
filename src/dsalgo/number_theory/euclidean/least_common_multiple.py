from dsalgo.number_theory.euclidean.greatest_common_divisor import (
    greatest_common_divisor,
)


def least_common_multiple(a: int, b: int) -> int:
    return 0 if a == b == 0 else a // greatest_common_divisor(a, b) * b
