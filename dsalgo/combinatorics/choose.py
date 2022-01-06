import typing

import numpy as np
from kagemeka.dsa.algebra.modular import (factorial, factorial_inverse,
                                          factorial_inverse_np, factorial_np)


def make_choose(
    mod: int,
    n: int,
) -> typing.Callable[[int, int], int]:
    fact = factorial(mod, n)
    ifact = factorial_inverse(mod, n)

    def choose(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k:
            return 0
        return fact[n] * ifact[n - k] % mod * ifact[k] % mod

    return choose


class Choose:
    def __call__(self, n: int, k: int) -> int:
        p, fact, ifact = self.__p, self.__fact, self.__ifact
        ok = 0 <= k <= n
        return fact[n] * ifact[n - k] % p * ifact[k] % p * ok

    def __init__(self, p: int, n: int) -> NoReturn:
        self.__p = p
        self.__fact = factorial(p, n)
        self.__ifact = factorial_inverse(p, n)


class CountPermutation:
    def __call__(self, n: int, k: int) -> int:
        p, fact, ifact = self.__p, self.__fact, self.__ifact
        ok = 0 <= k <= n
        return fact[n] * ifact[n - k] % p * ok

    def __init__(self, p: int, n: int) -> typing.NoReturn:
        self.__p = p
        self.__fact = factorial(p, n)
        self.__ifact = factorial_inverse(p, n)


class ModChooseNP:
    def __init__(self, mod: int, n: int) -> NoReturn:
        self.__mod = mod
        self.__fact = factorial_np(mod, n)
        self.__ifact = factorial_inverse_np(mod, n)

    def __call__(self, n: int, k: int) -> int:
        mod, fact, ifact = self.__mod, self.__fact, self.__ifact
        ok = (0 <= k) & (k <= n)
        return fact[n] * ifact[n - k] % mod * ifact[k] % mod * ok

    def inv(self, n: int, k: int) -> int:
        mod, fact, ifact = self.__mod, self.__fact, self.__ifact
        ok = (0 <= k) & (k <= n)
        return ifact[n] * fact[n - k] % mod * fact[k] % mod * ok


class NChoose:
    def __call__(
        self,
        r: int,
    ) -> int:
        return self[r]

    def __getitem__(
        self,
        r: int,
    ) -> int:
        return self.__a[r]

    def __init__(
        self,
        n: int,
        rmax: int,
        modulo: int,
    ) -> NoReturn:
        r, m = rmax, modulo
        fn = ModFactorial(m)
        a = list(
            range(
                n + 1,
                n - r,
                -1,
            )
        )
        a[0] = 1
        fn.cumprod(a)
        b = fn.inv(r + 1)
        for i in range(rmax + 1):
            a[i] *= b[i]
            a[i] %= m
        self.__a = a

    def __len__(self) -> int:
        return len(self.__a)


class NChoose:
    def __call__(
        self,
        r: int,
    ) -> int:
        return self[r]

    def __getitem__(
        self,
        r: int,
    ) -> int:
        return self.__a[r]

    def __init__(
        self,
        n: int,
        rmax: int,
        modulo: int,
    ) -> NoReturn:
        r, m = rmax, modulo
        fn = ModFactorial(m)
        a = np.arange(
            n + 1,
            n - r,
            -1,
        )
        a[0] = 1
        a = fn.cumprod(a)
        a *= fn.inv(r + 1)
        self.__a = a % m

    def __len__(self) -> int:
        return self.__a.size
