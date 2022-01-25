import typing


def desopo_papge(
    graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
) -> typing.List[typing.Optional[int]]:
    import collections

    n = len(graph)
    dist: typing.List[typing.Optional[int]] = [None] * n
    dist[src] = 0
    dq = collections.deque([src])
    state = [-1] * n
    while dq:
        u = dq.popleft()
        state[u] = 0
        assert dist[u] is not None
        for v, w in graph[u]:
            dist_v = dist[u] + w
            if dist[v] is not None and dist_v >= dist[v]:
                continue
            dist[v] = dist_v
            if state[v] == 1:
                continue
            if state[v] == -1:
                dq.append(v)
            else:
                dq.appendleft(v)
            state[v] = 1
    return dist
