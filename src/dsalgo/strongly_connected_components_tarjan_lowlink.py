import typing


def scc_tarjan_lowlink(
    graph: list[list[int]],
) -> list[int]:
    n = len(graph)
    stack: list[int] = []
    on_stack = [False] * n
    order = [-1] * n
    lowlink = [-1] * n
    ord = 0
    labels = [-1] * n
    label = 0

    def dfs(u: int) -> None:
        nonlocal ord, label
        order[u] = lowlink[u] = ord
        ord += 1
        stack.append(u)
        on_stack[u] = True
        for v in graph[u]:
            if order[v] == -1:
                dfs(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif on_stack[v] and order[v] < lowlink[u]:
                lowlink[u] = order[v]

        if lowlink[u] != order[u]:
            return
        while True:
            v = stack.pop()
            on_stack[v] = False
            labels[v] = label
            if v == u:
                break
        label += 1

    for i in range(n):
        if order[i] == -1:
            dfs(i)
    return labels
