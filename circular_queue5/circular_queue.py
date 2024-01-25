# circular_queue.py
class CircularQueue:
    def __init__(self, max_length):
        self.queue = {}
        self.max_length = max_length
        self.front = 0
        self.rear = 0

    def enqueue(self, element):
        if (self.rear + 1) % self.max_length == self.front:
            self.dequeue()

        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.max_length

    def dequeue(self):
        if self.front == self.rear:
            return None

        oldest_element = self.queue[self.front]
        del self.queue[self.front]
        self.front = (self.front + 1) % self.max_length

        return oldest_element

    def display(self):
        return list(self.queue.values())
