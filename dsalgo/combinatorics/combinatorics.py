import itertools
from functools import lru_cache
from typing import Iterable, List, Tuple, Union, final, overload

import numpy as np
from numba import njit

from ..algebra.modular import ModularInt as Mint
from ..algebra.modular import Modulus


class Combinatorics:
    ...


@lru_cache(maxsize=None)
def choose(
    cls,
    n,
    r,
    mod=None,
):
    if r > n or r < 0:
        return 0
    if r == 0:
        return 1
    res = cls.choose(n - 1, r, mod,) + cls.choose(
        n - 1,
        r - 1,
        mod,
    )
    if mod:
        res %= mod
    return res


class ChooseMod(
    Mint,
):
    def __init__(
        self,
        n: int = 1 << 20,
        *args,
        **kwargs,
    ):
        super().__init__(
            value=n,
            *args,
            **kwargs,
        )
        (self.fact, self.inv_fact,) = (
            self.factorial(),
            self.inverse_factorial(),
        )

    def __call__(self, n, r):
        return self.choose(n, r)

    @overload
    def choose(
        self,
        n: np.ndarray,
        r: np.ndarray,
    ) -> np.ndarray:
        ...

    @final
    def choose(
        self,
        n: int,
        r: int,
    ):
        bl = (0 <= r) & (r <= n)
        p = self.mod
        return bl * self.fact[n] * self.inv_fact[r] * self.inv_fact[n - r]


class NChooseMod(ChooseMod):
    def __init__(
        self,
        n=10 ** 9,
        r=1 << 20,
        *args,
        **kwargs,
    ):
        super().__init__(
            n=r,
            *args,
            **kwargs,
        )

        self.make(n)

    def __call__(
        self,
        r: int,
    ):
        return self.nchoose[r]

    def __iter__(self):
        return iter(self.nchoose)

    def __getitem__(
        self,
        key: int,
    ):
        return self.nchoose[key]

    def make(self, n: int):
        import numpy as np

        p = self.mod
        r = self.fact.size - 1

        self.nchoose = np.arange(
            n + 1,
            n - r,
            -1,
        )
        self.nchoose[0] = 1

        self.nchoose = (
            self.cumprod(
                self.nchoose,
            )
            * self.inv_fact
            % p
        )
