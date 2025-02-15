class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.rear == self.size:
            print("Queue is full")
        else:
            self.queue[self.rear] = item
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            item = self.queue[self.front]
            self.front += 1
            return item

    def display(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear):
                print(self.queue[i], end=" ")
            print()

queue = Queue(5)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.display()
queue.dequeue()
queue.display()
