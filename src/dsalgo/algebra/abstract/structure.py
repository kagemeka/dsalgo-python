import dataclasses
import typing

S = typing.TypeVar("S")


@dataclasses.dataclass
class Semigroup(typing.Generic[S]):
    op: typing.Callable[[S, S], S]


@dataclasses.dataclass
class Monoid(typing.Generic[S]):
    op: typing.Callable[[S, S], S]
    e: typing.Callable[[], S]



@dataclasses.dataclass
class Group(typing.Generic[S]):
    op: typing.Callable[[S, S], S]
    e: typing.Callable[[], S]
    inverse: typing.Callable[[S], S]

