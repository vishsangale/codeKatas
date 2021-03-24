import pytest

from katas.trees.bst import BST

def test_basic_operations():
    t = BST()
    t.add(3)
    t.add(2)
    t.add(1)
    t.add(5)
    t.add(4)
    t.add(6)
    t.visualize()

    assert 6 == len(t)
