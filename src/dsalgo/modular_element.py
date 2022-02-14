from __future__ import annotations

import abc
import typing
from socket import if_nameindex

from dsalgo.algebra.modular.multiplicative_inverse.fermat_little_theorem import (
    invert_fermat,
)


# class ModularElement(typing.Protocol):
class ModularElement(abc.ABC):
    _mod: typing.ClassVar[int]
    __value: int

    def __init__(self, value: int) -> None:
        value %= self.mod
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value

    @property
    def mod(self) -> int:
        return self._mod

    def __repr__(self) -> str:
        return f"{self.value}"

    # def __clone(self) -> Modular:
    #     return self.__class__(self._value)

    def __add__(self, rhs: ModularElement) -> ModularElement:
        return self.__class__(self.value + rhs.value)

    def __iadd__(self, rhs: ModularElement) -> ModularElement:
        return self + rhs

    def __radd__(self, lhs: int) -> int:
        return (self.__class__(lhs) + self).value

    def __neg__(self) -> ModularElement:
        return self.__class__(-self.value)

    def __sub__(self, rhs: ModularElement) -> ModularElement:
        return self + -rhs

    def __isub__(self, rhs: ModularElement) -> ModularElement:
        return self - rhs

    def __rsub__(self, lhs: int) -> int:
        return (self.__class__(lhs) - self).value

    def __mul__(self, rhs: ModularElement) -> ModularElement:
        return self.__class__(self.value * rhs.value)

    def __imul__(self, rhs: ModularElement) -> ModularElement:
        return self * rhs

    def __rmul__(self, lhs: int) -> int:
        return (self.__class__(lhs) * self).value

    def invert(self) -> ModularElement:
        return self.__class__(invert_fermat(self.mod, self.value))

    def __truediv__(self, rhs: ModularElement) -> ModularElement:
        assert rhs.value >= 1
        return self * rhs.invert()

    def __itruediv__(self, rhs: ModularElement) -> ModularElement:
        return self / rhs

    def __rtruediv__(self, lhs: int) -> int:
        return (self.__class__(lhs) / self).value

    def __floordiv__(self, rhs: ModularElement) -> ModularElement:
        return self / rhs

    def __ifloordiv__(self, rhs: ModularElement) -> ModularElement:
        return self // rhs

    def __rfloordiv__(self, lhs: int) -> int:
        return lhs / self

    def __pow__(self, n: int) -> ModularElement:
        return self.__class__(pow(self.value, n, self.mod))

    def __ipow__(self, n: int) -> ModularElement:
        return self**n

    def __eq__(self, rhs: object) -> bool:
        if not isinstance(rhs, ModularElement):
            raise NotImplementedError
        return self.value == rhs.value


def define_static_modular_element(
    prime_mod: int,
) -> typing.Type[ModularElement]:
    class Mint(ModularElement):
        _mod: typing.ClassVar[int] = prime_mod

    return Mint


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
