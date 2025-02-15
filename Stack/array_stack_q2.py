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

def reverse_number(n):
    stack = Stack()
   
    n_str = str(n)
  
    for digit in n_str:
        stack.push(digit)
    
    reversed_number = ""
   
    while not stack.is_empty():
        reversed_number += stack.pop()
    
    return int(reversed_number)  


input_number = 12345
print("Original number:", input_number)
print("Reversed number:", reverse_number(input_number))

