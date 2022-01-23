import unittest

from dsalgo.container.queue.singly_linked_list_queue import (
    SinglyLinkedListQueue,
)


class Test(unittest.TestCase):
    def test(self) -> None:
        que = SinglyLinkedListQueue[int]()
        que.append(1)
        self.assertEqual(len(que), 1)
        self.assertEqual(que.pop(), 1)
        self.assertEqual(len(que), 0)
        with self.assertRaises(Exception):
            que.pop()


if __name__ == "__main__":
    unittest.main()
