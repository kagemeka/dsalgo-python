import typing


class Foo():
    def __init__(self) -> typing.NoReturn:
        self.__bar = 1


def test() -> typing.NoReturn:
    foo = Foo()
    print(foo._Foo__bar)


if __name__ == '__main__':
    test()
