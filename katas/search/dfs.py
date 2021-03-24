"""Depth First Search Implementation"""

from katas.graphs.graph import GraphNode


def _dfs(src: GraphNode, dst: GraphNode, visited: set) -> bool:
    if src in visited:
        return False

    if src == dst:
        return True

    visited.add(src)

    for node in src.get_childs():
        if node == dst:
            return True
        if _dfs(node, dst, visited):
            return True
    return False



def dfs(src: GraphNode, dst: GraphNode) -> bool:
    if not src or not dst:
        return False

    visited = set()

    return _dfs(src, dst, visited)

