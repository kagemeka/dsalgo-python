"""
accumulate
algebra
"""

import typing

from dsalgo.type import T


def accumulate(
    identity_element: T,
) -> typing.Callable[
    [typing.Callable[[T, T], T]],
    typing.Callable[[typing.Iterable[T]], T],
]:
    def decorate(
        op: typing.Callable[[T, T], T],
    ) -> typing.Callable[[typing.Iterable[T]], T]:
        import functools

        def wrapped(arr: typing.Iterable[T]) -> T:
            return functools.reduce(op, arr, identity_element)

        return wrapped

    return decorate


@accumulate(0)
def xor(a: int, b: int) -> int:
    return a ^ b
