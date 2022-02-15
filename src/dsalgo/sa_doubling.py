import typing

# from dsalgo.descrete.compress_array import compress_array
from dsalgo.compress_array import compress_array


def suffix_array_doubling(arr: list[int]) -> list[int]:
    n = len(arr)
    (rank, _), k = compress_array(arr), 1
    while True:
        key = [r << 30 for r in rank]
        for i in range(n - k):
            key[i] |= 1 + rank[i + k]
        sa = sorted(range(n), key=lambda x: key[x])
        rank[sa[0]] = 0
        for i in range(n - 1):
            rank[sa[i + 1]] = rank[sa[i]] + (key[sa[i + 1]] > key[sa[i]])
        k <<= 1
        if k >= n:
            break
    return sa
