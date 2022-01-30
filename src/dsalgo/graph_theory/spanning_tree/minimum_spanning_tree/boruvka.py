import typing

from dsalgo.graph_theory.components.connected_components.union_find import (
    connected_components_union_find,
)


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
