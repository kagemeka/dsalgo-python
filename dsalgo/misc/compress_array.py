def compress_array(a: list[int]) -> tuple[(list[int],) * 2]:
    r"""Compress array.

    return
        compressed_array
        retrieve_array
    """
    import bisect

    v = sorted(set(a))
    return [bisect.bisect_left(v, x) for x in a], v
