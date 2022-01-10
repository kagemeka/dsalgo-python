import typing
from dsalgo.graph_theory.union_find import (
    UnionFind,
    get_labels,
)


def connected_components_bfs(
    n: int,
    edges: typing.List[typing.Tuple[int, int]],
) -> typing.List[int]:
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    labels = [-1] * n
    label = 0
    for i in range(n):
        if labels[i] != -1:
            continue
        labels[i] = label
        que = [i]
        for u in que:
            for v in graph[u]:
                if labels[v] != -1:
                    continue
                labels[v] = label
                que.append(v)
    return labels


def connected_components_dfs(
    n: int,
    edges: typing.List[typing.Tuple[int, int]],
) -> typing.List[int]:
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    labels = [-1] * n
    label = 0

    def dfs(u: int, label: int) -> None:
        labels[u] = label
        for v in graph[u]:
            if labels[v] == -1:
                dfs(v, label)

    for i in range(n):
        if labels[i] != -1:
            continue
        dfs(i, label)
        label += 1
    return labels


def connected_components_union_find(
    n: int,
    edges: typing.List[typing.Tuple[int, int]],
) -> typing.List[int]:
    """Compute Connected Components with Union-Find.

    Args:
        n (int): the number of graph nodes.
        edges (typing.List[typing.Tuple[int, int]]): undirected graph edges.

    Returns:
        typing.List[int]: label for each node.
    """
    uf = UnionFind(n)
    for u, v in edges:
        uf.unite(u, v)
    return get_labels(uf)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
