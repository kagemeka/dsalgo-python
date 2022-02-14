"""
Container
"""

import typing

T = typing.TypeVar("T")


class CircularBufferDeque(typing.Generic[T]):
    """CircularBufferDeque.

    one of the ways to implement Double-Ended-Queue with Dynamic Array.
    """

    __data: typing.List[typing.Optional[T]]
    __left: int
    __right: int
    __size: int

    def __init__(self, buffer_size: int) -> None:
        """Initialize.

        Args:
            buf_size (int): the size of circular buffer.
        """
        assert buffer_size >= 1
        self.__data = [None] * buffer_size
        self.__left = self.__right = 0  # data is stored in [left, right).
        self.__size = 0

    def __len__(self) -> int:
        """Length of deque.

        Returns:
            int: length
        """
        return self.__size

    @property
    def buffer_size(self) -> int:
        """Given buffer size.

        Returns:
            int: buffer size.
        """
        return len(self.__data)

    def __bool__(self) -> bool:
        """bool(dq).

        Returns:
            bool: return True if not empty else False
        """
        return not self.is_empty()

    def is_empty(self) -> bool:
        """Is Empty.

        Returns:
            bool: return True if empty else False.
        """
        return len(self) == 0

    def is_full(self) -> bool:
        """Is Full.

        Returns:
            bool: return True if the buffer is full else False.
        """
        return len(self) == self.buffer_size

    def append_right(self, v: T) -> None:
        """Append to right.

        Raises:
            Exception: raise an exception when the buffer is full.

        Args:
            v (T): value to append.
        """
        if self.is_full():
            raise Exception("buffer is already full")
        assert self.__data[self.__right] is None
        self.__data[self.__right] = v
        self.__size += 1
        self.__right += 1
        if self.__right == self.buffer_size:
            self.__right = 0

    def append_left(self, v: T) -> None:
        """Append to left.

        Raises:
            Exception: raise an exception when the buffer is full.

        Args:
            v (T): value to append.
        """
        if self.is_full():
            raise Exception("buffer is already full")
        if self.__left == 0:
            self.__left = self.buffer_size
        self.__left -= 1
        assert self.__data[self.__left] is None
        self.__data[self.__left] = v
        self.__size += 1

    def pop_right(self) -> T:
        """Pop from right.

        Raises:
            Exception: raise an exception when the deque is empty.

        Returns:
            T: popped value.
        """
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        if self.__right == 0:
            self.__right = self.buffer_size
        self.__right -= 1
        v, self.__data[self.__right] = self.__data[self.__right], None
        self.__size -= 1
        assert v is not None
        return v

    def pop_left(self) -> T:
        """Pop from left.

        Raises:
            Exception: raise an exception when the deque is empty.

        Returns:
            T: popped value.
        """
        if self.is_empty():
            raise Exception("cannot pop from empty deque.")
        v, self.__data[self.__left] = self.__data[self.__left], None
        self.__left += 1
        if self.__left == self.buffer_size:
            self.__left = 0
        self.__size -= 1
        assert v is not None
        return v


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
