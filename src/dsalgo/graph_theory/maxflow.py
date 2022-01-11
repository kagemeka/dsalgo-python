import typing


# O(EV^2)
def maxflow_dinic(
    capacity_graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)
    level = [-1] * n

    def update_level() -> None:
        nonlocal graph, level
        for i in range(n):
            level[i] = -1
        level[src] = 0
        que = [src]
        for u in que:
            for v in graph[u]:
                if level[v] != -1:
                    continue
                level[v] = level[u] + 1
                que.append(v)

    def flow_to_sink(u: int, flow_in: int) -> int:
        nonlocal residual_flow, graph, level
        if u == sink:
            return flow_in
        flow_out = 0
        edges = graph[u].copy()
        graph[u].clear()
        for v in edges:
            if level[v] == -1 or level[v] <= level[u]:
                graph[u].append(v)
                continue
            flow = flow_to_sink(v, min(flow_in, residual_flow[u][v]))
            residual_flow[u][v] -= flow
            if residual_flow[u][v] > 0:
                graph[u].append(v)
            if residual_flow[v][u] == 0 and flow > 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
            flow_in -= flow
            flow_out += flow
        return flow_out

    inf = 1 << 63
    flow = 0
    while True:
        update_level()
        if level[sink] == -1:
            break
        flow += flow_to_sink(src, inf)
    return flow


# O(V^2 + Ef)
def maxflow_ford_fulkerson(
    capacity_graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)
    visited = [False] * n

    def augment_flow(u: int, flow_in: int) -> int:
        visited[u] = True
        if u == sink:
            return flow_in
        edges = graph[u].copy()
        graph[u].clear()
        flow = 0
        for v in edges:
            if visited[v] or flow > 0:
                graph[u].append(v)
                continue
            flow = augment_flow(v, min(flow_in, residual_flow[u][v]))
            residual_flow[u][v] -= flow
            if residual_flow[u][v] > 0:
                graph[u].append(v)
            if flow == 0:
                continue
            if residual_flow[v][u] == 0:
                graph[v].append(u)
            residual_flow[v][u] += flow
        return flow

    inf = 1 << 63
    flow = 0
    while True:
        for i in range(n):
            visited[i] = False
            f = augment_flow(src, inf)
            if f == 0:
                break
            flow += f
    return flow


# O(V^2 + VE^2)
def maxflow_edmonds_karp(
    capacity_graph: typing.List[typing.List[typing.Tuple[int, int]]],
    src: int,
    sink: int,
) -> int:
    n = len(capacity_graph)
    residual_flow = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in capacity_graph[u]:
            residual_flow[u][v] += capacity

    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if residual_flow[u][v] > 0:
                graph[u].append(v)

    def find_path() -> typing.List[int]:
        ...


#     fn find_path(rf: &Vec<Vec<u64>>, g: &mut Vec<Vec<usize>>, src: usize, sink: usize) -> Vec<usize> {
#         let n = g.len();
#         let mut parent = vec![n; n];
#         parent[src] = src;
#         let mut que = std::collections::VecDeque::new();
#         que.push_back(src);
#         while let Some(u) = que.pop_front() {
#             g[u].retain(|&v| rf[u][v] != 0);
#             for &v in g[u].iter() {
#                 if parent[v] != n { continue; }
#                 parent[v] = u;
#                 que.push_back(v);
#             }
#         }
#         let mut v = sink;
#         let mut path = vec![v];
#         while parent[v] != n && parent[v] != v {
#             v = parent[v];
#             path.push(v);
#         }
#         path
#     }

#     fn augment_flow(rf: &mut Vec<Vec<u64>>, g: &mut Vec<Vec<usize>>, path: &Vec<usize>) -> u64 {
#         let mut flow = std::u64::MAX;
#         for i in 0..path.len() - 1 {
#             flow = std::cmp::min(flow, rf[path[i + 1]][path[i]]);
#         }
#         for i in 0..path.len() - 1 {
#             let u = path[i + 1];
#             let v = path[i];
#             rf[u][v] -= flow;
#             if rf[v][u] == 0 { g[v].push(u); }
#             rf[v][u] += flow;
#         }
#         flow
#     }

#     let mut flow = 0;
#     loop {
#         let path = find_path(&rf, &mut g, src, sink);
#         if path.len() == 1 { break; }
#         let f = augment_flow(&mut rf, &mut g, &path);
#         flow += f;
#     }
#     flow
# }


def mpm():
    ...


def push_relabel_fifo_verted():
    ...


def push_relabel_dist_verted():
    ...


def push_relabel_dynamic_tree():
    ...


def krt():
    ...


def binary_blocking_flow():
    ...


def orlin():
    ...
