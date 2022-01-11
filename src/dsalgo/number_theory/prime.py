import collections
import typing

import numpy as np


def sieve_of_eratosthenes(n: int) -> list[bool]:
    assert n > 1
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    i = 0
    while i * i < n - 1:
        i += 1
        if not is_prime[i]:
            continue
        for j in range(i * i, n, i):
            is_prime[j] = False
    return is_prime


def least_prime_factor(n: int) -> list[int]:
    is_prime = sieve_of_eratosthenes(n)
    lpf = list(range(n))
    lpf[1] = 0
    i = 0
    while i * i < n - 1:
        i += 1
        if not is_prime[i]:
            continue
        for j in range(i * i, n, i):
            if lpf[j] == j:
                lpf[j] = i
    return lpf


def greatest_prime_factor(n: int) -> list[int]:
    lpf = least_prime_factor(n)
    gpf = list(range(n))
    gpf[1] = 0
    for i in range(2, n):
        if lpf[i] == i:
            continue
        gpf[i] = gpf[i // lpf[i]]
    return gpf


def find_prime_numbers(n: int) -> list[int]:
    s = sieve_of_eratosthenes(n)
    return [i for i in range(n) if s[i]]


def find_prime_factors(n: int) -> list[int]:
    factors = []
    i = 1
    while i * i < n:
        i += 1
        if n % i:
            continue
        factors.append(i)
        while n % i == 0:
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def least_prime_factor_np(n: int) -> np.ndarray:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i * i < n - 1:
        i += 1
        if s[i] == i:
            np.minimum(s[i * i :: i], i, out=s[i * i :: i])
    return s


def sieve_of_eratosthenes_np(n: int) -> np.ndarray:
    return least_prime_factor_np(n) == np.arange(n)


def greatest_prime_factor_np(n: int) -> np.ndarray:
    s = np.arange(n)
    s[:2] = -1
    i = 0
    while i < n - 1:
        i += 1
        if s[i] == i:
            s[i::i] = i
    return s


def prime_factorize(n: int) -> typing.DefaultDict[int, int]:
    import collections

    cnt = collections.defaultdict(int)
    i = 1
    while i * i < n:
        i += 1
        while n % i == 0:
            n //= i
            cnt[i] += 1
    if n > 1:
        cnt[n] = 1
    return cnt


class PrimeFactorizeLPF:
    def __call__(self, n: int) -> typing.DefaultDict[int, int]:
        import collections

        cnt = collections.defaultdict(int)
        while n > 1:
            p = self.__lpf[n]
            n //= p
            cnt[p] += 1
        return cnt

    def __init__(self, n: int) -> NoReturn:
        self.__lpf = least_prime_factor(n)


def count_prime_factors(n: int) -> list[int]:
    cnt = [0] * n
    for p in find_prime_numbers(n):
        for i in range(p, n, p):
            cnt[i] += 1
    return cnt


def aks(n: int) -> bool:
    ...


def miller_rabin(n: int) -> bool:
    ...


def linear_sieve(n: int) -> list[bool]:
    ...


def sieve_of_atkin(n: int) -> list[bool]:
    ...
