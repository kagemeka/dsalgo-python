import typing

T = typing.TypeVar("T")


class CircularBufferDeque(typing.Generics[T]):
    def __bool__(self) -> bool:
        return self.__l <= self.__r

    def __init__(self, buf_size: int) -> typing.NoReturn:
        self.__data = [None] * max_size
        self.__l = 0
        self.__r = -1

    def append(self, v: T) -> typing.NoReturn:
        self.__r += 1
        self.__data[self.__r] = v

    def appendleft(self, v: T) -> typing.NoReturn:
        self.__l -= 1
        self.__data[self.__l] = v

    def is_empty(self) -> bool:
        return not bool(self)

    def pop(self) -> T:
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        v = self.__data[self.__r]
        self.__r -= 1
        return v

    def popleft(self) -> T:
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        v = self.__data[self.__l]
        self.__l += 1
        return v
