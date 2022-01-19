import typing


def flatnonzero(a: typing.List[bool]) -> typing.List[int]:
    return [i for i, x in enumerate(a) if x]
