import typing 


def hl_decompose(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.List[int]:
    # range query: O(\log^2{N})
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    roots = [-1] * n
    size = [1] * n
    
    def compute_size(u: int, parent: int) -> int:
        for v in graph[u]:
            if v != parent:
                size[u] += compute_size(v, u)
        return size[u]

    def decompose(u: int, parent: int, root: int) -> None:  # return the size of sub tree
        roots[u] = root
        heavy_node, max_size = None, 0
        for v in graph[u]:
            if v == parent:
                continue
            if size[v] > max_size:
                heavy_node, max_size = v, size[v]
        for v in graph[u]:
            if v == parent:
                continue
            decompose(v, u, root if v == heavy_node else v)
    
    compute_size(root, -1)
    decompose(root, -1, root)
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
# res = hl_decompose(edges, 0)
# print(res)