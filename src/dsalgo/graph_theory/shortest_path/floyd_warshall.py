import typing

from dsalgo.graph_theory.shortest_path.error import NegativeCycleError


def floyd_warshall(
    dense_graph: typing.List[typing.List[typing.Optional[int]]],
) -> typing.List[typing.List[typing.Optional[int]]]:
    import copy

    dist = copy.deepcopy(dense_graph)
    n = len(dist)
    for i in range(n):
        dist[i][i] = 0
    assert all(len(edges) == n for edges in dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] is None or dist[k][j] is None:
                    continue
                d = dist[i][k] + dist[k][j]
                if dist[i][j] is None or d < dist[i][j]:
                    dist[i][j] = d
    for i in range(n):
        if dist[i][i] < 0:
            raise NegativeCycleError
    return dist
