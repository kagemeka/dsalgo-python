import typing


def longest_increasing_sequence(a: list[int]) -> list[int]:
    import bisect

    inf = 1 << 60
    lis = [inf] * len(a)
    for x in a:
        lis[bisect.bisect_left(lis, x)] = x
    return lis[: bisect.bisect_left(lis, inf)]


def longest_non_decreasing_sequence(
    a: typing.List[int],
) -> typing.List[int]:
    import bisect

    inf = 1 << 60
    lis = [inf] * len(a)
    for x in a:
        lis[bisect.bisect_right(lis, x)] = x
    return lis[: bisect.bisect_left(lis, inf)]
