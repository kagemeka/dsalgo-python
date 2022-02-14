"""
Container
"""

import typing

from dsalgo.container.linked_list.singly_linked_list import (
    Node,
    add_last,
    pop_front,
)

T = typing.TypeVar("T")


class SinglyLinkedListQueue(typing.Generic[T]):
    """SinglyLinkedListQueue."""

    __first: typing.Optional[Node[T]]
    __last: typing.Optional[Node[T]]
    __size: int

    def __init__(self) -> None:
        """Initialize."""
        self.__first = None
        self.__last = None
        self.__size = 0

    def __bool__(self) -> bool:
        """bool(que).

        Returns:
            bool: return True if que is not empty else False.
        """
        return self.__first is not None

    def __len__(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        """IsEmpty.

        Returns:
            bool: return True if que is empty else False.
        """

    def append(self, v: T) -> None:
        """Append to back.

        Args:
            v (T): value to append.
        """
        # x = Node(value=v)
        self.__last = add_last(self.__last, Node(value=v))
        if self.__first is None:
            self.__first = self.__last
        self.__size += 1

    def pop(self) -> T:
        """Pop from front.

        Raises:
            Exception: raise an exception if que is empty.

        Returns:
            T: popped value.
        """
        if self.__first is None:
            raise Exception("cannot pop from empty queue.")
        popped, self.__first = pop_front(self.__first)
        if self.__first is None:
            self.__last = None
        self.__size -= 1
        return popped.value


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
