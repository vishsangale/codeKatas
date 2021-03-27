class Queue(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        str_val = ""
        for item in self.items:
            str_val += f"{item}<-"
        str_val = str_val[:-2]
        return str_val

    def enqueue(self, val):
        """Enqueue element to the end of the queue"""
        self.items.append(val)

    def peek(self) -> object:
        """Retrieve element at the head of the queue"""
        if not self.items:
            raise IndexError("Queue is empty, cannot peek item")
        return self.items[0]

    def dequeue(self) -> object:
        """Retrieve and remove element at the head of the queue"""
        if not self.items:
            raise IndexError("Queue is empty, cannot dequeue item")
        return self.items.pop(0)
