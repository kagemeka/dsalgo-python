"""
Discrete
"""

import typing


def bincount(arr: list[int]) -> list[int]:
    cnt = [0] * (max(arr) + 1)
    for x in arr:
        cnt[x] += 1
    return cnt
