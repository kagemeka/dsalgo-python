import typing

import numpy as np

T = typing.TypeVar("T")


def longest_common_subsequence(
    a: typing.Sequence[T],
    b: typing.Sequence[T],
) -> typing.List[T]:
    n, m = len(a), len(b)
    length = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            length[i + 1][j + 1] = max(
                length[i][j + 1], 
                length[i + 1][j], 
                length[i][j] + (b[j] == a[i]),
            )
    lcs = []
    i, j = n - 1, m - 1
    while i >= 0 and j >= 0:
        x = length[i + 1][j + 1]
        if length[i + 1][j] == x:
            j -= 1
            continue
        if length[i][j + 1] == x:
            i -= 1
            continue
        lcs.append(a[i])
        i -= 1
        j -= 1
    return lcs[::-1]


