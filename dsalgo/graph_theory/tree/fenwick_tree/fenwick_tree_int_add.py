import typing


S = typing.TypeVar("S")


class Monoid(typing.Protocol[S]):
    @classmethod
    def e(cls: S) -> S:
        ...

    def op(self: S, rhs: S) -> S:
        ...


class FenwickTree(typing.Generic[S]):
    def __init__(self, arr: typing.List[Monoid[S]]) -> None:
        arr[0].e()
