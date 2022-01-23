import typing

T = typing.TypeVar("T")


class DinamicArrayQueue(typing.Generic[T]):
    def __bool__(self) -> bool:
        """bool(que).

        Returns:
            bool: return True if que is not empty else False.
        """
        return self.__i < len(self.__arr)

    def is_empty(self) -> bool:
        """IsEmpty.

        Returns:
            bool: return True if que is empty else False.
        """
        return not self

    def __init__(self) -> None:
        """Initialize."""
        self.__arr: typing.List[T] = []
        self.__i = 0

    def append(self, v: T) -> None:
        """Append to back.

        Args:
            v (T): value to append.
        """
        self.__arr.append(v)

    def pop(self) -> T:
        """Pop from front.

        Raises:
            Exception: raise an exception if que is empty.

        Returns:
            T: popped value.
        """
        if self.is_empty():
            raise Exception("queue is empty.")
        v = self.__arr[self.__i]
        self.__i += 1
        return v


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
