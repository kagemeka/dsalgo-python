import typing


def is_bipartite(graph: typing.List[typing.List[int]]) -> bool:
    n = len(graph)
    assert n >= 1
    label = [-1] * n
    label[0] = 0
    que = [0]
    for u in que:
        for v in graph[u]:
            if label[v] == label[u]:
                return False
            if label[v] != -1:
                continue
            label[v] = label[u] ^ 1
            que.append(v)
    assert all(l != -1 for l in label)
    return True


def label_bipartite(g: typing.List[typing.List[int]]) -> typing.List[int]:
    assert is_bipartite(g)
    n = len(g)
    label = [-1] * n
    label[0] = 0
    que = [0]
    for u in que:
        for v in g[u]:
            if label[v] != -1:
                continue
            label[v] = label[u] ^ 1
            que.append(v)
    return label
