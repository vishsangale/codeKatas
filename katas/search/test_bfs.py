from katas.graphs.graph import GraphNode
from katas.search.bfs import bfs

def test_bfs_search():
    src = None
    dst = None

    assert False == bfs(src, dst)

    dst = GraphNode(1)

    assert False == bfs(src, dst)

    assert True == bfs(dst, dst)

    src = GraphNode(2)

    assert False == bfs(src, dst)

    src.add_edge(dst)

    assert True == bfs(src, dst)
