class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.right = None


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

    def __repr__(self):
        str_val = ""
        current = self.root
        while current:
            str_val += str(current.val) + "->"
            current = current.next
        str_val = str_val[:-2]
        return str_val
