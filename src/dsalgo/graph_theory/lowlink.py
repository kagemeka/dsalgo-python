import typing 


def lowlink_undirected(
    n: int,
    edges: typing.List[typing.Tuple[int, int]],
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    graph: typing.List[typing.List[typing.Tuple[int, int]]] = [
        [] for _ in range(n)
    ]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, i))
        graph[v].append((u, i))
    order = [-1] * n
    lowlink = [-1] * n
    ord = 0

    def dfs(u: int, edge_id_to_u: int) -> None:
        nonlocal ord
        order[u] = lowlink[u] = ord
        ord += 1
        for v, edge_id in graph[u]:
            if edge_id == edge_id_to_u:
                continue
            if order[v] != -1:
                lowlink[u] = min(lowlink[u], order[v])
                continue
            dfs(v, edge_id)
            lowlink[u] = min(lowlink[u], lowlink[v])
    
    for i in range(n):
        if order[i] == -1:
            dfs(i, -1)
    return order, lowlink


def lowlink_directed():
    ...


def bridges_lowlink(
    n: int,
    edges: typing.List[typing.Tuple[int, int]],
) -> typing.List[int]:
    # bridge is defined on undirected graph.
    # https://cp-algorithms.com/graph/bridge-searching.html
    order, lowlink = lowlink_undirected(n, edges)
    bridge_ids: typing.List[int] = []
    for i, (u, v) in enumerate(edges):
        if order[u] > order[v]:
            u, v = v, u
        if lowlink[v] > order[u]:
            bridge_ids.append(i)
    return bridge_ids


def strong_bridges():
    ...


def articulation_points_lowlink(
    n: int,
    edges: typing.List[typing.Tuple[int, int]],
) -> typing.List[int]:
    # articulation point is defined on undirected graph.
    # https://cp-algorithms.com/graph/cutpoints.html
    graph: typing.List[typing.List[typing.Tuple[int, int]]] = [
        [] for _ in range(n)
    ]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, i))
        graph[v].append((u, i))
    order = [-1] * n
    lowlink = [-1] * n
    ord = 0
    articulation_points: typing.List[int] = []

    def dfs(u: int, edge_id_to_u: int) -> None:
        nonlocal ord
        order[u] = lowlink[u] = ord
        ord += 1
        num_childs = 0
        is_articulation = False
        for v, edge_id in graph[u]:
            if edge_id == edge_id_to_u:
                continue
            if order[v] != -1:
                lowlink[u] = min(lowlink[u], order[v])
                continue
            num_childs += 1
            dfs(v, edge_id)
            lowlink[u] = min(lowlink[u], lowlink[v])
            is_articulation |= edge_id_to_u != -1 and lowlink[v] >= order[u]
        is_articulation |= edge_id_to_u == -1 and num_childs >= 2 
        if is_articulation:
            articulation_points.append(u)
    
    for i in range(n):
        if order[i] == -1:
            dfs(i, -1)
    print(order, lowlink)
    return sorted(articulation_points)


def strong_articulation_points():
    ...




# edges = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 3)]
# n = 5
# print(bridges_lowlink(n, edges))



# print(articulation_points_lowlink(n, edges))
# print(edges)