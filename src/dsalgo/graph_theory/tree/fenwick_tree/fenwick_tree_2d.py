import typing

S = typing.TypeVar("S")


class FenwickTree2D(typing.Generic[S]):
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
