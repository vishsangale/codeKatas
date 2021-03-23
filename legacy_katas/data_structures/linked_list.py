"""Implementation of Linked List data structure."""

import unittest


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def find(self, item):
        node = self.head
        while node:
            if node.value == item:
                return True
            node = node.next
        return False

    def remove(self, item):
        node = self.head
        prev = node

        while node:
            if node.value == item:
                if node.next and prev == node:
                    self.head = node.next
                    return True
                if not node.next and node != self.head:
                    prev.next = None
                    return True
                if not node.next and node == self.head:
                    self.head = None
                    return True

                prev.next = node.next
                return True
            node = node.next

        return False

    def __str__(self):
        str_val = ""
        node = self.head
        while node:
            str_val += str(node.value) + "-->"
            node = node.next
        return str_val


class TestLinkedListMethods(unittest.TestCase):
    def test_simple(self):
        ll = LinkedList()

        self.assertEqual(None, ll.head)

        ll.add(4)
        ll.add(3.14)
        ll.add("Pi")
        self.assertEqual("Pi", ll.head.value)

        self.assertEqual(False, ll.remove(8))
        self.assertEqual(True, ll.remove("Pi"))
        self.assertEqual(3.14, ll.head.value)

        self.assertEqual(False, ll.find("Pi"))
        self.assertEqual(True, ll.find(4))
        self.assertEqual(True, ll.remove(4))
        self.assertEqual(True, ll.remove(3.14))
        self.assertEqual(False, ll.remove(3.14))


if __name__ == "__main__":
    unittest.main()
