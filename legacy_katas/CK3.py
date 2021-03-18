

class BinaryMinHeap():
    def __init__(self):
        self.heap = []

    def get_minimum(self):
        return self.heap[0]

    def get_heap_size(self):
        return len(self.heap)

    def is_empty(self):
        if self.heap:
            return True
        else:
            return False

    def get_left_child(self, node_index):
        return self.heap[2*node_index + 1]

    def get_right_child(self, node_index):
        return self.heap[2 * node_index + 2]

    def get_parent(self, child_index):
        return self.heap[(child_index - 1)/2]

    def insert(self, element):
        pass

heap  = BinaryMinHeap()
print heap.is_empty()