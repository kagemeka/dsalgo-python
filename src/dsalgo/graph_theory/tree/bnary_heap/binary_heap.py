import typing
from dsalgo.algebra.abstract.order import Order

T = typing.TypeVar("T", bound=Order)


class BinaryMinHeap(typing.Generic[T]):
    __data: typing.List[T]

    def __init__(self) -> None:
        self.__data = []

    def __len__(self) -> int:
        return len(self.__data)

    def __repr__(self) -> str:
        return str(self.__data)

    def __bool__(self) -> bool:
        return bool(self.__data)

    def __swap(self, i: int, j: int) -> None:
        d = self.__data
        d[i], d[j] = d[j], d[i]

    def push(self, x: T) -> None:
        d = self.__data
        i = len(d)
        d.append(x)
        while i > 0:
            j = (i - 1) >> 1
            if d[i] >= d[j]:
                break
            self.__swap(i, j)
            i = j

    def pop(self) -> T:
        d = self.__data
        self.__swap(0, -1)
        x = d.pop()
        i = 0
        while True:
            j = (i << 1) + 1
            if j >= len(d):
                break
            j += j < len(d) - 1 and d[j + 1] < d[j]
            if d[i] <= d[j]:
                break
            self.__swap(i, j)
            i = j
        return x
