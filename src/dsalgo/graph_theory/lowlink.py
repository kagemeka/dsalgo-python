

import typing 

def compute_lowlink(
    graph: typing.List[typing.List[typing.Tuple[int, int]]],
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    n = len(graph)
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


def find_bridges(
    n: int,
    edges: typing.List[typing.Tuple[int, int]],
) -> typing.List[typing.Tuple[int, int]]:
    graph: typing.List[typing.List[typing.Tuple[int, int]]] = [
        [] for _ in range(n)
    ]
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, i))
        graph[v].append((u, i))
    order, lowlink = compute_lowlink(graph)
    bridge_ids: typing.List[typing.Tuple[int, int]] = []
    for i, (u, v) in enumerate(edges):
        if order[u] > order[v]:
            u, v = v, u
        if lowlink[v] > order[u]:
            bridge_ids.append(i)
            # bridges.append((u, v) if u < v else (v, u))
    return bridge_ids


edges = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 3)]
n = 5
print(find_bridges(n, edges))


# pub fn bridges(n: usize, g: &Vec<(usize, usize)>) -> Vec<(usize, usize)> {
#     let mut t = vec![vec![]; n];
#     for (u, v) in g {
#         t[*u].push(*v);
#         t[*v].push(*u);
#     }
#     let (order, low) = lowlink(&t);
#     let mut bridges = Vec::new();
#     for (u, v) in g {
#         let mut u = *u;
#         let mut v = *v;
#         if order[u] > order[v] { std::mem::swap(&mut u, &mut v); }
#         if low[v] <= order[u] { continue; }
#         if u > v { std::mem::swap(&mut u, &mut v); } 
#         bridges.push((u, v)); 

#     }
#     bridges.sort();
#     bridges
# }


# pub fn articulation_points(g: &Vec<Vec<usize>>) -> Vec<usize> {
#     let n = g.len();
#     let mut articulation_points = Vec::new();
#     let (order, low) = lowlink(g);
#     let mut visited = vec![false; n];
#     fn dfs(
#         g: &Vec<Vec<usize>>, 
#         u: usize, 
#         parent: usize, 
#         visited: &mut Vec<bool>,
#         order: &Vec<usize>, 
#         low: &Vec<usize>, 
#         points: &mut Vec<usize>,
#     ) {
#         let n = g.len();
#         visited[u] = true;
#         let mut cnt = 0u32;
#         let mut is_articulation = false;
#         for v in g[u].iter().map(|x| *x) {
#             if visited[v] { continue; }
#             cnt += 1;
#             dfs(g, v, u, visited, order, low, points);
#             if parent == n || low[v] < order[u] { continue; }
#             is_articulation = true;
#         }
#         if parent == n && cnt >= 2 { is_articulation = true; }
#         if is_articulation { points.push(u); }
#     }
#     for i in 0..n {
#         if visited[i] { continue; }
#         dfs(g, i, n, &mut visited, &order, &low, &mut articulation_points);
#     }
#     articulation_points.sort();
#     articulation_points
# } 