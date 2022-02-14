"""
Graph Theory

"""

import typing


def tree_bfs(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    que = [root]
    for u in que:
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            que.append(v)
    return parent, depth
