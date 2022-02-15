"""
Container
"""

from __future__ import annotations

import dataclasses
import typing

T = typing.TypeVar("T")


@dataclasses.dataclass
class Node(typing.Generic[T]):
    value: T
    next: typing.Optional[Node[T]] = None


def add_last(
    last: typing.Optional[Node[T]],
    node: Node[T],
) -> Node[T]:
    if last is None:
        return node
    last.next = node
    return node


def pop_front(
    first: Node[T],
) -> tuple[Node[T], typing.Optional[Node[T]]]:
    popped, new_first = first, first.next
    popped.next is None
    return popped, new_first
