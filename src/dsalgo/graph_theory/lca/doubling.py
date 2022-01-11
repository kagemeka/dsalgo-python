import numpy as np

from .tree import Tree
from .tree_bfs import TreeBFS

# cut below


class LCA:
    def __init__(
        self,
        tree: Tree,
    ):
        self.g = tree
        self.preprocess()

    def calc_dist(
        self,
        u: int,
        v: int,
    ) -> int:
        lca = self.find_lca(u, v)
        dist = self.dist
        du, dv = dist[u], dist[v]
        d_lca = dist[lca]
        return du + dv - 2 * d_lca

    def preprocess(
        self,
    ):
        bfs = TreeBFS(self.g)
        bfs.search(0)
        self.parent = bfs.parent
        self.depth = bfs.depth
        self.dist = bfs.dist
        self.find_ancestors()

    def find_ancestors(
        self,
    ):
        n = self.g.size
        dep = self.depth
        m = max(dep).bit_length()
        ancestors = [None] * m
        ancestors[0] = np.array(
            self.parent,
        )
        for i in range(m - 1):
            a = ancestors[i]
            ancestors[i + 1] = a[a]
        for i in range(m):
            a = list(ancestors[i])
            ancestors[i] = a
        self.ancestors = ancestors

    def find_lca(
        self,
        u: int,
        v: int,
    ) -> int:
        u, v = self.sort(u, v)
        dep = self.depth
        du, dv = dep[u], dep[v]
        v = self.upstream(
            v,
            dv - du,
        )
        if v == u:
            return u
        return self._find_support(
            du,
            u,
            v,
        )

    def _find_support(
        self,
        dep: int,
        u: int,
        v: int,
    ) -> int:
        n = dep.bit_length()
        ancestors = self.ancestors
        for i in range(
            n - 1,
            -1,
            -1,
        ):
            a = ancestors[i]
            nu, nv = a[u], a[v]
            if nu == nv:
                continue
            u, v = nu, nv
        return self.parent[u]

    def upstream(
        self,
        v: int,
        d: int,
    ):
        n = d.bit_length()
        for i in range(n):
            if ~d >> i & 1:
                continue
            v = self.ancestors[i][v]
        return v

    def sort(
        self,
        u: int,
        v: int,
    ):
        dep = self.depth
        du, dv = dep[u], dep[v]
        if du > dv:
            u, v = v, u
        return u, v
