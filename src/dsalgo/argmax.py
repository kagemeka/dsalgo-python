"""
Discrete
"""


import typing


def argmax(arr: typing.List[int]) -> typing.Optional[int]:
    if len(arr) == 0:
        return None
    idx, max_value = 0, arr[0]
    for i, x in enumerate(arr):
        if x > max_value:
            idx, max_value = i, x
    return idx
