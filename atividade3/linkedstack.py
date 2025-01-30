class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def isEmpty(self):
        return self.top is None
    
    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    
    def __len__(self):
        return self.size