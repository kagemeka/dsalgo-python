import typing


def bfs_sparse(
    g: typing.List[typing.List[int]],
    src: int,
) -> typing.List[int]:
    n = len(g)
    dist = [1 << 60] * n
    dist[src] = 0
    que = [src]
    for u in que:
        for v in g[u]:
            dv = dist[u] + 1
            if dv >= dist[v]:
                continue
            dist[v] = dv
            que.append(v)
    return dist


Numeric = typing.Union[int, float]


def dijkstra_sparse(
    g: typing.List[typing.Tuple[int, Numeric]],
    src: int,
) -> typing.List[typing.Optional[Numeric]]:
    import heapq

    n = len(g)
    dist = [None] * n
    dist[src] = 0
    hq = [(0, src)]
    while hq:
        du, u = heapq.heappop(hq)
        if du > dist[u]:
            continue
        for v, w in g[u]:
            dv = du + w
            if dist[v] is not None and dv >= dist[v]:
                continue
            dist[v] = dv
            heapq.heappush(hq, (dv, v))
    return dist


def dijkstra_dense(
    g: typing.List[typing.List[Numeric]],
    src: int,
) -> typing.List[Numeric]:
    inf = 1 << 60
    n = len(g)
    assert 0 <= src < n
    for i in range(n):
        for j in range(n):
            assert g[i][j] >= 0
    dist = [inf] * n
    dist[src] = 0
    fixed = [False] * n
    for _ in range(n - 1):
        u, du = -1, inf
        for i in range(n):
            if fixed[i] or dist[i] >= du:
                continue
            u, du = i, dist[i]
        if u == -1:
            break
        fixed[u] = True
        for v in range(n):
            dist[v] = min(dist[v], du + g[u][v])
    return dist


def bellmand_ford_sparse(
    g: list[list[tuple[int, int]]], src: int
) -> list[int]:
    n = len(g)
    dist = [1 << 60] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, w in g[u]:
                dist[v] = min(dist[v], dist[u] + w)
    for u in range(n):
        for v, w in g[u]:
            if dist[u] + w >= dist[v]:
                continue
            raise Exception("Negative cycle found.")
    return dist


def johnson_sparse(g: list[list[tuple[int, int]]]) -> list[list[int]]:
    import copy

    n = len(g)
    t = copy.deepcopy(g)
    t.append([(i, 0) for i in range(n)])
    h = bellmand_ford_sparse(t, n)[:-1]
    for u in range(n):
        g[u] = [*map(lambda v, w: (v, w + h[u] - h[v]), g[u])]
    dist = [None] * n
    for i in range(n):
        d = dijkstra_sparse(g, i)
        dist[i] = [d[j] - h[i] + h[j] for j in range(n)]
    return dist


def floyd_warshall(g: list[list[int]]) -> NoReturn:
    n = len(g)
    assert len(g[0]) == n
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    for i in range(n):
        if g[i][i] < 0:
            raise Exception("Negative cycle found.")


def A_star_sparse(
    g: list[list[tuple[int, int]]],
    src: int,
    dst: int,
    hf: typing.Callable[[int, int], int],
) -> int:
    import heapq

    n = len(g)
    inf = 1 << 60
    cost = [inf] * n
    hq = [(hf(src, dst) + 0, 0, src)]
    while hq:
        _, cu, u = heapq.heappop(hq)
        cu *= -1
        if u == dst:
            return cu
        if cu >= cost[u]:
            continue
        for v, w in g[u]:
            cv = cu + w
            if cv >= cost[v]:
                continue
            heapq.heappush(q, (hf(v, dst) + cv, -cv, v))
    return inf


def zero_one_bfs_sparse(
    g: list[list[tuple[int, int]]],
    src: int,
) -> list[int]:
    import collections

    n = len(g)
    dist = [1 << 60] * n
    dist[src] = 0
    dq = collections.deque([src])
    while dq:
        u = dq.popleft()
        for v, w in g[u]:
            dv = dist[u] + w
            if dv >= dist[v]:
                continue
            dist[v] = dv
            if w:
                dq.append(v)
            else:
                dq.appendleft(v)
    return dist


def desopo_papge(g: list[list[tuple[int, int]]], src: int) -> list[int]:
    import collections

    n = len(g)
    dist = [1 << 60] * n
    dist[src] = 0
    dq = collections.deque([src])
    state = [-1] * n
    while dq:
        u = dq.popleft()
        state[u] = 0
        for v, w in g[u]:
            dv = dist[u] + w
            if dv >= dist[v]:
                continue
            dist[v] = dv
            if state[v] == 1:
                continue
            if state[v] == -1:
                dq.append(v)
            else:
                dq.appendleft(v)
            state[v] = 1
    return dist


def viterbi():
    ...


def count_dijkstra_sparse():
    ...
