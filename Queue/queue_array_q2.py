class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = self.rear = -1
        self.size = size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.size
        print(self.queue[self.rear])

queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.display()
queue.dequeue()
queue.display()
queue.enqueue(6)
queue.display()
