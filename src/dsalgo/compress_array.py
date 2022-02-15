"""
Discrete
"""
import typing


def compress_array(
    arr: list[int],
) -> typing.Tuple[list[int], list[int]]:
    r"""Compress Array.

    Args:
        arr (list[int]): array to compress.

    Returns:
        typing.Tuple[list[int], list[int]]:
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
