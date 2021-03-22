class Stack(object):
    def __init__(self) -> None:
        self.top = None
        self.items = []

    def push(self, val: object) -> None:
        self.items.append(val)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        str_val = ""
        for item in self.items:
            str_val += f"{item}<-"
        str_val = str_val[:-2]
        return str_val

    def pop(self) -> object:
        if not self.items:
            raise IndexError("Stack is empty, cannot pop item")
        return self.items.pop(-1)

    def peak(self) -> object:
        if not self.items:
            raise IndexError("Stack is empty, cannot pop item")
        return self.items[-1]
