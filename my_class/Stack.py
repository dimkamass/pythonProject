class Stack:
    def __init__(self):
        self.my_stack = []

    def push(self, item):
        self.my_stack.append(item)

    def pop(self):
        self.my_stack.pop()

    def peek(self):
        if len(self.my_stack) > 0:
            return self.my_stack[-1]
        else:
            print('Empty stack')
            return None

    def is_empty(self):
        return len(self.my_stack) == 0

    def size(self):
        return len(self.my_stack)
