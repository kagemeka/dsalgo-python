import typing

T = typing.TypeVar("T")


def accumulate(
    e: T,
) -> typing.Callable[
    [typing.Callable[[T, T], T]],
    typing.Callable[[typing.Iterable[T]], T],
]:
    def decorate(
        op: typing.Callable[[T, T], T],
    ) -> typing.Callable[[typing.Iterable[T]], T]:
        import functools

        def wrapped(a: typing.Iterable[T]) -> T:
            return functools.reduce(op, a, e)

        return wrapped

    return decorate


@accumulate(0)
def xor(a: int, b: int) -> int:
    return a ^ b
