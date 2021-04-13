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


def test_ordering_operations(capfd):
    t = BST()
    t.add(3)
    t.add(2)
    t.add(1)
    t.add(5)
    t.add(4)
    t.add(6)
    t.inorder()
    out, err = capfd.readouterr()
    assert out == "1\n2\n3\n4\n5\n6\n"

    t.preorder()
    out, err = capfd.readouterr()
    assert out == "3\n2\n1\n5\n4\n6\n"

    t.postorder()
    out, err = capfd.readouterr()
    assert out == "1\n2\n4\n6\n5\n3\n"


def test_remove_node(capfd):
    t = BST()
    t.add(3)
    t.add(2)
    t.add(1)
    t.add(5)
    t.add(4)
    t.add(6)

    t.remove(5)
    t.inorder()
    out, err = capfd.readouterr()
    assert out == "1\n2\n3\n4\n6\n"

    t.remove(6)
    t.inorder()
    out, err = capfd.readouterr()
    assert out == "1\n2\n3\n4\n"

    t.remove(5)
    t.inorder()
    out, err = capfd.readouterr()
    assert out == "1\n2\n3\n4\n"

    t.remove(3)
    t.inorder()
    out, err = capfd.readouterr()
    assert out == "1\n2\n4\n"

