import typing


def euler_totient(n: int) -> int:
    c, p = n, 1
    while p * p < n:
        p += 1
        if n % p:
            continue
        c = c // p * (p - 1)
        while n % p == 0:
            n //= p
    if n > 1:
        c = c // n * (n - 1)
    return c


def euler_totient_lpf(n: int, lpf: list[int]) -> int:
    ...
