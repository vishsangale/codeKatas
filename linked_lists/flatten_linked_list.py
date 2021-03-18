from linked_lists.linked_list import LinkedList


def flatten_linked_list(ll):
    if not ll:
        return None
    flatten_list = LinkedList()
    current = ll
    while current:
        current_vertical = current.root
        while current_vertical:
            flatten_list.add(current_vertical.val)
            current_vertical = current_vertical.next
        if hasattr(current, 'right'):
            current = current.right
        else:
            current = None
    return flatten_list


def test_flatten():
    a = LinkedList()
    a.add(5)
    a.add(7)
    a.add(8)
    a.add(30)

    b = LinkedList()
    b.add(10)
    b.add(20)

    c = LinkedList()
    c.add(19)
    c.add(22)
    c.add(50)

    d = LinkedList()
    d.add(28)
    d.add(35)
    d.add(40)
    d.add(45)

    main_list = LinkedList()
    main_list.root = a
    main_list.root.right = b
    main_list.root.right.right = c
    main_list.root.right.right.right = d

    ll = flatten_linked_list(main_list.root)
    assert str(ll) == "5->7->8->30->10->20->19->22->50->28->35->40->45"
