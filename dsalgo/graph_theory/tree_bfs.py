import typing


def tree_bfs(
    g: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[(typing.List[int],) * 2]:
    n = len(g) + 1
    t = [[] for _ in range(n)]
    for u, v in g:
        t[u].append(v)
        t[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    que = [root]
    for u in que:
        for v in t[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            que.append(v)
    return parent, depth
