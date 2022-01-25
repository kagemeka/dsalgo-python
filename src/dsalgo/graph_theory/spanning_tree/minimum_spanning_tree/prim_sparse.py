import typing
from dsalgo.constant import INT_INF


def __to_directed(
    n: int,
    edges: typing.List[typing.Tuple[int, int, int]],
) -> typing.List[typing.List[typing.Tuple[int, ...]]]:
    graph: typing.List[typing.List[typing.Tuple[int, ...]]] = [
        [] for _ in range(n)
    ]
    for e in edges:
        u, v = e[:2]
        graph[u].append((v, *e[2:]))
        graph[v].append((u, *e[2:]))
    return graph


# O((E + V)\log{E})
def mst_prim_sparse(
    n: int,
    edges: typing.List[typing.Tuple[int, int, int]],
) -> typing.List[typing.Tuple[int, int, int]]:
    graph = __to_directed(n, edges)
    mst_edges: typing.List[typing.Tuple[int, int, int]] = []
    import heapq

    hq = [(0, -1, 0)]
    weight = [INT_INF] * n
    visited = [False] * n
    while hq:
        weight_to_u, pre, u = heapq.heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        if pre != -1:
            mst_edges.append((pre, u, weight_to_u))
        for v, weight_to_v in graph[u]:
            if visited[v] or weight_to_v >= weight[v]:
                continue
            weight[v] = weight_to_v
            heapq.heappush(hq, (weight_to_v, u, v))

    return mst_edges
