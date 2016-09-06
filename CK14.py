from Queue import Queue


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_traversal(root):
    if not root:
        return
    q = Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        if current.left:
            q.put(current.left)
        if current.right:
            q.put(current.right)
        print current.data


class BST():
    def __init__(self):
        self.root = None

    def insert(self, root, item):
        if not self.root:
            self.root = Node(item)
        elif not root:
            return
        elif item < root.data:
            if root.left:
                self.insert(root.left, item)
            else:
                root.left = Node(item)
        elif root.right:
            self.insert(root.right, item)
        else:
            root.right = Node(item)



