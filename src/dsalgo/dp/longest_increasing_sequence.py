import bisect
import typing


def longest_increasing_sequence(arr: typing.List[int]) -> typing.List[int]:
    """Longest Increasing Sequence.

    Args:
        arr (typing.List[int]): integer array.

    Returns:
        typing.List[int]: result.
    """
    inf = 1 << 60
    lis = [inf] * len(arr)
    for x in arr:
        lis[bisect.bisect_left(lis, x)] = x
    return lis[: bisect.bisect_left(lis, inf)]


def longest_non_decreasing_sequence(arr: typing.List[int]) -> typing.List[int]:
    """Longest Non Decreasing Sequence.

    Args:
        arr (typing.List[int]): integer array.

    Returns:
        typing.List[int]: result.
    """
    inf = 1 << 60
    lis = [inf] * len(arr)
    for x in arr:
        lis[bisect.bisect_right(lis, x)] = x
    return lis[: bisect.bisect_left(lis, inf)]
