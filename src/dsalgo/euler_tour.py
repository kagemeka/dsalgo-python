"""
Graph Theory

"""

import typing


def euler_tour_recurse(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.List[int]:
    """Euler Tour.

    Args:
        tree_edges (typing.List[typing.Tuple[int, int]]):
            undirected graph edges.
        root (int): tour root node.

    Returns:
        typing.List[int]: the result array represent the tour on edges.

    Examples:
        >>> edges = [(0, 1), (0, 3), (1, 4), (1, 2)]
        >>> euler_tour(edges, 0)
        [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
    """
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    parent: typing.List[typing.Optional[int]] = [None] * n
    tour: typing.List[int] = []

    def dfs(u: int) -> None:
        tour.append(u)
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            dfs(v)
        tour.append(~u)

    dfs(root)
    return tour


def euler_tour(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.List[int]:
    """Euler Tour.

    Args:
        tree_edges (typing.List[typing.Tuple[int, int]]):
            undirected graph edges.
        root (int): tour root node.

    Returns:
        typing.List[int]: the result array represent the tour on edges.

    Examples:
        >>> edges = [(0, 1), (0, 3), (1, 4), (1, 2)]
        >>> euler_tour(edges, 0)
        [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
    """
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    parent: typing.List[typing.Optional[int]] = [None] * n
    tour = [-1] * (n << 1)

    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u
        if u < 0:
            continue
        st.append(~u)
        for v in graph[u][::-1]:
            if v == parent[u]:
                continue
            parent[v] = u
            st.append(v)
    return tour


def to_nodes(tour_edges: typing.List[int]) -> typing.List[int]:
    """Convert Euler-tour-on-edges to Euler-tour-on-nodes.

    Args:
        tour_edges (typing.List[int]): euler tour on edges.

    Returns:
        typing.List[int]: euler tour on nodes.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> to_nodes(tour_edges)
        [0, 1, 4, 1, 2, 1, 0, 3, 0]
    """
    parent = compute_parent(tour_edges)
    tour_nodes: typing.List[int] = []
    for u in tour_edges[:-1]:
        if u >= 0:
            tour_nodes.append(u)
        else:
            p = parent[~u]
            assert p is not None
            tour_nodes.append(p)
    return tour_nodes


def compute_parent(
    tour_edges: typing.List[int],
) -> typing.List[typing.Optional[int]]:
    """Compute parent from Euler-tour-on-edges.

    Args:
        tour_edges (typing.List[int]): euler tour on edges.

    Returns:
        typing.List[typing.Optional[int]]:
            parent list.
            the tour root's parent is None.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> compute_parent(tour_edges)
        [None, 0, 1, 0, 1]
    """
    n = len(tour_edges) >> 1
    parent: typing.List[typing.Optional[int]] = [None] * n
    st = [tour_edges[0]]
    for u in tour_edges[1:]:
        if u < 0:
            st.pop()
            continue
        parent[u] = st[-1]
        st.append(u)

    return parent


def compute_depth(tour_edges: typing.List[int]) -> typing.List[int]:
    """Compute depth from Euler-tour-on-edges.

    Args:
        tour_edges (typing.List[int]): euler tour on edges.

    Returns:
        typing.List[int]: depth list.

    Examples:
        >>> tour_edges = [0, 1, 4, -5, 2, -3, -2, 3, -4, -1]
        >>> compute_depth(tour_edges)
        [0, 1, 2, 1, 2]

    """
    n = len(tour_edges) >> 1
    parent = compute_parent(tour_edges)
    depth = [0] * n
    for u in tour_edges[1:]:
        if u < 0:
            continue
        p = parent[u]
        assert p is not None
        depth[u] = depth[p] + 1
    return depth


def compute_first_index(tour_nodes: typing.List[int]) -> typing.List[int]:
    """Compute first index in euler tour from euler tour on nodes.

    Args:
        tour_nodes (typing.List[int]): euler tour on nodes.

    Returns:
        typing.List[int]: first indices.

    Examples:
        >>> tour_nodes = [0, 1, 4, 1, 2, 1, 0, 3, 0]
        >>> compute_first_index(tour_nodes)
        [0, 1, 4, 7, 2]
    """
    n = len(tour_nodes) + 1 >> 1
    first_idx = [-1] * n
    for i, u in enumerate(tour_nodes):
        if first_idx[u] == -1:
            first_idx[u] = i
    return first_idx


def compute_last_index(tour_nodes: typing.List[int]) -> typing.List[int]:
    """Compute last index in euler tour from euler tour on nodes.

    Args:
        tour_nodes (typing.List[int]): euler tour on nodes.

    Returns:
        typing.List[int]: last indices.

    Examples:
        >>> tour_nodes = [0, 1, 4, 1, 2, 1, 0, 3, 0]
        >>> compute_last_index(tour_nodes)
        [8, 5, 4, 7, 2]
    """

    n = len(tour_nodes) + 1 >> 1
    last_idx = [-1] * n
    for i, u in enumerate(tour_nodes):
        last_idx[u] = i
    return last_idx


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
