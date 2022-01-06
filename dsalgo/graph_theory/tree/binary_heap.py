import heapq
import typing


@typing.final
class BinaryHeap:
    def __init__(
        self,
    ) -> NoReturn:
        self.__a = []

    def __swap(
        self,
        i: int,
        j: int,
    ) -> NoReturn:
        a = self.__a
        a[i], a[j] = a[j], a[i]

    def push(
        self,
        x: int,
    ) -> NoReturn:
        a = self.__a
        i = len(a)
        a.append(x)
        while i > 0:
            j = (i - 1) // 2
            if a[i] >= a[j]:
                break
            self.__swap(i, j)
            i = j

    def pop(
        self,
    ) -> int:
        a = self.__a
        self.__swap(0, -1)
        x = a.pop()
        i = 0
        while 1:
            j = i * 2 + 1
            if j >= len(a):
                break
            j += j < len(a) - 1 and a[j + 1] < a[j]
            if a[i] <= a[j]:
                break
            self.__swap(i, j)
            i = j
        return x

    def __repr__(self) -> str:
        return str(self.__a)

    def __bool__(self) -> bool:
        return bool(self.__a)
