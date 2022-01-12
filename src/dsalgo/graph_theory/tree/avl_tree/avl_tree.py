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

    def insert(self, key: K, value: typing.Optional[V]) -> None:
        self.__root = self.__insert(self.__root, key, value)
        
    def __insert(self, node: typing.Optional[Node[K, V]], key: K, value: V) -> Node[K, V]:
        if node is None:
            return Node(key, value)
        
        if key <= node.key:
            node.left = self.__insert(node.left, key, value)
        else:
            node.right = self.__insert(node.right, key, value)
        
        node.height = max(
            self.__get_height(node.left),
            self.__get_height(node.right),
        ) + 1
        
        balance = self.__get_balance(node)
        
        if balance < -1:  # balancing left direction
            if self.__get_balance(node.left) <= 0:
                return right_rotate(node)
            assert node.left is not None
            node.left = left_rotate(node.left)  # left exist (balance < -1)
            return right_rotate(node)
        elif balance > 1:
            if self.__get_balance(node.right) >= 0:
                return left_rotate(node)
            assert node.right is not None
            node.right = right_rotate(node.right)
            return left_rotate(node)
        else:
            return node
            
    def __get_height(self, node: typing.Optional[Node[K, V]]) -> int:
        if node is None:
            return 0
        return node.height
    
    def __get_balance(self, node: typing.Optional[Node[K, V]]) -> int:
        if node is None:
            return 0
        return self.__get_height(node.right) - self.__get_height(node.right)
    
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



tree = AVLTree[int, int]()

tree.insert(1, 1)
tree.insert(3, 2)

print(tree._AVLTree__root)