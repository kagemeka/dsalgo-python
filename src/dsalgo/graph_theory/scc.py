def scc(self):  # strongly connected components
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
