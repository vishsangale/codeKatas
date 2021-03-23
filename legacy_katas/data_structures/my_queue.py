"""Implementation of queue data structure."""

import unittest


class Queue(object):
    def __init__(self):
        self._container = []

    def enqueue(self, item):
        self._container.append(item)

    def dequeue(self):
        if self._container:
            return self._container.pop(0)
        else:
            raise Exception("Exmpty Queue")

    def front(self):
        if self._container:
            return self._container[0]
        else:
            raise Exception("Empty Queue")


class TestQueueMethods(unittest.TestCase):
    def test_simple(self):
        queue = Queue()
        queue.enqueue(1)

        self.assertEqual(1, queue.dequeue())

        with self.assertRaises(Exception):
            queue.dequeue()

        with self.assertRaises(Exception):
            queue.front()

        queue.enqueue(3)
        self.assertEqual(3, queue.front())
        self.assertEqual(3, queue.dequeue())

        queue.enqueue("a")
        queue.enqueue(4)
        queue.enqueue(3.14)

        self.assertEqual("a", queue.dequeue())
        self.assertEqual(4, queue.dequeue())
        self.assertEqual(3.14, queue.dequeue())

        with self.assertRaises(Exception):
            queue.dequeue()


if __name__ == "__main__":
    unittest.main()
