
import typing 
from dsalgo.graph_theory.tree_bfs import tree_bfs 
from dsalgo.graph_theory.union_find import UnionFind
from dsalgo.algebra.abstract.structure import Semigroup
from dsalgo.misc.sparse_table import sparse_table
from dsalgo.graph_theory.euler_tour import (
    euler_tour,
    to_nodes,
    compute_first_index,
    compute_depth,
)


def lca_binary_lifting(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    n = len(tree_edges) + 1
    parent, depth = tree_bfs(tree_edges, root)
    k = max(1, max(depth).bit_length())
    ancestor = [[n] * n for _ in range(k)]
    ancestor[0] = parent
    ancestor[0][root] = root
    for i in range(k - 1):
        for j in range(n):
            ancestor[i + 1][j] = ancestor[i][ancestor[i][j]]
    
    def get_lca(u: int, v: int) -> int:
        if depth[u] > depth[v]:
            u, v = v, u
        d = depth[v] - depth[u]
        for i in range(d.bit_length()):
            if d >> i & 1:
                v = ancestor[i][v]
        if v == u:
            return u
        for a in ancestor[::-1]:
            nu, nv = a[u], a[v]
            if nu != nv:
                u, v = nu, nv
        return parent[u]
    
    return get_lca


def lca_tarjan_offline(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
    query_pairs: typing.List[typing.Tuple[int, int]],
) -> typing.List[int]:
    n = len(tree_edges) + 1
    graph: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for u, v in tree_edges:
        graph[u].append(v)
        graph[v].append(u)
    queries: typing.List[typing.List[typing.Tuple[int, int]]] = [
        [] for _ in range(n)
    ]
    for i, (u, v) in enumerate(query_pairs):
        queries[u].append((v, i))
        queries[v].append((u, i))
    visited = [False] * n
    uf = UnionFind(n)
    ancestor = [n] * n
    lca = [n] * len(query_pairs)
    
    def dfs(u: int) -> None:
        visited[u] = True
        ancestor[u] = u
        for v in graph[u]:
            if visited[v]:
                continue
            dfs(v)
            uf.unite(u, v)
            ancestor[uf.find(u)] = u
        
        for v, query_id in queries[u]:
            if visited[v]:
                lca[query_id] = ancestor[uf.find(v)]
    
    dfs(root)
    return lca


def lca_euler_tour_rmq(
    tree_edges: typing.List[typing.Tuple[int, int]],
    root: int,
) -> typing.Callable[[int, int], int]:
    # sparse table
    # segment tree
    # sqrt decomposition
    # here, using sparse table
    tour = euler_tour(tree_edges, root)
    depth = compute_depth(tour)
    tour = to_nodes(tour)
    first_idx = compute_first_index(tour)
    semigroup = Semigroup[typing.Tuple[int, int]](op=min)
    get_min = sparse_table(semigroup, [(depth[i], i) for i in tour])
    
    def get_lca(u: int, v: int) -> int:
        left, right = first_idx[u], first_idx[v]
        if left > right:
            left, right = right, left
        return get_min(left, right + 1)[1]
    
    return get_lca


def lca_farach_colton_bender():
    ...


def lca_hld_decomposition():
    ...
