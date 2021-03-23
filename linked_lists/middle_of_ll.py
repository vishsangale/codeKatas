"""Find the middle of a given linked list"""
from linked_lists.linked_list import Node


def get_middle_of_ll(ll):
    if ll is None:
        return None
    current = ll
    length = 0
    while current:
        length += 1
        current = current.next
    mid = length // 2
    current = ll
    while mid:
        current = current.next
        mid -= 1
    return current.val


def test_empty_list():
    assert get_middle_of_ll(None) is None


def test_single_element_list():
    ll = Node(13)
    assert get_middle_of_ll(ll) == 13


def test_two_element_list():
    ll = Node(13)
    ll.next = Node(15)
    assert get_middle_of_ll(ll) == 15


def test_odd_num_elements_list():
    ll = Node(13)
    ll.next = Node(15)
    ll.next.next = Node(17)
    ll.next.next.next = Node(19)
    ll.next.next.next = Node(21)
    assert get_middle_of_ll(ll) == 17


def test_even_num_elements_list():
    ll = Node(13)
    ll.next = Node(15)
    ll.next.next = Node(17)
    ll.next.next.next = Node(19)
    ll.next.next.next.next = Node(21)
    ll.next.next.next.next.next = Node(23)
    assert get_middle_of_ll(ll) == 19
