import typing

from dsalgo.graph_theory.shortest_path.shortest_path_error import (
    NegativeCycleError,
)


def bellman_ford_sparse(
    graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
) -> typing.List[typing.Optional[int]]:
    n = len(graph)
    dist: typing.List[typing.Optional[int]] = [None] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] is None:
                    continue
                dist_v = dist[u] + w
                if dist[v] is None or dist_v < dist[v]:
                    dist[v] = dist_v
    for u in range(n):
        for v, w in graph[u]:
            if dist[u] is None:
                continue
            if dist[v] is None or dist[u] + w < dist[v]:
                raise NegativeCycleError
    return dist
