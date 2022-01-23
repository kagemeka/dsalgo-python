import typing

from dsalgo.container.linked_list.doubly_linked_list import (
    Node,
    add_left,
    add_right,
    pop_left,
    pop_right,
)

T = typing.TypeVar("T")


class DoublyLinkedListDeque(typing.Generic[T]):
    """DoublyLinkedListDeque."""

    __first: typing.Optional[Node[T]]
    __last: typing.Optional[Node[T]]
    __size: int

    def __init__(self) -> None:
        """Initialize."""
        self.__first = None
        self.__last = None
        self.__size = 0

    def __len__(self) -> int:
        return self.__size

    def __bool__(self) -> bool:
        """bool(dq).

        Returns:
            bool: return True if deque is not empty else False.
        """
        return self.__first is not None

    def append_right(self, v: T) -> None:
        """Append to right.

        Args:
            v (T): value to append.
        """
        self.__last = add_right(self.__last, Node(value=v))
        if self.__first is None:
            self.__first = self.__last
        self.__size += 1

    def append_left(self, v: T) -> None:
        """Append to left.

        Args:
            v (T): value to append.
        """
        self.__first = add_left(self.__first, Node(value=v))
        if self.__last is None:
            self.__last = self.__first
        self.__size += 1

    def pop_right(self) -> T:
        """Pop from right.

        Raises:
            Exception: raise an exception if the deque is empty.

        Returns:
            T: popped value.
        """
        if self.__last is None:
            raise Exception("cannot pop from empty deque.")
        popped, self.__last = pop_right(self.__last)
        if self.__last is None:
            self.__first = None
        self.__size -= 1
        return popped.value

    def pop_left(self) -> T:
        """Pop from left.

        Raises:
            Exception: raise an exception if the deque is empty.

        Returns:
            T: popped value.
        """
        if self.__first is None:
            raise Exception("cannot pop from empty deque.")
        popped, self.__first = pop_left(self.__first)
        if self.__first is None:
            self.__last = None
        self.__size -= 1
        return popped.value


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
