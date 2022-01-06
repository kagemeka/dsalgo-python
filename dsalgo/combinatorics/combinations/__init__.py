import typing


class Combinations:
    def __call__(
        self,
        a: typing.Iterable[
            typing.Any,
        ],
        r: int,
    ) -> typing.AsyncIterator[tuple[typing.Any],]:
        a = tuple(a)
        n = len(a)
        if r < 0 or r > n:
            return
        rng = range(r)
        i = list(rng)
        yield a[:r]
        while 1:
            for j in reversed(rng):
                if i[j] != j + n - r:
                    break
            else:
                return
            i[j] += 1
            for j in range(j + 1, r):
                i[j] = i[j - 1] + 1
            yield tuple(a[j] for j in i)
