from Queue import Queue
from sys import maxint

from numpy import inf

from CK14 import BST, level_traversal


def in_order_traversal(root):
    if not root:
        return
    current = root
    s = []
    while True:
        if current:
            s.append(current)
            current = current.left
        elif len(s) > 0:
            current = s.pop()
            print current.data
            current = current.right
        else:
            break


def is_balanced(root):
    if root is None:
        return True
    else:
        return (
            (abs(find_height(root.left) - find_height(root.right)) < 2)
            and is_balanced(root.right)
            and is_balanced(root.left)
        )


def find_height(root):
    if not root:
        return 0
    return 1 + max(find_height(root.left), find_height(root.right))


if __name__ == "__main__":
    t = BST()
    t.insert(t.root, 12)
    t.insert(t.root, 10)
    t.insert(t.root, 14)
    t.insert(t.root, 9)
    t.insert(t.root, 11)
    t.insert(t.root, 13)
    t.insert(t.root, 15)
    t.insert(t.root, 6)
    t.insert(t.root, 4)
    in_order_traversal(t.root)
