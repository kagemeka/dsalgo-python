import typing

from dsalgo.graph_theory.tree_algo.tree_bfs import tree_bfs


def heavy_light_decompose(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.List[int]:
    # range query: O(\log^2{N})
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    labels = [-1] * n
    label = 0

    def dfs(u: int, parent: int) -> int:
        nonlocal label
        size_u = 1
        heavy_node, max_size = None, 0
        for v in graph[u]:
            if v == parent:
                continue
            size_v = dfs(v, u)
            size_u += size_v
            if size_v > max_size:
                heavy_node, max_size = v, size_v
        if heavy_node is None:
            labels[u] = label
            label += 1
        else:
            labels[u] = labels[heavy_node]
        return size_u

    dfs(root, -1)
    return labels


def compute_roots(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
    labels: typing.List[int],
) -> typing.List[int]:
    n = len(tree_edges) + 1
    k = max(labels) + 1
    roots = [-1] * k
    min_depth = [n] * k
    _, depth = tree_bfs(tree_edges, root)
    for i, label in enumerate(labels):
        if depth[i] < min_depth[label]:
            min_depth[label] = depth[i]
            roots[label] = i
    return roots


# edges = [
#     (0, 1),
#     (0, 6),
#     (0, 10),
#     (1, 2),
#     (1, 5),
#     (2, 3),
#     (2, 4),
#     (6, 7),
#     (7, 8),
#     (7, 9),
#     (10, 11),
# ]
# root = 0
# labels = hl_decompose(edges, root)
# print(labels)
# roots = compute_roots(edges, root, labels)
# print(roots)