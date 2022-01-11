import typing

from dsalgo.container.linked_list import DoublyLinkedListNode

T = typing.TypeVar("T")


class CircularBufferDeque(typing.Generic[T]):
    """CircularBufferDeque.

    one of the ways to implement Double-Ended-Queue with Dynamic Array.

    """

    def __bool__(self) -> bool:
        """bool(dq).

        Returns:
            bool: return True if not empty else False
        """
        return self.__l <= self.__r

    def __init__(self, buf_size: int) -> None:
        """Initialize.

        Args:
            buf_size (int): the size of circular buffer.
        """
        self.__data: typing.List[typing.Optional[T]] = [None] * buf_size
        self.__l = 0
        self.__r = -1

    def append(self, v: T) -> None:
        """Append to right.

        Args:
            v (T): value to append.
        """
        self.__r += 1
        self.__data[self.__r] = v

    def appendleft(self, v: T) -> None:
        """Append to left.

        Args:
            v (T): value to append.
        """
        self.__l -= 1
        self.__data[self.__l] = v

    def is_empty(self) -> bool:
        """IsEmpty.

        Returns:
            bool: return True if empty else False.
        """
        return not bool(self)

    def pop(self) -> T:
        """Pop from right.

        Raises:
            Exception: raise an exception when the deque is empty.

        Returns:
            T: popped value.
        """
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        v = self.__data[self.__r]
        self.__r -= 1
        assert v is not None
        return v

    def popleft(self) -> T:
        """Pop from left.

        Raises:
            Exception: raise an exception when the deque is empty.

        Returns:
            T: popped value.
        """
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        v = self.__data[self.__l]
        self.__l += 1
        assert v is not None
        return v


class MiddleIndexDeque:
    """CircularBufferDeque.

    one of the ways to implement Double-Ended-Queue with Dynamic Array.

    """

    ...


class DoublyLinkedListDeque(typing.Generic[T]):
    """CircularBufferDeque."""

    def __bool__(self) -> bool:
        """bool(dq).

        Returns:
            bool: return True if deque is not empty else False.
        """
        return self.__first is not None

    def __init__(self) -> None:
        """Initialize."""
        self.__first: typing.Optional[DoublyLinkedListNode] = None
        self.__last: typing.Optional[DoublyLinkedListNode] = None

    def append(self, v: T) -> None:
        """Append to right.

        Args:
            v (T): value to append.
        """
        x = DoublyLinkedListNode(value=v, left=self.__last)
        if x.left is None:
            self.__first = x
        else:
            assert self.__last is not None
            self.__last.right = x
        self.__last = x

    def appendleft(self, v: T) -> None:
        """Append to left.

        Args:
            v (T): value to append.
        """
        x = DoublyLinkedListNode(value=v, right=self.__first)
        if x.right is None:
            self.__last = x
        else:
            assert self.__first is not None
            self.__first.left = x
        self.__first = x

    def pop(self) -> T:
        """Pop from right.

        Raises:
            Exception: raise an exception if the deque is empty.

        Returns:
            T: popped value.
        """
        if self.__last is None:
            raise Exception("cannot pop from empty deque.")
        v = self.__last.value
        self.__last = self.__last.left
        if self.__last is None:
            self.__first = None
        else:
            self.__last.right = None
        return v

    def popleft(self) -> T:
        """Pop from left.

        Raises:
            Exception: raise an exception if the deque is empty.

        Returns:
            T: popped value.
        """
        if self.__first is None:
            raise Exception("cannot pop from empty deque.")
        v = self.__first.value
        self.__first = self.__first.right
        if self.__first is None:
            self.__last = None
        else:
            self.__first.left = None
        return v


if __name__ == "__main__":
    import doctest

    doctest.testmod()
