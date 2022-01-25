import typing


def dijkstra_sparse(
    graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
) -> typing.List[typing.Optional[int]]:
    import heapq

    n = len(graph)
    dist: typing.List[typing.Optional[int]] = [None] * n
    dist[src] = 0
    hq = [(0, src)]
    while hq:
        dist_u, u = heapq.heappop(hq)
        if dist_u > dist[u]:
            continue
        for v, w in graph[u]:
            dist_v = dist_u + w
            if dist[v] is not None and dist_v >= dist[v]:
                continue
            dist[v] = dist_v
            heapq.heappush(hq, (dist_v, v))
    return dist
