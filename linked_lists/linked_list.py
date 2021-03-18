class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.root = None

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        current = self.root
        while current.next:
            current = current.next
        current.next = node

    def __str__(self):
        current = self.root
        while current:
            print(current.val, "->")
            current = current.next
