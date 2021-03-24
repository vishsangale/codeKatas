"""Implementation of Breadth First Search."""

from katas.graphs.graph import GraphNode
from katas.stacks.stack import Stack


def bfs(src: GraphNode, dst: GraphNode) -> bool:
    """Return true if the src and dst are connected else false"""
    if not src or not dst:
        return False
    visited = set()
    next_to_visit = Stack()
    next_to_visit.push(src)

    while not next_to_visit.is_empty():
        node = next_to_visit.pop()
        if node == dst:
            return True
        visited.add(node)
        childs = node.get_childs()
        for child in childs:
            next_to_visit.push(child)

    return False

