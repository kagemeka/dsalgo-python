import typing


def bincount(a: list[int]) -> list[int]:
    c = [0] * (max(a) + 1)
    for x in a:
        c[x] += 1
    return c
