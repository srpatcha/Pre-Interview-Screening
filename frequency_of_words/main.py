# main.py
import threading
from word_frequency import compute_word_frequency

def main():
    with open('subfolder/input.txt', 'r') as file:
        line = file.read()

    thread1 = threading.Thread(target=compute_word_frequency, args=(line,))
    thread1.start()
    thread1.join()

if __name__ == "__main__":
    main()
