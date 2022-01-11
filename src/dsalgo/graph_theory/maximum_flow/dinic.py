from abc import ABCMeta, abstractmethod

from . import Graph


class MaximumFlow(Graph):
    @abstractmethod
    def maximum_flow(self, source, sink):
        ...

    def minimum_cut(self, **kwargs):
        return self.maximum_flow(**kwargs)


class DinicSparse(MaximumFlow):
    def __init__(self, **kwargs):
        super(Dinic, self).__init__(**kwargs)

    def bfs(self, source=0):
        from collections import deque

        n = len(self.nodes)
        self.lv = lv = [None] * n
        lv[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v, e in self.edges[u].items():
                if e.capacity == 0:
                    continue
                if lv[v] is not None:
                    continue
                lv[v] = lv[u] + 1
                q.append(v)

    def flow_to_sink(self, u, flow_in):
        if u == self.sink:
            return flow_in
        flow_out = 0
        for v, e in self.edges[u].items():
            if e.capacity == 0:
                continue
            if self.lv[v] <= self.lv[u]:
                continue
            flow = self.flow_to_sink(v, min(flow_in, e.capacity))
            if not flow:
                continue
            self.edges[u][v].capacity -= flow
            if u in self.edges[v]:
                self.edges[v][u].capacity += flow
            else:
                self.add_edge(v, u, capacity=flow)
            flow_in -= flow
            flow_out += flow
        return flow_out

    def maximum_flow(self, source, sink):
        self.sink = sink
        inf = float("inf")
        flow = 0
        while True:
            self.bfs(source)
            if self.lv[sink] is None:
                return flow
            flow += self.flow_to_sink(source, inf)


class FordFulkerson(MaximumFlow):
    ...


class PushRelabel(MaximumFlow):
    ...
