import typing


class FIFOQueue:
    def __bool__(self) -> bool:
        return self.__i < len(self.__a)

    def __init__(
        self,
    ) -> NoReturn:
        self.__a = []
        self.__i = 0

    def append(
        self,
        v: typing.Any,
    ) -> NoReturn:
        self.__a.append(v)

    def pop(
        self,
    ) -> typing.Any:
        v = self.__a[self.__i]
        self.__i += 1
        return v
