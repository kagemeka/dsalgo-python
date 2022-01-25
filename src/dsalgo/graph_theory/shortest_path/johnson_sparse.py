import typing

from dsalgo.graph_theory.shortest_path.bellman_ford_sparse import (
    bellman_ford_sparse,
)
from dsalgo.graph_theory.shortest_path.dijkstra_sparse import dijkstra_sparse


def johnson_sparse(
    graph: typing.List[typing.List[typing.Tuple[int, int]]]
) -> typing.List[typing.List[typing.Optional[int]]]:
    import copy

    n = len(graph)
    graph = copy.deepcopy(graph)
    h = bellman_ford_sparse(
        graph + [[(i, 0) for i in range(n)]],
        n,
    )[:-1]
    # potential
    for u in range(n):
        for i, (v, w) in enumerate(graph[u]):
            if w is None or h[u] is None or h[v] is None:
                continue
            graph[u][i] = (v, w + h[u] - h[v])
    dists: typing.List[typing.List[typing.Optional[int]]] = []
    for u in range(n):
        dist = dijkstra_sparse(graph, u)
        for v in range(n):
            if dist[v] is None or h[u] is None or h[v] is None:
                continue
            dist[v] -= h[u] - h[v]
        dists.append(dist)
    return dists
