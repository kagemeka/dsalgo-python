import typing

from ....graph import Edge, Graph
from ....union_find.parent_size_at_same import UnionFind

# TODO cut below


class MSTBoruvkaUF:
    def __call__(self, g: Graph) -> Graph:
        n = g.size
        self.__new_g = Graph.from_size(n)
        self.__uf = UnionFind(n)
        self.__root = list(range(n))
        self.__n = n
        edges = [(u, e.to, e.weight) for u in range(n) for e in g.edges[u]]
        self.__edge_is_added = [False] * len(edges)
        self.__edges = edges
        while not self.__all_same():
            self.__update_min_edge_indices()
            self.__add_min_edges()
            self.__update_all_roots()
        return self.__new_g

    def __add_min_edges(
        self,
    ) -> NoReturn:
        edge_is_added = self.__edge_is_added
        for i in range(self.__n):
            if i != self.__root[i]:
                continue
            i = self.__min_edge_idx[i]
            if edge_is_added[i]:
                continue
            u, v, w = self.__edges[i]
            self.__uf.unite(u, v)
            self.__new_g.add_edge(Edge(u, v, w))
            edge_is_added[i] = True

    def __all_same(self) -> bool:
        n, root = self.__n, self.__root
        return all(root[i] == root[i + 1] for i in range(n - 1))

    def __update_all_roots(
        self,
    ) -> NoReturn:
        for i in range(self.__n):
            self.__root[i] = self.__uf.find(i)

    def __update_min_edge_indices(
        self,
    ) -> NoReturn:
        root, edges = self.__root, self.__edges
        min_edge_idx = [-1] * self.__n
        for i, (u, v, w) in enumerate(edges):
            u, v = root[u], root[v]
            if u == v:
                continue
            j = min_edge_idx[u]
            if j == -1 or w < edges[j][2]:
                min_edge_idx[u] = i
            j = min_edge_idx[v]
            if j == -1 or w < edges[j][2]:
                min_edge_idx[v] = i
        self.__min_edge_idx = min_edge_idx
