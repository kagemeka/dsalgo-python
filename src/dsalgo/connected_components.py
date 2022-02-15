from __future__ import annotations


def union_find(
    n: int,
    edges: list[tuple[int, int]],
) -> list[int]:
    from dsalgo.union_find import UnionFind, get_labels

    """Compute Connected Components with Union-Find.

    Args:
        n (int): the number of graph nodes.
        edges (list[tuple[int, int]]): undirected graph edges.

    Returns:
        list[int]: label for each node.
    """
    uf = UnionFind(n)
    for u, v in edges:
        uf.unite(u, v)
    return get_labels(uf)


def bfs(
    n: int,
    edges: list[tuple[int, int]],
) -> list[int]:
    graph: list[list[int]] = [[] for _ in range(n)]
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


def dfs(
    n: int,
    edges: list[tuple[int, int]],
) -> list[int]:
    graph: list[list[int]] = [[] for _ in range(n)]
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


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
