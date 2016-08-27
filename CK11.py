""" Remove duplicates from unsorted linked lists
"""

from CK2 import SinglyLinkedList, Node

unique = dict()
""" Time complexity O(n)
    Space complexity O(n)
"""


def remove_duplicates(head):
    if not head:
        return
    current = head
    prev = None
    while current:
        if current.data in unique:
            prev.next = current.next
        else:
            unique[current.data] = 1
            prev = current
        current = current.next
    return head


""" Time complexity O(n^2)
    Space complexity O(1)
"""


def remove_duplicates_without_buffer(head):
    if not head or not head.next:
        return
    i = head
    prev = None
    while i:
        j = i
        while j:
            if i != j and i.data == j.data:
                prev.next = j.next
            else:
                prev = j
            j = j.next
        i = i.next
    return head


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert(None, Node(1, None))
    sll.insert(sll.tail, Node(2, None))
    sll.insert(sll.tail, Node(3, None))
    sll.insert(sll.tail, Node(4, None))
    sll.insert(sll.tail, Node(5, None))
    sll.insert(sll.tail, Node(1, None))
    sll.traverse(sll.head)
    # head = remove_duplicates(sll.head)
    head = remove_duplicates_without_buffer(sll.head)
    sll.traverse(head)
