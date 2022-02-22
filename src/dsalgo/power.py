import typing

from dsalgo.algebra.abstract.abstract_structure import Monoid

S = typing.TypeVar("S")


def define_power_func(monoid: Monoid[S]) -> typing.Callable[[S, int], S]:
    def pow(value: S, exponent: int) -> S:
        assert exponent >= 0
        if exponent == 0:
            return monoid.e()
        x = pow(value, exponent >> 1)
        x = monoid.op(x, x)
        if exponent & 1:
            x = monoid.op(x, value)
        return x

    return pow
