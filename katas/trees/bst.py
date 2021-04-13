import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

from katas.stacks.stack import Stack
from katas.trees.tree import TreeNode


class BST(object):
    def __init__(self):
        self.root = None

    def __len__(self):
        """Number of elements in the tree"""
        nr_elements = 0
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            nr_elements += 1
            if node.left:
                s.push(node.left)
            if node.right:
                s.push(node.right)
        return nr_elements

    def add(self, _val):
        node = TreeNode(_val)

        if not self.root:
            self.root = node
            return
        self._add(self.root, node)

    def _add(self, root, node):

        if not root:
            root = node
            return

        if root.val > node.val and root.left:
            self._add(root.left, node)
        elif root.val > node.val:
            root.left = node
        elif root.val <= node.val and root.right:
            self._add(root.right, node)
        else:
            root.right = node

    def _create_nx_tree(self, root, g):
        if not root:
            return
        if root.left:
            g.add_edge(root.val, root.left.val)
            self._create_nx_tree(root.left, g)
        if root.right:
            g.add_edge(root.val, root.right.val)
            self._create_nx_tree(root.right, g)

    def create_nx_tree(self):
        g = nx.Graph()
        if not self.root:
            return g
        self._create_nx_tree(self.root, g)
        return g

    def visualize(self):
        g = self.create_nx_tree()
        pos = graphviz_layout(g, prog="dot")
        nx.draw(g, pos, with_labels=True)
        plt.savefig("tree.png")

    def _preorder(self, node):
        if not node:
            return

        print(node.val)
        self._preorder(node.left)
        self._preorder(node.right)

    def preorder(self):
        """Preorder traversal of the BST"""
        self._preorder(self.root)

    def _inorder(self, node):
        if not node:
            return

        self._inorder(node.left)
        print(node.val)
        self._inorder(node.right)

    def inorder(self):
        """Inorder traversal of the BST"""
        self._inorder(self.root)

    def _postorder(self, node):
        if not node:
            return

        self._postorder(node.left)
        self._postorder(node.right)
        print(node.val)

    def postorder(self):
        """Postorder traversal of the BST"""
        self._postorder(self.root)

    def find_min(self, root):
        node = root
        min_val = node.val
        while node:
            min_val = node.val
            node = node.left

        return min_val

    def _remove(self, root, key):
        if not root:
            return root

        if not root.left and not root.right and root.val == key:
            return None

        if not root.left and root.right and root.val == key:
            return root.right

        if root.left and not root.right and root.val == key:
            return root.left

        if root.val == key:
            min_val = self.find_min(root.right)
            root.val = min_val
            root.right = self._remove(root.right, min_val)
        else:
            if root.val > key:
                root.left = self._remove(root.left, key)
            else:
                root.right = self._remove(root.right, key)

        return root

    def remove(self, key):
        self.root = self._remove(self.root, key)
