"""Implementation of binary search tree data structure."""

import unittest


class BinaryNode(object):
    def __init__(self, item, left=None, right=None):
        self.val = item
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        if not self.root:
            self.root = BinaryNode(item)
        else:
            self.add_helper(self.root, item)

    def add_helper(self, root, item):
        if root.val < item:
            if not root.right:
                root.right = BinaryNode(item)
            else:
                self.add_helper(root.right, item)
        else:
            if not root.left:
                root.left = BinaryNode(item)
            else:
                self.add_helper(root.left, item)

    def inorder(self):
        self.inorder_helper(self.root)
        print()

    def inorder_helper(self, root):
        if not root:
            return

        self.inorder_helper(root.left)
        print(root.val, end=",")
        self.inorder_helper(root.right)

    def preorder(self):
        self.preorder_helper(self.root)
        print()

    def preorder_helper(self, root):
        if not root:
            return

        print(root.val, end=",")
        self.preorder_helper(root.left)
        self.preorder_helper(root.right)

    def postorder(self):
        self.postorder_helper(self.root)
        print()

    def postorder_helper(self, root):
        if not root:
            return

        self.postorder_helper(root.left)
        self.postorder_helper(root.right)
        print(root.val, end=",")


class TestBinarySearchTreeMethods(unittest.TestCase):
    def test_simple(self):
        bst = BinarySearchTree()

        bst.add(5)
        bst.add(4)
        bst.add(6)
        bst.add(3)
        bst.add(7)
        bst.add(2)

        bst.inorder()
        bst.preorder()
        bst.postorder()


if __name__ == "__main__":
    unittest.main()
