import typing


def gcd_recurse(a: int, b: int) -> int:
    return gcd_recurse(b, a % b) if b else a


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def array_gcd(arr: typing.List[int]) -> typing.Optional[int]:
    if len(arr) == 0:
        return None
    g = arr[0]
    for x in arr:
        g = gcd(g, x)
    return g
