# TODO cut below
import typing

from kgmk.dsa.linked_list.singly import SinglyLinkedListNode


class FIFOQueue(typing.Generic[T]):
    def __bool__(self) -> bool:
        return self.__first is not None

    def __init__(self) -> NoReturn:
        self.__first: typing.Optional[SinglyLinkedListNode] = None
        self.__last: typing.Optional[SinglyLinkedListNode] = None

    def append(self, v: typing.Any) -> NoReturn:
        x = SinglyLinkedListNode(value=v)
        if self.__last is None:
            self.__first = x
        else:
            self.__last.next = x
        self.__last = x

    def pop(self) -> typing.Any:
        if self.__first is None:
            raise Exception("cannot pop from empty queue.")
        v = self.__first.value
        self.__first = self.__first.next
        if self.__first is None:
            self.__last = None
        return v
