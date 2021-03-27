from katas.graphs.graph import GraphNode
from katas.search.dfs import dfs


def test_dfs_search():
    src = None
    dst = None

    assert False == dfs(src, dst)

    dst = GraphNode(1)

    assert False == dfs(src, dst)

    assert True == dfs(dst, dst)

    src = GraphNode(2)

    assert False == dfs(src, dst)

    src.add_edge(dst)

    assert True == dfs(src, dst)
