from __future__ import annotations


def argmax(arr: list[int]) -> int | None:
    if len(arr) == 0:
        return None
    idx, max_value = 0, arr[0]
    for i, x in enumerate(arr):
        if x > max_value:
            idx, max_value = i, x
    return idx


def bincount(arr: list[int]) -> list[int]:
    cnt = [0] * (max(arr) + 1)
    for x in arr:
        cnt[x] += 1
    return cnt


def compress(
    arr: list[int],
) -> tuple[list[int], list[int]]:
    """
    Returns:
        tuple[list[int], list[int]]:
            first: compressed array.
            second: array to retrieve original value.
    """
    import bisect

    v = sorted(set(arr))
    return [bisect.bisect_left(v, x) for x in arr], v
