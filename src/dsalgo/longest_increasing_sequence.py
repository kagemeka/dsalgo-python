"""
DP
"""

import bisect
import typing

from dsalgo.constant import INT_INF


def longest_increasing_sequence(arr: typing.List[int]) -> typing.List[int]:
    """Longest Increasing Sequence.

    Args:
        arr (typing.List[int]): integer array.

    Returns:
        typing.List[int]: result.
    """
    lis = [INT_INF] * len(arr)
    for x in arr:
        lis[bisect.bisect_left(lis, x)] = x
    return lis[: bisect.bisect_left(lis, INT_INF)]


def longest_non_decreasing_sequence(arr: typing.List[int]) -> typing.List[int]:
    """Longest Non Decreasing Sequence.

    Args:
        arr (typing.List[int]): integer array.

    Returns:
        typing.List[int]: result.
    """
    lis = [INT_INF] * len(arr)
    for x in arr:
        lis[bisect.bisect_right(lis, x)] = x
    return lis[: bisect.bisect_left(lis, INT_INF)]
