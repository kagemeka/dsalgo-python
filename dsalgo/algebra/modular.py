import abc
import enum
import typing

import numpy as np


def cumprod(mod: int, a: typing.List[int]) -> typing.List[int]:
    """Compute cummulative product over Modular."""
    a = a.copy()
    for i in range(len(a) - 1):
        a[i + 1] = a[i + 1] * a[i] % mod
    return a


def factorial(mod: int, n: int) -> typing.List[int]:
    fact = list(range(n))
    fact[0] = 1
    return cumprod(mod, fact)


def factorial_inverse(p: int, n: int) -> typing.List[int]:
    ifact = list(range(1, n + 1))
    ifact[-1] = pow(factorial(p, n)[-1], -1, p)
    return cumprod(p, ifact[::-1])[::-1]


def cumprod_np(a: np.ndarray, mod: int) -> np.ndarray:
    """Compute cumprod over modular not in place.

    the parameter a must be one dimentional ndarray.
    """
    n = a.size
    assert a.ndim == 1
    m = int(n ** 0.5) + 1
    a = np.resize(a, (m, m))
    for i in range(m - 1):
        a[:, i + 1] = a[:, i + 1] * a[:, i] % mod
    for i in range(m - 1):
        a[i + 1] = a[i + 1] * a[i, -1] % mod
    return a.ravel()[:n]


def factorial_np(n: int, mod: int) -> np.ndarray:
    a = np.arange(n)
    a[0] = 1
    return cumprod_np(a, mod)


def factorial_inverse_np(n: int, mod: int) -> np.ndarray:
    a = np.arange(1, n + 1)
    a[-1] = inverse(int(factorial_np(n, mod)[-1]), mod)
    return cumprod_np(a[::-1], mod)[::-1]


def inverse(mod: int, n: int) -> int:
    return pow(n, -1, mod)


def inverse_table(n: int, mod: int) -> list[int]:
    b, a = factorial(n, mod), factorial_inverse(n, mod)
    for i in range(n - 1):
        a[i + 1] = a[i + 1] * b[i] % mod
    return a


def inverse_table_np(n: int, mod: int) -> NoReturn:
    a = factorial_inverse_np(n, mod)
    a[1:] *= factorial_np(n - 1, mod)
    return a % mod


class Modulo(enum.IntEnum):
    MOD0 = 10 ** 4 + 7
    MOD1 = 998_244_353
    MOD2 = 10 ** 9 + 7
    MOD3 = 10 ** 9 + 9


class Modular:
    ...


T: typing.Type = typing.Union[int, Modular]


class Modular(abc.ABC):
    mod: int

    def __init__(self, value: int) -> NoReturn:
        value %= self.mod
        self.__value = value

    def __repr__(self) -> str:
        return f"{self.__value}"

    def __clone(self) -> Modular:
        return self.__class__(self.__value)

    @classmethod
    def __to_mod(cls, rhs: T) -> Modular:
        if type(rhs) != int:
            return rhs
        return cls(rhs)

    def __add__(self, rhs: T) -> Modular:
        x = self.__clone()
        x.__value += self.__to_mod(rhs).__value
        x.__value %= self.mod
        return x

    def __iadd__(self, rhs: T) -> Modular:
        return self + rhs

    def __radd__(self, lhs: T) -> Modular:
        return self + lhs

    def __neg__(self) -> Modular:
        return self.__class__(-self.__value)

    def __sub__(self, rhs: T) -> Modular:
        return self + -rhs

    def __isub__(self, rhs: T) -> Modular:
        return self - rhs

    def __rsub__(self, lhs: T) -> Modular:
        return -self + lhs

    def __mul__(self, rhs: T) -> Modular:
        x = self.__clone()
        x.__value *= self.__to_mod(rhs).__value
        x.__value %= self.mod
        return x

    def __imul__(self, rhs: T) -> Modular:
        return self * rhs

    def __rmul__(self, lhs: T) -> Modular:
        return self * lhs

    def __truediv__(self, rhs: T) -> Modular:
        return self * self.__to_mod(rhs).inv()

    def __itruediv__(self, rhs: T) -> Modular:
        return self / rhs

    def __rtruediv__(self, lhs: T) -> Modular:
        return self.inv() * lhs

    def __floordiv__(self, rhs: T) -> Modular:
        return self / rhs

    def __ifloordiv__(self, rhs: T) -> Modular:
        return self // rhs

    def __rfloordiv__(self, lhs: T) -> Modular:
        return lhs / self

    def __pow__(self, n: int) -> Modular:
        return pow(self.__value, n, self.mod)

    def __ipow__(self, n: int) -> Modular:
        return self ** n

    def __rpow__(self, rhs: T) -> Modular:
        return self.__to_mod(rhs) ** self.__value

    def inv(self) -> Modular:
        return self ** (self.mod - 2)

    def __eq__(self, rhs: T) -> bool:
        return self.__value == self.__to_mod(rhs).__value

    def congruent(self, rhs: T) -> bool:
        return self == rhs

    @classmethod
    def mul_identity(cls) -> Modular:
        return cls(1)

    @classmethod
    def add_identity(cls) -> Modular:
        return cls(0)


def define_static_modular(mod: int) -> Modular:
    class Mint(Modular):
        mod: typing.Final[int] = mod

    return Mint
