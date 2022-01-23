import typing


def compress_array(
    arr: typing.List[int],
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    """Compress array.

    return
        compressed_array
        retrieve_array
    """
    import bisect

    v = sorted(set(arr))
    return [bisect.bisect_left(v, x) for x in arr], v
