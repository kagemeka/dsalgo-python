from kagemeka.dsa.graph_theory.union_find import UnionFind


def kruskal_uf(
    n: int, g: list[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    g = sorted(g, key=lambda e: e[2])
    uf = UnionFind(n)
    mst: list[tuple[int, int, int]] = []
    for u, v, w in g:
        if uf.find(u) == uf.find(v):
            continue
        ms.append((u, v, w))
        uf.unite(u, v)
    return mst
