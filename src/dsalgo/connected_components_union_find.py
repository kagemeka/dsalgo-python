import typing

from dsalgo.graph_theory.union_find.union_find import UnionFind, get_labels


def connected_components_union_find(
    n: int,
    edges: list[typing.Tuple[int, int]],
) -> list[int]:
    """Compute Connected Components with Union-Find.

    Args:
        n (int): the number of graph nodes.
        edges (list[typing.Tuple[int, int]]): undirected graph edges.

    Returns:
        list[int]: label for each node.
    """
    uf = UnionFind(n)
    for u, v in edges:
        uf.unite(u, v)
    return get_labels(uf)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
