"""Find the middle of a given linked list"""
from linked_lists.linked_list import LinkedList


def get_middle_of_ll(ll):
    if ll is None:
        return None
    current = ll
    length = 0
    while current:
        length += 1
        current = current.next
    mid = (length // 2)
    current = ll
    while mid:
        current = current.next
        mid -= 1
    return current.val


def test_empty_list():
    assert get_middle_of_ll(None) is None


def test_single_element_list():
    ll = LinkedList()
    ll.add(13)
    assert get_middle_of_ll(ll.root) == 13


def test_two_element_list():
    ll = LinkedList()
    ll.add(13)
    ll.add(15)
    assert get_middle_of_ll(ll.root) == 15


def test_odd_num_elements_list():
    ll = LinkedList()
    ll.add(13)
    ll.add(15)
    ll.add(17)
    ll.add(19)
    ll.add(21)
    assert get_middle_of_ll(ll.root) == 17


def test_even_num_elements_list():
    ll = LinkedList()
    ll.add(13)
    ll.add(15)
    ll.add(17)
    ll.add(19)
    ll.add(21)
    ll.add(23)
    assert get_middle_of_ll(ll.root) == 19
