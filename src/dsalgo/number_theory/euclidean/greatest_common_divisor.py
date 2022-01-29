import math
import typing


def greatest_common_divisor_recurse(a: int, b: int) -> int:
    return greatest_common_divisor_recurse(b, a % b) if b else a


def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def array_gcd(arr: typing.List[int]) -> typing.Optional[int]:
    if len(arr) == 0:
        return None
    gcd = arr[0]
    for x in arr:
        gcd = math.gcd(gcd, x)
    return gcd
