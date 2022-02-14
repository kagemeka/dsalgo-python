import typing


def transpose_graph(
    graph: typing.List[typing.List[int]],
) -> typing.List[typing.List[int]]:
    n = len(graph)
    new_graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            new_graph[v].append(u)
    return new_graph


def scc_kosaraju(graph: typing.List[typing.List[int]]) -> typing.List[int]:
    n = len(graph)
    visited = [False] * n
    que: typing.List[int] = []
    t_graph = transpose_graph(graph)
    labels = [-1] * n
    label = 0

    def dfs(u: int) -> None:
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        que.append(u)

    def rev_dfs(u: int, label: int):
        labels[u] = label
        for v in t_graph[u]:
            if labels[v] == -1:
                rev_dfs(v, label)

    for u in range(n):
        if not visited[u]:
            dfs(u)
    for u in que[::-1]:
        if labels[u] != -1:
            continue
        rev_dfs(u, label)
        label += 1
    return labels
