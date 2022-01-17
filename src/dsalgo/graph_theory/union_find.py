import typing


class UnionFind():
    def __init__(self, n: int) -> None:
        self.__data = [-1] * n

    def __len__(self) -> int:
        return len(self.__data)

    def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0:
            return u
        d[u] = self.find(d[u])
        return d[u]

    def unite(self, u: int, v: int) -> None:
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        d = self.__data
        if d[u] > d[v]:
            u, v = v, u
        d[u] += d[v]
        d[v] = u

    def size(self, u: int) -> int:
        return -self.__data[self.find(u)]


def get_labels(uf: UnionFind) -> typing.List[int]:
    n = len(uf)
    labels = [-1] * n
    label = 0
    for i in range(n):
        root = uf.find(i)
        if labels[root] == -1:
            labels[root] = label
            label += 1
        labels[i] = labels[root]
    return labels
