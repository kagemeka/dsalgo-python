import typing


def flatnonzero(a: list[bool]) -> list[int]:
    return [i for i, x in enumerate(a) if x]
