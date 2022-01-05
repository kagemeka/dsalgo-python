import dataclasses
import typing


T = typing.TypeVar('T')


@dataclasses.dataclass
class Monoid(
    typing.Generic[T],
):
    fn: typing.Callable[
        [T, T],
        T,
    ]
    e: T


def add(i: int, j: int) -> int:
    return i + j


def test():
    e = 0
    mon = Monoid[int](
        add,
        e,
    )

    ...


if __name__ == '__main__':
    test()
