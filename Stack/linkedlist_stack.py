class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack elements:", stack.display())
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Stack elements after pop:", stack.display())
print("Is stack empty?", stack.is_empty())
