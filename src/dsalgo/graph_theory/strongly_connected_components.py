import typing 


def scc_path_based(graph: typing.List[typing.List[int]]) -> typing.List[int]:
    n = len(graph)
    order = [-1] * n
    labels = [-1] * n
    stack_0: typing.List[int] = []
    stack_1: typing.List[int] = []
    ord = 0
    label = 0
    
    def dfs(u: int) -> None:
        nonlocal ord, label
        order[u] = ord
        ord += 1
        stack_0.append(u)
        stack_1.append(u)
        for v in graph[u]:
            if order[v] == -1:
                dfs(v)
            elif labels[v] == -1:
                # v is start of a scc.
                while order[stack_0[-1]] > order[v]:
                    stack_0.pop()
        
        if stack_0[-1] != u:
            return
        while True:
            v = stack_1.pop()
            labels[v] = label
            print(u, v)
            if v == u:
                break
        label += 1
        stack_0.pop()
        
    for i in range(n):
        if order[i] == -1:
            dfs(i)
            
    return labels


g = [[1, 3], [2], [3], []]
print(scc_path_based(g))


# /// scc Tarjan with lowlink
# /// O(V + E)
# /// references
# /// - https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
# pub fn tarjan(g: &Vec<Vec<usize>>) -> Vec<usize> {
#     fn dfs(
#         g: &Vec<Vec<usize>>, 
#         order: &mut Vec<usize>,
#         low: &mut Vec<usize>,
#         label: &mut Vec<usize>,
#         on_stack: &mut Vec<bool>,
#         st: &mut Vec<usize>,
#         u: usize,
#         ord: &mut usize,
#         l: &mut usize,
#     ) {
#         order[u] = *ord;
#         low[u] = *ord;
#         *ord += 1;
#         st.push(u);
#         on_stack[u] = true;
#         for v in g[u].iter().map(|x| *x) {
#             if order[v] == g.len() {
#                 dfs(g, order, low, label, on_stack, st, v, ord, l);
#                 if low[v] < low[u] { low[u] = low[v]; }
#             } else if on_stack[v] && order[v] < low[u] {
#                 low[u] = order[v];
#             }
#         }
#         if low[u] == order[u] {
#             loop {
#                 let v = st.pop().unwrap();
#                 on_stack[v] = false;
#                 label[v] = *l;
#                 if v == u { break; }
#             }
#             *l += 1;
#         }
#     }
#     let n = g.len();
#     let mut order = vec![n; n];
#     let mut low = vec![n; n];
#     let mut label = vec![n; n];
#     let mut on_stack = vec![false; n];
#     let mut st = Vec::with_capacity(n);
#     let mut ord = 0;
#     let mut l = 0;
#     for i in 0..n {
#         if order[i] == n { dfs(g, &mut order, &mut low, &mut label, &mut on_stack, &mut st, i, &mut ord, &mut l); }
#     }
#     label
# }



# /// scc Kosaraju 
# /// O(V + E)
# /// references
# /// - https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
# pub fn kosaraju(g: &Vec<Vec<usize>>) -> Vec<usize> {
#     fn dfs(g: &Vec<Vec<usize>>, visited: &mut Vec<bool>, que: &mut Vec<usize>, u: usize) {
#         visited[u] = true;
#         for v in g[u].iter() {
#             if !visited[*v] { dfs(g, visited, que, *v); }
#         }
#         que.push(u);
#     }
#     fn rev_dfs(g: &Vec<Vec<usize>>, label: &mut Vec<usize>, l: usize, u: usize) {
#         label[u] = l;
#         for v in g[u].iter() {
#             if label[*v] == g.len() { rev_dfs(g, label, l, *v); }
#         }
#     }
#     let n = g.len();
#     let mut visited = vec![false; n];
#     let mut que = Vec::with_capacity(n);
#     let mut label = vec![n; n];
#     let mut l = 0usize;
#     for i in 0..n {
#         if !visited[i] { dfs(g, &mut visited, &mut que, i); }
#     }
#     let mut t = vec![vec![]; n];
#     for u in 0..n {
#         for v in g[u].iter() { t[*v].push(u); }
#     }
#     for i in que.iter().rev() {
#         if label[*i] != n { continue; }
#         rev_dfs(&t, &mut label, l, *i);
#         l += 1;
#     }
#     label 
# }


def scc_tarjan():
    ...

def scc_kosaraju(self):  # strongly connected components
    n = self.__N
    visited, q, label, l = [False] * n, [], [-1] * n, 0
    t = self.__class__(n)
    for u in range(n):
        for v in self.edges[u]:
            t.add_edge(v, u)

    def dfs(u: int) -> NoReturn:
        visited[u] = True
        for v in self.edges[u]:
            if not visited[v]:
                dfs(v)
        q.append(u)

    def rev_dfs(u: int, r: int):
        label[u] = l
        for v in t.edges[u]:
            if label[v] == -1:
                rev_dfs(v, r)

    for u in range(n):
        if not visited[u]:
            dfs(u)
    for u in q[::-1]:
        if label[u] != -1:
            continue
        rev_dfs(u, l)
        l += 1
    return label

