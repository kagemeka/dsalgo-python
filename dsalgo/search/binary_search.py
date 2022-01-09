import typing

T = typing.TypeVar("T")


def binary_search(
    is_ok: typing.Callable[[T], bool],
    arr: typing.List[T],
    lo: typing.Optional[int] = None,
    hi: typing.Optional[int] = None,
) -> int:
    """Descrete Binary Search.

    Args:
        is_ok (typing.Callable[[T], bool]):
            conditional function to search index of arr.
        arr (typing.List[T]):
            array for search.
            it must be monotonous between [lo, hi) over is_ok.
            that means following conditions should be satisfied.
                is_ok(arr[lo]) = ... = is_ok(arr[i - 1]) = False
                is_ok(arr[i], ... = is_ok(arr[hi - 1]) = True
            where
                lo <= i < hi
        lo (typing.Optional[int], optional):
            low index. Defaults to None.
            0 <= lo <= len(arr)
        hi (typing.Optional[int], optional):
            high index. Defaults to None.
            0 <= hi <= len(arr)

    Constraits:
        - lo <= hi

    Returns:
        int:
            return minimum i (lo <= i < hi) such that is_ok(arr[i]) = True.
            or return hi if such a i does not exist.
    """
    if lo is None:
        lo = -1
    if hi is None:
        hi = len(arr)
    assert -1 <= lo < hi <= len(arr)
    lo -= 1
    while hi - lo > 1:
        i = (lo + hi) >> 1
        if is_ok(arr[i]):
            hi = i
        else:
            lo = i
    return hi


def bisect_left(arr: typing.List[int], x: int) -> int:
    """Bisect Left.

    Args:
        arr (typing.List[int]): monotonous increasing sequence.
        x (int): target value.

    Returns:
        int:
            first index i such that arr[i] >= x.
            if i does not exist, return the size of arr.
    """
    is_ok: typing.Callable[[int], bool] = lambda y: y >= x
    return binary_search(is_ok, arr)


def bisect_right(arr: typing.List[int], x: int) -> int:
    """Bisect Right.

    Args:
        arr (typing.List[int]): monotonous increasing sequence.
        x (int): target value.

    Returns:
        int:
            first index i such that arr[i] > x.
            if i does not exist, return the size of arr.
    """
    is_ok: typing.Callable[[int], bool] = lambda y: y > x
    return binary_search(is_ok, arr)
