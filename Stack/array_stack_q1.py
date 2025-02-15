class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

def reverse_string(s):
    stack = Stack()
  
    for char in s:
        stack.push(char)
    
    reversed_string = ""
   
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string


input_string = "hello"
print("Original string:", input_string)
print("Reversed string:", reverse_string(input_string))


