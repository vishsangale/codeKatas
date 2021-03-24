
class GraphNode(object):
    def __init__(self, _val):
        self.val = _val
        self.children = set()

    def add_edge(self, node):
        self.children.add(node)

    def remove_edge(self, node):
        if node in self.children:
            self.children.remove(node)

    def get_childs(self):
        return self.children


