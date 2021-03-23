import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

from katas.stacks.stack import Stack

class TreeNode(object):
    def __init__(self, _val) -> None:
        self.val = _val
        self.left = None
        self.right = None

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
