import typing


def connected_components_dfs(
    n: int,
    edges: list[typing.Tuple[int, int]],
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
