"""Implementation of stack data structure."""

import unittest


class Stack(object):
    def __init__(self):
        self._container = []

    def push(self, item):
        self._container.append(item)

    def pop(self):
        if self._container:
            return self._container.pop()
        else:
            raise Exception("Empty Stack")

    def peak(self):
        if self._container:
            return self._container[-1]
        else:
            raise Exception("Empty Stack")


class TestStackMethods(unittest.TestCase):
    def test_simple_push_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.pop())
        with self.assertRaises(Exception):
            stack.pop()
        with self.assertRaises(Exception):
            stack.peak()

        stack.push(2)
        self.assertEqual(2, stack.peak())
        self.assertEqual(2, stack.pop())

        stack.push(3)
        stack.push("a")
        stack.push(4.5)

        self.assertEqual(4.5, stack.pop())
        self.assertEqual("a", stack.pop())
        self.assertEqual(3, stack.pop())


if __name__ == "__main__":
    unittest.main()
