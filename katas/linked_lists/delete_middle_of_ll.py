from linked_lists.linked_list import Node


def delete_middle_ll(ll):
    if not ll or not ll.next:
        return None
    length = 0
    current = ll
    while current:
        length += 1
        current = current.next
    mid = length // 2
    if mid == 0:
        return None
    current = ll
    while mid > 1:
        current = current.next
        mid -= 1
    current.next = current.next.next
    return ll


def test_delete_middle_ll_empty_list():
    assert delete_middle_ll(None) is None


def test_delete_middle_ll_single_node():
    ll = Node(15)
    assert delete_middle_ll(ll) is None


def test_delete_middle_ll_two_nodes():
    ll = Node(15)
    ll.next = Node(17)
    assert str(delete_middle_ll(ll)) == "15"


def test_delete_middle_ll_odd_nodes():
    ll = Node(15)
    ll.next = Node(17)
    ll.next.next = Node(19)
    ll.next.next.next = Node(21)
    ll.next.next.next.next = Node(23)
    assert str(delete_middle_ll(ll)) == "15->17->21->23"


def test_delete_middle_ll_even_nodes():
    ll = Node(15)
    ll.next = Node(17)
    ll.next.next = Node(19)
    ll.next.next.next = Node(21)
    ll.next.next.next.next = Node(23)
    ll.next.next.next.next.next = Node(25)
    assert str(delete_middle_ll(ll)) == "15->17->19->23->25"
