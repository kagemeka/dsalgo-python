import abc
import enum
import typing


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


def inverse_naive(mod: int, n: int) -> int:
    """Modular Inverse naive implementation.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, -1, mod)


def inverse_fermat(p: int, n: int) -> int:
    """Modular Inverse by Fermat's Little theorem.

    Args:
        p (int): [description]
        n (int): [description]

    Returns:
        int: [description]
    """
    return pow(n, p - 2, p)


def inverse_extended_gcd(mod: int, n: int) -> int:
    """Modular Inverse with extended eucledian GCD algorithm.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]

    Constraints:

    """
    ...


def inverse_euler(mod: int, n: int) -> int:
    """Modular Inverse by Euler's theorem.

    Args:
        mod (int): [description]
        n (int): [description]

    Returns:
        int: [description]

    Constraints:

    """
    ...


def inverse_table(n: int, mod: int) -> typing.List[int]:
    """Modular Inverse table.

    Args:
        n (int): [description]
        mod (int): [description]

    Returns:
        typing.List[int]: [description]
    """
    b, a = factorial(n, mod), factorial_inverse(n, mod)
    for i in range(n - 1):
        a[i + 1] = a[i + 1] * b[i] % mod
    return a


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

    @property
    def value(self) -> int:
        return self.__value

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
