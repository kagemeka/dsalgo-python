import typing


def base_convert_to_ten(
    base: int,
    digits: typing.Iterable[int],
) -> int:
    assert abs(base) >= 2
    p = 1
    n = 0
    for d in digits:
        n += d * p
        p *= base
    return n


def base_convert_from_ten(
    base: int,
    n: int,
) -> typing.List[int]:
    assert abs(base) >= 2
    if n == 0:
        return [0]
    digits = []
    while n:
        n, r = divmod(n, base)
        if r < 0:
            r -= base
            n += 1
        digits.append(r)
    return digits


def base_convert(
    b0: int,
    b1: int,
    digits: typing.List[int],
) -> typing.List[int]:
    return base_convert_from_ten(
        b1,
        base_convert_to_ten(b0, digits),
    )
