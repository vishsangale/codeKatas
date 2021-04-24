class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def _collect_level_nodes(node, level_map, depth=0):
    if not node:
        return

    if depth not in level_map:
        level_map[depth] = (0, 0)

    count, val = level_map[depth]
    count += 1
    val += node.val
    level_map[depth] = (count, val)

    _collect_level_nodes(node.left, level_map, depth + 1)
    _collect_level_nodes(node.right, level_map, depth + 1)


def calc_level_mean(node):
    level_map = dict()

    _collect_level_nodes(node, level_map, 0)

    out = [0] * len(level_map)

    for i in range(len(level_map)):
        out[i] = level_map[i][1] / level_map[i][0]

    return out


def test_get_average():
    r = Node(4)
    r.left = Node(7)
    r.right = Node(9)

    r.left.left = Node(10)
    r.left.right = Node(2)
    r.right.left = Node(6)

    r.left.right.right = Node(6)
    r.left.right.right.left = Node(2)

    out = calc_level_mean(r)
    print(out)
    assert [4, 8, 6, 6, 2] == out
