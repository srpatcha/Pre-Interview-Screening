# test_word_frequency.py
import unittest
from word_frequency import compute_word_frequency

class TestWordFrequency(unittest.TestCase):
    def test_compute_word_frequency(self):
        line = "which is better python 2 or python 3"
        result = compute_word_frequency(line)
        expected_result = {'2': 1, '3': 1, 'better': 1, 'is': 1, 'or': 1, 'python': 2, 'which': 1}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
