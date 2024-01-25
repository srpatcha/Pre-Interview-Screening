# test_circular_queue.py
import unittest
from circular_queue import CircularQueue

class TestCircularQueue(unittest.TestCase):
    def test_circular_queue_operations(self):
        cq = CircularQueue(5)

        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        cq.enqueue(4)
        cq.enqueue(5)
        result = cq.display()
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected_result)

        cq.enqueue(6)
        result = cq.display()
        expected_result = [2, 3, 4, 5, 6]
        self.assertEqual(result, expected_result)

        oldest_element = cq.dequeue()
        self.assertEqual(oldest_element, 2)

        cq.enqueue(7)
        result = cq.display()
        expected_result = [3, 4, 5, 6, 7]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()