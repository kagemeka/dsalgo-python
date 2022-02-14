import typing


def dijkstra_dense(
    dense_graph: typing.List[typing.List[typing.Optional[int]]],
    src: int,
) -> typing.List[typing.Optional[int]]:
    n = len(dense_graph)
    assert 0 <= src < n
    for i in range(n):
        for j in range(n):
            assert dense_graph[i][i] is None or dense_graph[i][j] >= 0
    dist: typing.List[typing.Optional[int]] = [None] * n
    dist[src] = 0
    fixed = [False] * n
    for _ in range(n - 1):
        u: typing.Optional[int] = None
        dist_u: typing.Optional[int] = None
        for i in range(n):
            if fixed[i] or dist[i] is None:
                continue
            if dist_u is None or dist[i] < dist_u:
                u, dist_u = i, dist[i]
        if u is None:
            break
        fixed[u] = True
        for v in range(n):
            if dense_graph[u][v] is None:
                continue
            dist_v = dist_u + dense_graph[u][v]
            if dist[v] is None or dist_v < dist[v]:
                dist[v] = dist_v
    return dist
