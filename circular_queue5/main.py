# main.py
import threading
from circular_queue import CircularQueue

def main():
    with open('subfolder/input.txt', 'r') as file:
        max_length = int(file.read().strip())

    thread1 = threading.Thread(target=perform_circular_queue_operations, args=(max_length,))
    thread1.start()
    thread1.join()

def perform_circular_queue_operations(max_length):
    cq = CircularQueue(max_length)

    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    result = cq.display()
    print(f"Initial Queue: {result}")

    cq.enqueue(6)
    result = cq.display()
    print(f"After Enqueue(6): {result}")

    oldest_element = cq.dequeue()
    print(f"Dequeued Element: {oldest_element}")

    cq.enqueue(7)
    result = cq.display()
    print(f"After Enqueue(7): {result}")

if __name__ == "__main__":
    main()