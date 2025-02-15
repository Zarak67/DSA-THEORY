class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
      
class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.value

    def display(self):
        temp = self.front
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_first_k_elements(queue, k):
    if queue.is_empty() or k <= 0:
        return
    stack = []

    for _ in range(k):
        if queue.is_empty():
            return 
        stack.append(queue.dequeue())
    

    while stack:
        queue.enqueue(stack.pop())
    

    size = 0
    current = queue.front
    while current:
        size += 1
        current = current.next
    
    for _ in range(size - k):
        queue.enqueue(queue.dequeue())


queue = LinkedListQueue()
for i in range(1, 11):
    queue.enqueue(i)

print("Original queue:")
queue.display()

reverse_first_k_elements(queue, 5)
print("Queue after reversing the first 5 elements:")
queue.display()


