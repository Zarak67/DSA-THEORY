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

def search_stack(stack, element):
    temp_stack = Stack()
    index = -1
    current_index = 0
   
    while not stack.is_empty():
        top_element = stack.pop()
        temp_stack.push(top_element)
        if top_element == element:
            index = current_index
            break
        current_index += 1
 
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return index


stack = Stack()
for i in range(10):
    stack.push(i)
search_element = 5
print("Index of element", search_element, ":", search_stack(stack, search_element))
