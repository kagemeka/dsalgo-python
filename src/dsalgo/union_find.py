from __future__ import annotations


class UnionFind:
    __data: list[int]

    def __init__(self, size: int) -> None:
        self.__data = [-1] * size

    def __len__(self) -> int:
        return len(self.__data)

    def find_root(self, node: int) -> int:
        assert 0 <= node < len(self)
        if self.__data[node] < 0:
            return node
        self.__data[node] = self.find_root(self.__data[node])
        return self.__data[node]

    def unite(self, node_u: int, node_v: int) -> None:
        assert 0 <= node_u < len(self) and 0 <= node_v < len(self)
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u

    def size(self, node: int) -> int:
        assert 0 <= node < len(self)
        return -self.__data[self.find_root(node)]


def get_labels(uf: UnionFind) -> list[int]:
    n = len(uf)
    labels = [-1] * n
    label = 0
    for i in range(n):
        root = uf.find_root(i)
        if labels[root] == -1:
            labels[root] = label
            label += 1
        labels[i] = labels[root]
    return labels


class UnionFindByRank:
    ...


class UnionFindBySize:
    ...


class PotentialUnionFind:
    ...


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
