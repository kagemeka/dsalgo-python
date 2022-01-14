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
# used for set, multiset, map

# concrete datastructure such a set or multiset or map should have.
# cannot implement multimap.

def insert(root: typing.Optional[Node[K, V]], node: Node[K, V]) -> Node[K, V]:
    if root is None:
        return node
    if node.key <= root.key:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    root.height = max(__get_height(root.left), __get_height(root.right)) + 1    
    balance = __get_balance(root)
    if balance < -1:  # lean to left direction
        if __get_balance(root.left) > 0:
            assert root.left is not None  # left exist (because balance < -1)
            root.left = left_rotate(root.left)
        return right_rotate(root)
    elif balance > 1:
        if __get_balance(root.right) < 0:
            assert root.right is not None
            root.right = right_rotate(root.right)
        return left_rotate(root)
    else:
        return root
    

def remove(
    root: typing.Optional[Node[K, V]], 
    node: Node[K, V],
) -> typing.Optional[Node[K, V]]:
    if root is None:
        return None
    
    

def __get_height(root: typing.Optional[Node[K, V]]) -> int:
    if root is None:
        return 0
    return root.height


def __get_balance(root: typing.Optional[Node[K, V]]) -> int:
    if root is None:
        return 0
    return __get_height(root.right) - __get_height(root.left)
    

def left_rotate(root: Node[K, V]) -> Node[K, V]:
    u = root.right 
    assert u is not None
    u.left, root.right = root, u.left
    return u


def right_rotate(root: Node[K, V]) -> Node[K, V]:
    u = root.left
    assert u is not None 
    u.right, root.left = root, u.right
    return u


root = None
for _ in range(100000):
    root = insert(root, Node(1, 1))


print(__get_height(root))