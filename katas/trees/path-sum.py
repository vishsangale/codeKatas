"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

from katas.trees.tree import TreeNode


def has_path_sum(root: TreeNode, target_sum: int) -> bool:

    if not root:
        return False

    current_sum = 0
    return _has_path_sum(root, current_sum, target_sum)


def _has_path_sum(root: TreeNode, current_sum: int, target_sum: int) -> bool:

    if not root and current_sum == target_sum:
        return True

    current_sum += root.val
    if not root.left and not root.right and current_sum == target_sum:
        return True
    if root.left and _has_path_sum(root.left, current_sum, target_sum):
        return True
    if root.right and _has_path_sum(root.right, current_sum, target_sum):
        return True
    return False


def test_has_path_sum():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    assert has_path_sum(root, 22)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    assert not has_path_sum(root, 5)

    root = TreeNode(1)

    assert has_path_sum(root, 1)
