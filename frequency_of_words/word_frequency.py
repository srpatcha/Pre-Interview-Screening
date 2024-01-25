# word_frequency.py
from collections import Counter
import re

def compute_word_frequency(line):
    
    cleaned_line = re.sub(r'[^a-zA-Z0-9 ]', '', line.lower())
    words = cleaned_line.split()
    word_frequency = Counter(words)
    sorted_word_frequency = dict(sorted(word_frequency.items()))

    return sorted_word_frequency
