import unittest

from dsalgo.container.deque.doubly_linked_list_deque import (
    DoublyLinkedListDeque,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        que = DoublyLinkedListDeque[int]()
        que.append_right(1)
        self.assertEqual(len(que), 1)
        que.append_left(2)
        self.assertEqual(len(que), 2)
        self.assertEqual(que.pop_right(), 1)
        self.assertEqual(len(que), 1)
        self.assertEqual(que.pop_right(), 2)
        self.assertEqual(len(que), 0)
        with self.assertRaises(Exception):
            que.pop_left()


if __name__ == "__main__":
    unittest.main()
