import dataclasses
import typing

S = typing.TypeVar("S")


@dataclasses.dataclass
class Semigroup(typing.Generic[S]):
    op: typing.Callable[[S, S], S]
