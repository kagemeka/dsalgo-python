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


import typing

from kgmk.dsa.linked_list.doubly import DoublyLinkedListNode

# TODO cut below


class DoublyLinkedListDeque:
    def __bool__(self) -> bool:
        return self.__first is not None

    def __init__(
        self,
    ) -> NoReturn:
        self.__first: typing.Optional[DoublyLinkedListNode] = None
        self.__last: typing.Optional[DoublyLinkedListNode] = None

    def append(
        self,
        v: typing.Any,
    ) -> NoReturn:
        x = DoublyLinkedListNode(value=v, left=self.__last)
        if x.left is None:
            self.__first = x
        else:
            self.__last.right = x
        self.__last = x

    def appendleft(
        self,
        v: typing.Any,
    ) -> NoReturn:
        x = DoublyLinkedListNode(value=v, right=self.__first)
        if self.__right is None:
            self.__last = x
        else:
            self.__first.left = x
        self.__first = x

    def pop(
        self,
    ) -> typing.Any:
        if self.__last is None:
            raise Exception("cannot pop from empty deque.")
        v = self.__last.value
        self.__last = self.__last.left
        if self.__last is None:
            self.__first = None
        else:
            self.__last.right = None
        self.__last.right = None
        return v

    def popleft(
        self,
    ) -> typing.Any:
        if self.__first is None:
            raise Exception("cannot pop from empty deque.")
        v = self.__first.value
        self.__first = self.__first.right
        if self.__first is None:
            self.__last = None
        else:
            self.__first.left = None
        return v
