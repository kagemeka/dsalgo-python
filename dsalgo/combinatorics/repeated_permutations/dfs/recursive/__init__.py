import typing


class RepeatedPermutations:
    def __call__(
        self,
        a: typing.Iterable[typing.Any],
        repeat: int,
    ) -> typing.Iterator[tuple[typing.Any]]:
        self.__a = tuple(a)
        self.__repeat = repeat
        return self.__dfs([-1] * repeat, 0)

    def __dfs(
        self,
        p: list[int],
        i: int,
    ) -> typing.Iterator[tuple[typing.Any]]:
        a = self.__a
        if i == self.__repeat:
            yield tuple(a[j] for j in p)
            return
        n = len(a)
        for j in range(n):
            p[i] = j
            for _p in self.__dfs(p, i + 1):
                yield _p
