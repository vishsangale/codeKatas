""" Implementation of singly linked list"""

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class SinglyLinkedList():
    def __init__(self):
        self.tail = None
        self.head = None

    def insert(self, previous, new):
        if not self.head:
            self.head = new
            self.tail = new
        elif not previous:
            new.next = self.head
            self.head = new
        elif previous == self.tail:
            self.tail.next = new
            self.tail = new
        else:
            temp = SinglyLinkedList()
            temp = previous.next
            previous.next = new
            new.next = temp


    def delete(self, node):
        pass

    def traverse(self):
        current = self.head
        while current:
            print current.data
            current = current.next


sll = SinglyLinkedList()
sll.insert(None, Node(4, None))
sll.insert(sll.tail, Node(5, None))
sll.insert(None, Node(6, None))
sll.insert(sll.head, Node(7, None))
sll.insert(sll.head.next, Node(9, None))
sll.traverse()
