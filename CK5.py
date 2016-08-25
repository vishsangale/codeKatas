""" Check if singly linked list is a palindrome
    Time Complexity O(n)
    Space Complexity O(n)
    """
from CK2 import SinglyLinkedList, Node


def reverse(head):
    if not head:
        return None
    elif not head.next:
        return head
    prev = None
    current = head
    while (current):
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    head = prev
    return head


def compare(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next

    return True


def find_mid(head):
    p1 = head
    p2 = head
    while p2:
        p2 = p2.next
        if p2:
            p2 = p2.next
            p1 = p1.next
    return p1


def is_palindrome(sll):
    mid = find_mid(sll.head)
    head = reverse(mid)
    return compare(sll.head, head)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert(None, Node(4, None))
    sll.insert(sll.tail, Node(5, None))
    sll.insert(sll.tail, Node(3, None))
    sll.insert(sll.tail, Node(3, None))
    sll.insert(sll.tail, Node(5, None))
    sll.insert(sll.tail, Node(4, None))
    sll.traverse(sll.head)
    print is_palindrome(sll)
