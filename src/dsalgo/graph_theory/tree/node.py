from __future__ import annotations

import dataclasses
import typing

from dsalgo.algebra.abstract.order import Order

K = typing.TypeVar("K", bound=Order)
V = typing.TypeVar("V")
T = typing.TypeVar("T")


@dataclasses.dataclass
class Node(typing.Generic[K, V, T]):
    key: K
    value: typing.Optional[V] = None
    parent: typing.Optional[Node[K, V, T]] = None
    left: typing.Optional[Node[K, V, T]] = None
    right: typing.Optional[Node[K, V, T]] = None
    data: typing.Optional[T] = None
