import typing

from dsalgo.constant import INT_INF


# O(V^2)
def mst_prime_dense(
    graph: list[list[int]],
) -> list[tuple[int, int, int]]:
    n = len(graph)
    for u in range(1, n):
        for v in range(u):
            assert graph[u][v] == graph[v][u]
    mst_edges: list[tuple[int, int, int]] = []
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
