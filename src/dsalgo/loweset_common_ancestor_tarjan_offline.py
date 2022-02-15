"""
Graph Theory
"""


import typing

from dsalgo.graph_theory.union_find.union_find import UnionFind


def lca_tarjan_offline(
    tree_edges: list[tuple[int, int]],
    root: int,
    query_pairs: list[tuple[int, int]],
) -> list[int]:
    n = len(tree_edges) + 1
    graph: list[list[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    queries: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for i, (u, v) in enumerate(query_pairs):
        queries[u].append((v, i))
        queries[v].append((u, i))
    visited = [False] * n
    uf = UnionFind(n)
    ancestor = [n] * n
    lca = [n] * len(query_pairs)

    def dfs(u: int) -> None:
        visited[u] = True
        ancestor[u] = u
        for v in graph[u]:
            if visited[v]:
                continue
            dfs(v)
            uf.unite(u, v)
            ancestor[uf.find(u)] = u

        for v, query_id in queries[u]:
            if visited[v]:
                lca[query_id] = ancestor[uf.find(v)]

    dfs(root)
    return lca
