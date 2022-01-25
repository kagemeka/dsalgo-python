import typing


def euler_totient(n: int) -> int:
    count, p = n, 1
    while p * p < n:
        p += 1
        if n % p:
            continue
        count = count // p * (p - 1)
        while n % p == 0:
            n //= p
    if n > 1:
        count = count // n * (n - 1)
    return count
