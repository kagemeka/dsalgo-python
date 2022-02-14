"""
Combinatorics
"""

import typing


def next_permutation(
    arr: typing.List[int],
) -> typing.Optional[typing.List[int]]:
    n, arr = len(arr), arr.copy()
    last_asc_idx = n
    for i in range(n - 2, -1, -1):
        if arr[i] >= arr[i + 1]:
            continue
        last_asc_idx = i
        break
    if last_asc_idx == n:
        return None
    arr[last_asc_idx + 1 :] = arr[-1:last_asc_idx:-1]
    for i in range(last_asc_idx + 1, n):
        if arr[last_asc_idx] >= arr[i]:
            continue
        arr[last_asc_idx], arr[i] = arr[i], arr[last_asc_idx]
        break
    return arr
