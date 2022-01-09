import typing

import numpy as np

T = typing.TypeVar("T")


def lcs(
    self,
    a: typing.Sequence[T],
    b: typing.Sequence[T],
) -> typing.List[T]:
    n, m = len(a), len(b)
    l = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        x = a[i]
        for j in range(m):
            l[i + 1][j + 1] = max(
                l[i][j + 1], l[i + 1][j], l[i][j] + (b[j] == x)
            )
    res = []
    i, j = n - 1, m - 1
    while i >= 0 and j >= 0:
        x = l[i + 1][j + 1]
        if l[i + 1][j] == x:
            j -= 1
            continue
        if l[i][j + 1] == x:
            i -= 1
            continue
        res.append(a[i])
        i -= 1
        j -= 1
    return res[::-1]


def lcs_np(
    self,
    a: np.array,
    b: np.array,
) -> np.array:
    n, m = a.size, b.size
    l = np.zeros(
        (n + 1, m + 1),
        dtype=np.int64,
    )
    for i in range(n):
        np.maximum(
            l[i, :-1] + (a[i] == b),
            l[i, 1:],
            out=l[i + 1, 1:],
        )
        np.maximum.accumulate(
            l[i + 1],
            out=l[i + 1],
        )
    res = []
    i, j = n - 1, m - 1
    while i >= 0 and j >= 0:
        x = l[i + 1, j + 1]
        if l[i + 1, j] == x:
            j -= 1
            continue
        if l[i, j + 1] == x:
            i -= 1
            continue
        res.append(a[i])
        i -= 1
        j -= 1
    return np.array(res)[::-1]
