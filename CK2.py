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

    def delete(self, previous):
        if not previous:
            if not self.head:
                return
            elif self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif previous.next == self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = previous
                self.tail.next = None
        elif previous == self.tail:
            return
        else:
            previous.next = previous.next.next

    def traverse(self, head):
        current = head
        traversal = ''
        while current:
            traversal += str(current.data) + ' -> '
            current = current.next
        print traversal





