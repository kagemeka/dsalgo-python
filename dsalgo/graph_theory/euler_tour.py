import typing


def euler_tour_dfs(
    g: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[(typing.List[int],) * 3]:
    n = len(g) + 1
    t = [[] for _ in range(n)]
    for u, v in g:
        t[u].append(v)
        t[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    tour = []

    def dfs(u: int) -> typing.NoReturn:
        tour.append(u)
        for v in t[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            dfs(v)
        tour.append(~u)

    dfs(root)
    return tour, parent, depth


def euler_tour(
    g: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Tuple[(typing.List[int],) * 3]:
    n = len(g) + 1
    t = [[] for _ in range(n)]
    for u, v in g:
        t[u].append(v)
        t[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    tour = [-1] * (n << 1)
    st = [root]
    for i in range(n << 1):
        u = st.pop()
        tour[i] = u
        if u < 0:
            continue
        st.append(~u)
        for v in t[u][::-1]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            st.append(v)
    return tour, parent, depth


def to_nodes(
    tour: typing.List[int], parent: typing.List[int]
) -> typing.List[int]:
    return [u if u >= 0 else parent[~u] for u in tour[:-1]]
