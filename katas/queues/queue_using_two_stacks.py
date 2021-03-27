"""Build a queue using two stacks"""

from katas.stacks.stack import Stack

class QueueFromStacks(object):
    def __init__(self) -> None:
        self.old_stack = Stack() # store oldest elements
        self.new_stack = Stack() # store newest elements

    def __len__(self)-> int:
        return len(self.old_stack) + len(self.new_stack)

    def enqueue(self, _val:object)->None:
        self.new_stack.push(_val)

    def _move_elements(self):
        # move from new stack to old stack
        while not self.new_stack.is_empty():
            self.old_stack.push(self.new_stack.pop())

    def dequeue(self)->object:
        if self.old_stack.is_empty():
            self._move_elements()
        return self.old_stack.pop()

    def peek(self)->object:
        if self.old_stack.is_empty():
            self._move_elements()
        return self.old_stack.peek()

