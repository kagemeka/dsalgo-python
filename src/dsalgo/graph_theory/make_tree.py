import typing


def bfs_tree(
    graph: typing.List[typing.List[int]],
    root: int,
) -> typing.List[typing.Tuple[int, int]]:
    """Compute breadth first search tree from directed graph.

    Args:
        graph (typing.List[typing.List[int]]): directed graph.
        root (int): tree root node.

    Returns:
        typing.List[typing.Tuple[int, int]]: bfs tree.

    Examples:
        >>> graph = [[1, 3], [0, 2, 3], [1, 3], [0, 1, 2]]
        >>> bfs_tree(graph, 0)
        [(0, 1), (0, 3), (1, 2)]
    """
    n = len(graph)
    tree_edges: typing.List[typing.Tuple[int, int]] = []

    added_to_que = [False] * n
    que = [root]
    added_to_que[root] = True
    for u in que:
        added_to_que[u] = True
        for v in graph[u]:
            if added_to_que[v]:
                continue
            tree_edges.append((u, v) if u < v else (v, u))
            que.append(v)
            added_to_que[v] = True
    return tree_edges


def dfs_tree(
    graph: typing.List[typing.List[int]],
    root: int,
) -> typing.List[typing.Tuple[int, int]]:
    """Compute depth first search tree from directed graph.

    Args:
        graph (typing.List[typing.List[int]]): directed graph.
        root (int): tree root node.

    Returns:
        typing.List[typing.Tuple[int, int]]: dfs tree.

    Examples:
        >>> graph = [[1, 3], [0, 2, 3], [1, 3], [0, 1, 2]]
        >>> dfs_tree(graph, 0)
        [(0, 1), (1, 2), (2, 3)]
    """
    n = len(graph)
    tree_edges: typing.List[typing.Tuple[int, int]] = []
    visited = [False] * n

    def dfs(u: int) -> None:
        visited[u] = True
        for v in graph[u]:
            if visited[v]:
                continue
            tree_edges.append((u, v) if u < v else (v, u))
            dfs(v)

    dfs(root)

    return tree_edges


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
