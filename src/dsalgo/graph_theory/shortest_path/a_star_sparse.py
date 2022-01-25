import typing


def A_star_sparse(
    graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
    dst: int,
    heuristic_func: typing.Callable[[int, int], int],
) -> typing.Optional[int]:
    import heapq

    n = len(graph)
    costs: typing.List[typing.Optional[int]] = [None] * n
    costs[src] = 0
    hq = [(heuristic_func(src, dst) + 0, 0, src)]  # score, negative_cost, node
    while hq:
        _, cost_u, u = heapq.heappop(hq)
        cost_u *= -1
        if u == dst:
            return cost_u
        if cost_u >= costs[u]:
            continue
        for v, w in graph[u]:
            cost_v = cost_u + w
            if costs[v] is not None and cost_v >= costs[v]:
                continue
            costs[v] = cost_v
            heapq.heappush(hq, (heuristic_func(v, dst) + cost_v, -cost_v, v))
    return None
