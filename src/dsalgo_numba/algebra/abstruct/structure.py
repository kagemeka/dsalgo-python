import typing

# Monoid
S = typing.TypeVar("S")


@nb.njit
def op(a: S, b: S) -> S:
    ...


@nb.njit
def op() -> S:
    ...
