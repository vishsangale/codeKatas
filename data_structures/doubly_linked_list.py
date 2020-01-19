"""Implementation of doubly linked list."""

import unittest


class DoublyLLNode(object):
    def __init__(self, item, next=None, prev=None):
        self.val = item
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def find(self, item):
        node = self.head
        while node:
            if node.val == item:
                return True
            node = node.next
        return False

    def add(self, item):
        if not self.head:
            self.head = DoublyLLNode(item)
        else:
            node = DoublyLLNode(item)
            self.head.prev = node
            node.next = self.head
            self.head = node

    def remove(self, item):
        node = self.head
        prev = node
        while node:
            if node.val == item:
                if not node.next and node.prev:
                    prev.next = None
                    return True
                if not node.next and not node.prev:
                    self.head = None
                    return True
                if not node.prev:
                    self.head = self.head.next
                    self.head.prev = None
                    return True
                prev.next = node.next
                node.next.prev = prev
                return True
            prev = node
            node = node.next
        return False

    def __str__(self):
        str_val = ''
        node = self.head
        while node:
            str_val += str(node.val) + '<-->'
            node = node.next
        str_val += 'None'
        return str_val

class TestDoublyLinkedListMethods(unittest.TestCase):
    def test_simple(self):
        ll = DoublyLinkedList()

        self.assertEqual(None, ll.head)

        ll.add(4)

        self.assertEqual(True, ll.find(4))

        ll.add(5)
        ll.add('Pi')
        ll.add(3.14)
        ll.add('omega')
        print(ll)

        self.assertEqual(False, ll.remove('Omega'))
        self.assertEqual(True, ll.remove('omega'))

        self.assertEqual(3.14, ll.head.val)
        ll.remove(4)
        print(ll)


if __name__ == '__main__':
    unittest.main()
