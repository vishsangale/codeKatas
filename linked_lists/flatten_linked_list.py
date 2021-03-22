from linked_lists.linked_list import Node


def flatten_linked_list(ll):
    if not ll:
        return None

    current = ll
    flatten_list = None
    prev_node = None
    while current:
        current_vertical = current
        while current_vertical:
            new_node = Node(current_vertical.val)
            if not flatten_list:
                flatten_list = new_node
            else:
                prev_node.next = new_node
            prev_node = new_node
            current_vertical = current_vertical.next

        if hasattr(current, 'right'):
            current = current.right
        else:
            current = None
    return flatten_list


def test_flatten():
    a = Node(5)
    a.next = Node(7)
    a.next.next = Node(8)
    a.next.next.next = Node(30)

    b = Node(10)
    b.next = Node(20)

    c = Node(19)
    c.next = Node(22)
    c.next.next = Node(50)

    d = Node(28)
    d.next = Node(35)
    d.next.next = Node(40)
    d.next.next.next = Node(45)

    main_list = a
    main_list.right = b
    main_list.right.right = c
    main_list.right.right.right = d

    ll = flatten_linked_list(main_list)
    assert str(ll) == "5->7->8->30->10->20->19->22->50->28->35->40->45"
