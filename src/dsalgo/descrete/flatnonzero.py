import typing


def flatnonzero(arr: typing.List[bool]) -> typing.List[int]:
    return [i for i, x in enumerate(arr) if x]
