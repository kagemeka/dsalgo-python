import typing


class Permutations:
    def __call__(
        self,
        a: typing.Iterable[
            typing.Any,
        ],
        r: typing.Optional[int] = None,
    ) -> typing.AsyncIterator[tuple[typing.Any],]:
        a = tuple(a)
        n = len(a)
        if r is None:
            r = n
        if r < 0 or r > n:
            return
        self.__r = r
        self.__n = n
        self.__a = a
        self.__i = list(range(n))
        self.__l = 0
        return self.__dfs()

    def __dfs(
        self,
    ) -> NoReturn:
        l, r = self.__l, self.__r
        i = self.__i
        if l == r:
            a = self.__a
            yield tuple(a[j] for j in i[:r])
            return
        n = self.__n
        for j in range(l, n):
            i[l], i[j] = i[j], i[l]
            self.__l = l + 1
            for p in self.__dfs():
                yield p
            i[l], i[j] = i[j], i[l]
