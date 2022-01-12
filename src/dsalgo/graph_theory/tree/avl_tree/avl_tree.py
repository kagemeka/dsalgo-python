from __future__ import annotations
import typing 


import dataclasses 
from dsalgo.algebra.abstract.order import Order
    
        
K = typing.TypeVar('K', bound=Order)
V = typing.TypeVar('V')


@dataclasses.dataclass
class Node(typing.Generic[K, V]):
    key: K
    value: typing.Optional[V] = None 
    left: typing.Optional[Node[K, V]] = None 
    right: typing.Optional[Node[K, V]] = None
    height: int = 1


# https://www.programiz.com/dsa/avl-tree
class AVLTree(typing.Generic[K, V]):
    __root: typing.Optional[Node[K, V]]

    def __init__(self) -> None:
        self.__root = None

    def isnert(self, key: K, value: typing.Optional[V]) -> None:
        node = Node(key=key, value=value)
        if self.__root is None:
            self.__root = node
            return 
        
        if key <= self.__root.key:
            if self.__root is None:
                self.__root.left = node
                return
            else:
                assert self.__root.left is not None
                self.__root.left = left_rotate(self.__root.left)
        else:
            ...
            
    def remove(self, key: K) -> None:
        ...
    

def left_rotate(node: Node[K, V]) -> Node[K, V]:
    u = node.right 
    assert u is not None
    u.left, node.right = node, u.left
    return u


def right_rotate(node: Node[K, V]) -> Node[K, V]:
    u = node.left 
    assert u is not None 
    u.right, node.left = node, u.right
    return u



