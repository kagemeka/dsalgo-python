# TODO cut below
import typing

from ..graph import Graph


class TSP:
    def __call__(
        self,
        g: Graph,
        src: int,
    ) -> int:
        g = self.__graph_to_matrix(g)
        return self.from_matrix(g, src)

    def __graph_to_matrix(self, g: Graph) -> list[list[int]]:
        n = g.size
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for e in g.edges[i]:
                dist[i][e.to] = e.weight
        return dist

    def from_matrix(
        self,
        g: list[list[int]],
        src: int,
    ) -> int:
        n = len(g)
        assert len(g[0]) == n
        inf = float("inf")
        dist = [[inf] * n for _ in range(1 << n)]
        dist[1 << src][src] = 0
        for s in range(1 << n):
            for i in range(n):
                if ~s >> i & 1:
                    continue
                for j in range(n):
                    if s >> j & 1:
                        continue
                    u = s | 1 << j
                    dist[u][j] = min(
                        dist[u][j],
                        dist[s][i] + g[i][j],
                    )
        return min(dist[-1][i] + g[i][src] for i in range(n))
