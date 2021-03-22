class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.right = None

    def __repr__(self):
        str_val = ""
        current = self
        while current:
            str_val += str(current.val) + "->"
            current = current.next
        str_val = str_val[:-2]
        return str_val
