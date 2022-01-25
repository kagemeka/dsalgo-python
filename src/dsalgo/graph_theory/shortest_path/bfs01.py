import typing


def bfs01_sparse(
    graph: typing.List[typing.List[tuple[int, int]]],
    src: int,
) -> typing.List[typing.Optional[int]]:
    import collections

    n = len(graph)
    dist: typing.List[typing.Optional[int]] = [None] * n
    dist[src] = 0
    dq = collections.deque([src])
    while dq:
        u = dq.popleft()
        assert dist[u] is not None
        for v, w in graph[u]:
            dist_v = dist[u] + w
            if dist[v] is not None and dist_v >= dist[v]:
                continue
            dist[v] = dist_v
            if w >= 1:
                dq.append(v)
            else:
                dq.appendleft(v)
    return dist
