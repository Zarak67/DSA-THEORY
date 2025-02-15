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

def get_minimum(queue):
    if queue.is_empty():
        return None
    min_val = float('inf')
    current = queue.front
    while current:
        if current.value < min_val:
            min_val = current.value
        current = current.next
    return min_val


queue = LinkedListQueue()
for i in range(10, 0, -1):
    queue.enqueue(i)

print("Minimum in the queue:", get_minimum(queue))  identify if these are using array and linked lists
