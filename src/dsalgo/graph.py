import dataclasses
import typing

T = typing.TypeVar("T")
U = typing.TypeVar("U")


@dataclasses.dataclass
class Edge(typing.Generic[T]):
    u: int
    v: int
    data: typing.Optional[T] = None


@dataclasses.dataclass
class Graph(typing.Generic[T, U]):
    nodes: list[typing.Optional[T]]
    edges: list[list[Edge[U]]]


def add_edge(graph: Graph[T, U], edge: Edge[U]) -> None:
    graph.edges[edge.u].append(edge)


def create_graph(n: int) -> Graph[T, U]:
    return Graph(
        nodes=[None] * n,
        edges=[[] for _ in range(n)],
    )


@dataclasses.dataclass
class UndirectedGraph(typing.Generic[T, U]):
    nodes: list[typing.Optional[T]]
    edges: list[Edge[U]]


def create_undirected_graph(n: int) -> UndirectedGraph[T, U]:
    return UndirectedGraph(
        nodes=[None] * n,
        edges=[],
    )


def to_directed(
    graph: UndirectedGraph[T, U],
) -> Graph[T, U]:
    new_graph: Graph[T, U] = create_graph(size_of(graph))
    new_graph.nodes = graph.nodes
    for edge in graph.edges:
        add_edge(new_graph, edge)
    return new_graph


@dataclasses.dataclass
class DenseGraph(typing.Generic[T, U]):
    nodes: list[typing.Optional[T]]
    edge_datas: list[list[typing.Optional[U]]]


def create_dense_graph(n: int) -> DenseGraph[T, U]:
    return DenseGraph(
        nodes=[None] * n,
        edge_datas=[[None] * n for _ in range(n)],
    )


def size_of(
    graph: typing.Union[
        Graph[T, U],
        UndirectedGraph[T, U],
        DenseGraph[T, U],
    ],
) -> int:
    return len(graph.nodes)
