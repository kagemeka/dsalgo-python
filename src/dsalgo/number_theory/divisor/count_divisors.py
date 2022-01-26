# zeta transform
import typing


def count_divisors(n: int) -> typing.List[int]:
    cnt = [1] * n
    cnt[0] = 0
    for i in range(2, n):
        for j in range(i, n, i):
            cnt[j] += 1
    return cnt
