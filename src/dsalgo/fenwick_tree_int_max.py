import typing


class FenwickTree:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] = max(data[j], data[i])
        self.__data = data

    def __len__(self) -> int:
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self.__data) - 1
        i += 1
        while i < len(self.__data):
            self.__data[i] = max(self.__data[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self.__data)
        v = 0
        while i > 0:
            v = max(v, self.__data[i])
            i -= i & -i
        return v
