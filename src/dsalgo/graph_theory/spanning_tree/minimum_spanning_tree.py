import typing

from dsalgo.constant import INT_INF
from dsalgo.graph_theory.components.connected_components.connected_components import (
    connected_components_union_find,
)
from dsalgo.graph_theory.union_find import UnionFind


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


def mst_kruskal_unionfind(
    n: int,
    edges: typing.List[typing.Tuple[int, int, int]],
) -> typing.List[typing.Tuple[int, int, int]]:
    edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    mst_edges: typing.List[typing.Tuple[int, int, int]] = []
    for u, v, weight in edges:
        if uf.find(u) == uf.find(v):
            continue
        mst_edges.append((u, v, weight))
        uf.unite(u, v)
    return mst_edges


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


# O(V^2)
def mst_prime_dense(
    graph: typing.List[typing.List[int]],
) -> typing.List[typing.Tuple[int, int, int]]:
    n = len(graph)
    for u in range(1, n):
        for v in range(u):
            assert graph[u][v] == graph[v][u]
    mst_edges: typing.List[typing.Tuple[int, int, int]] = []
    min_edge = [(-1, INT_INF)] * n  # (previous node, weight)
    min_edge[0] = (-1, 0)
    visited = [False] * n
    for _ in range(n):
        pre = -1
        u = -1
        weight_to_u = INT_INF
        for i in range(n):
            if visited[i] or min_edge[i][1] >= weight_to_u:
                continue
            u = i
            pre, weight_to_u = min_edge[i]
        assert weight_to_u < INT_INF
        visited[u] = True
        if pre != -1:
            mst_edges.append((pre, u, weight_to_u))
        for v in range(n):
            if visited[v] or graph[u][v] >= min_edge[v][1]:
                continue
            min_edge[v] = (u, graph[u][v])
    assert len(mst_edges) == n - 1
    return mst_edges


# O(E\log{V})
def mst_boruvka(
    n: int,
    edges: typing.List[typing.Tuple[int, int, int]],
) -> typing.List[typing.Tuple[int, int, int]]:
    m = len(edges)
    is_added = [False] * m
    mst_edges: typing.List[typing.Tuple[int, int, int]] = []
    while True:  # O(\log{N}) times loop.
        label = connected_components_union_find(
            n,
            [(u, v) for u, v, _ in mst_edges],
        )
        k = max(label) + 1
        if k == 1:
            break
        min_edge = [-1] * k  # for each component.
        for i, (u, v, weight) in enumerate(edges):
            u, v = label[u], label[v]
            if u == v:
                continue
            if min_edge[u] == -1 or weight < edges[min_edge[u]][2]:
                min_edge[u] = i
            if min_edge[v] == -1 or weight < edges[min_edge[v]][2]:
                min_edge[v] = i

        for i in min_edge:
            if is_added[i]:
                continue
            mst_edges.append(edges[i])
            is_added[i] = True
    return mst_edges


def reverse_delete():
    ...


def randomized_linear():
    ...
