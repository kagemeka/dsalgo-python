import typing


def bfs_sparse(
    graph: typing.List[typing.List[int]],
    src: int,
) -> typing.List[typing.Optional[int]]:
    n = len(graph)
    dist: typing.List[typing.Optional[int]] = [None] * n
    dist[src] = 0
    que = [src]
    for u in que:
        assert dist[u] is not None
        for v in graph[u]:
            dist_v = dist[u] + 1
            if dist[v] is not None and dist_v >= dist[v]:
                continue
            dist[v] = dist_v
            que.append(v)
    return dist


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
