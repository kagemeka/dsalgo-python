
import typing 
from dsalgo.graph_theory.tree_bfs import tree_bfs 
from dsalgo.graph_theory.union_find import UnionFind

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
    
    def get(u: int, v: int) -> int:
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
    
    return get 


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


# pub fn with_hl_decomposition() {}


# pub mod eulertour_rmq {

#     use super::{SparseTable, DisjointSparseTable, euler_tour_node, Semigroup};
#     use super::{SegmentTree, Monoid};


#     pub struct WithSparseTable<'a, S> {
#         first_idx: Vec<usize>,
#         sp: DisjointSparseTable<'a, S>,
#     }
#     impl<'a> WithSparseTable<'a, (usize, usize)> {
#         pub fn new(g: &Vec<(usize, usize)>, root: usize) -> Self {
#             let (tour, first_idx, _, _, depth) = euler_tour_node(g, root);
#             let sg = Semigroup::<'a, (usize, usize)> {
#                 op: &|x, y| std::cmp::min(*x, *y),
#                 commutative: true,
#                 idempotent: true,
#             };
#             let mut a = Vec::with_capacity(tour.len());
#             for &i in tour.iter() {
#                 a.push((depth[i as usize], i as usize));
#             }
#             let sp = DisjointSparseTable::new(sg, &a);
#             Self { first_idx: first_idx, sp: sp }
#         }

#         pub fn get(&self, u: usize, v: usize) -> usize {
#             let mut l = self.first_idx[u];
#             let mut r = self.first_idx[v];
#             if l > r { std::mem::swap(&mut l, &mut r); }
#             self.sp.get(l, r + 1).1
#         }
#     }


#     pub struct WithSegmentTree<'a, S: Copy> {
#         first_idx: Vec<usize>,
#         seg: SegmentTree<'a, S>,
#     }
#     impl<'a> WithSegmentTree<'a, (usize, usize)> {
#         pub fn new(g: &Vec<(usize, usize)>, root: usize) -> Self {
#             let (tour, first_idx, _, _, depth) = euler_tour_node(g, root);
#             let m = Monoid::<'a, (usize, usize)> {
#                 op: &|x, y| std::cmp::min(*x, *y),
#                 e: &|| (std::usize::MAX, 0),
#                 commutative: true,
#                 idempotent: false,
#             };
#             let mut a = Vec::with_capacity(tour.len());
#             for &i in tour.iter() {
#                 a.push((depth[i as usize], i as usize));
#             }
#             let seg = SegmentTree::from_vec(m, &a);
#             Self { first_idx: first_idx, seg: seg }
#         }

#         pub fn get(&self, u: usize, v: usize) -> usize {
#             let mut l = self.first_idx[u];
#             let mut r = self.first_idx[v];
#             if l > r { std::mem::swap(&mut l, &mut r); }
#             self.seg.get(l, r + 1).1
#         }
#     }


#     pub struct WithSqrtDecomposition {}

# }

# /// references
# /// - https://ei1333.hateblo.jp/entry/2018/05/29/011140
# /// - https://www.slideshare.net/iwiwi/2-12188845
# pub struct WithHLD {}

def lca_euler_tour_rmq(): 
    # sparse table
    # segment tree
    # sqrt decomposition
    
    # here, using sparse table
    ...


def lca_farach_colton_bender():
    ...


def lca_hld_decomposition():
    ...
