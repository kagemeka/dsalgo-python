import typing


def lcp_array_kasai(a: list[int], sa: list[int]) -> list[int]:
    n = len(a)
    assert n > 0
    rank = [0] * n
    for i, j in enumerate(sa):
        rank[j] = i
    lcp, h = [0] * (n - 1), 0
    for i in range(n):
        if h > 0:
            h -= 1
        r = rank[i]
        if r == n - 1:
            continue
        j = sa[r + 1]
        while i + h < n and j + h < n and a[i + h] == a[j + h]:
            h += 1
        lcp[r] = h
    return lcp
