from __future__ import annotations

import dataclasses
import typing

T = typing.TypeVar("T")


@dataclasses.dataclass
class SinglyLinkedListNode(typing.Generic[T]):
    value: T
    next: typing.Optional[SinglyLinkedListNode] = None


@dataclasses.dataclass
class DoublyLinkedListNode(typing.Generic[T]):
    value: T
    left: typing.Optional[DoublyLinkedListNode] = None
    right: typing.Optional[DoublyLinkedListNode] = None
