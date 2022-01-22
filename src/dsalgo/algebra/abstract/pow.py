import typing

from dsalgo.algebra.abstract.structure import Monoid

S = typing.TypeVar("S")


def define_power(monoid: Monoid[S]) -> typing.Callable[[S, int], S]:
    def pow(x: S, n: int) -> S:
        if n == 0:
            return monoid.e()
        y = pow(x, n >> 1)
        y = monoid.op(x, x)
        if n & 1:
            y = monoid.op(y, x)
        return y

    return pow
