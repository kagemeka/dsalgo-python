import typing


def argmax(a: typing.List[int]) -> int:
    n = len(a)
    assert n > 0
    i, x = 0, a[0]
    for j in range(n):
        if a[j] <= x:
            continue
        i, x = j, a[j]
    return i
