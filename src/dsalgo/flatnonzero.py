"""
Discrete
"""

import typing


def flatnonzero(arr: list[bool]) -> list[int]:
    return [i for i, x in enumerate(arr) if x]
