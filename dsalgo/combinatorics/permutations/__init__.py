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
