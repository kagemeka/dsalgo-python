import typing

from dsalgo.graph_theory.union_find.union_find import UnionFind


def mst_kruskal_unionfind(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[tuple[int, int, int]]:
    edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    mst_edges: list[tuple[int, int, int]] = []
    for u, v, weight in edges:
        if uf.find(u) == uf.find(v):
            continue
        mst_edges.append((u, v, weight))
        uf.unite(u, v)
    return mst_edges
