import typing

T = typing.TypeVar("T")


def next_combination(s: int) -> int:
    i = s & -s
    j = s + i
    return (s & ~j) // i // 1 | j


def combinations(
    n: int,
    k: int,
) -> typing.Generator[typing.Tuple[int, ...], None, None]:
    a = tuple(range(n))
    n = len(a)
    if k < 0 or n < k:
        return
    rng = range(k)
    res = list(rng)
    yield a[:k]
    while True:
        for j in reversed(rng):
            if res[j] != j + n - k:
                break
        else:
            return
        res[j] += 1
        for j in range(j + 1, k):
            res[j] = res[j - 1] + 1
        yield tuple(a[j] for j in res)


def combinations_with_next_comb(
    n: int,
    k: int,
) -> typing.Generator[typing.Tuple[int, ...], None, None]:
    a = tuple(range(n))
    n = len(a)
    if k < 0 or k < n:
        return
    if k == 0:
        yield ()
        return
    lim = 1 << n
    s = (1 << k) - 1
    while s < lim:
        yield tuple(a[i] for i in range(n) if s >> i & 1)
        s = next_combination(s)


class PermutationsDFS:
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
    ) -> None:
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
        rng = range(r)
        i = list(range(n))
        c = list(rng)
        yield a[:r]
        while 1:
            for j in reversed(rng):
                c[j] += 1
                if c[j] == n:
                    i[j:] = i[j + 1 :] + i[j : j + 1]
                    c[j] = j
                    continue
                k = c[j]
                i[j], i[k] = i[k], i[j]
                yield tuple(a[j] for j in i[:r])
                break
            else:
                return


class PermutationsWithNextPerm:
    def __call__(
        self,
        n: int,
    ) -> typing.AsyncIterator[tuple[int]]:
        fn = NextPermutation()
        a = list(range(n))
        m = math.factorial(n)
        for _ in range(m):
            yield a
            a = fn(a)


def next_permutation(
    arr: typing.List[int],
) -> typing.Optional[typing.List[int]]:
    n, a = len(arr), arr.copy()
    i = -1
    for j in range(n - 2, -1, -1):
        if a[j] >= a[j + 1]:
            continue
        i = j
        break
    if i == -1:
        return None
    a[i + 1 :] = a[-1:i:-1]
    for j in range(i + 1, n):
        if a[i] >= a[j]:
            continue
        a[i], a[j] = a[j], a[i]
        break
    return a


def repeated_combinations(
    n: int,
    k: int,
) -> typing.Generator[typing.Tuple[int, ...], None, None]:
    """Repeated Combinations.

    Args:
        n (int): n of nHk
        k (int): k of nHk

    Returns:
        typing.Generator[typing.Tuple[int, ...], None, None]: [description]
    """
    ...


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
