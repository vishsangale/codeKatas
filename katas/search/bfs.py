"""Implementation of Breadth First Search."""

from katas.graphs.graph import GraphNode

def bfs(src: GraphNode, dst: GraphNode) -> bool:
    """Return true if the src and dst are connected else false"""
    visited = set()
    next_to_visit = Stack()
    next_to_visit.push(src)

    while not next_to_visit.is_empty():
        node = next_to_voisit.pop()
        if node == dst:
            return True
        visited.add(node)
        childs = node.get_childs()
        for child in childs:
            next_to_visit.add(child)

    return False

