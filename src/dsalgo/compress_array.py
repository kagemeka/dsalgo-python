"""
Discrete
"""
import typing


def compress_array(
    arr: typing.List[int],
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    r"""Compress Array.

    Args:
        arr (typing.List[int]): array to compress.

    Returns:
        typing.Tuple[typing.List[int], typing.List[int]]:
            first: compressed array.
            second: array to retrieve original value.

    Complexity:
        time: O(N\log{N})
        space: O(N)
        where:
            N: size of arr.
    """
    import bisect

    v = sorted(set(arr))
    return [bisect.bisect_left(v, x) for x in arr], v
