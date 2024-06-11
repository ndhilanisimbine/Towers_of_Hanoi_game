class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def get_name(self):
        return self.name

    def get_size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def print_items(self):
        print(f"{self.name} Stack: {self.items}")
