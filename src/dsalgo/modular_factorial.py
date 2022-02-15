"""
Tag
- numbe theory
"""


import typing


def cumprod(mod: int, a: list[int]) -> list[int]:
    """Compute cummulative product over Modular."""
    a = a.copy()
    for i in range(len(a) - 1):
        a[i + 1] = a[i + 1] * a[i] % mod
    return a


def factorial(mod: int, n: int) -> list[int]:
    fact = list(range(n))
    fact[0] = 1
    return cumprod(mod, fact)


def factorial_inverse(p: int, n: int) -> list[int]:
    ifact = list(range(1, n + 1))
    ifact[-1] = pow(factorial(p, n)[-1], -1, p)
    return cumprod(p, ifact[::-1])[::-1]
