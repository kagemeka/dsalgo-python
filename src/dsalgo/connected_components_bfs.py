import typing


def connected_components_bfs(
    n: int,
    edges: list[typing.Tuple[int, int]],
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
