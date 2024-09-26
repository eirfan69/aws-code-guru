import time
import threading

# Inefficient use of list where set would be better
def check_duplicates(arr):
    unique_items = []
    for item in arr:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

# Concurrency issue: improper use of locks
class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

def inefficient_threading_operation():
    counter = Counter()
    threads = []
    
    # Create multiple threads that increment the counter inefficiently
    for _ in range(1000):
        thread = threading.Thread(target=counter.increment)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Test inefficient duplicate check
    arr = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9]
    print(f"Unique items: {check_duplicates(arr)}")

    # Test inefficient threading
    start_time = time.time()
    inefficient_threading_operation()
    end_time = time.time()
    print(f"Inefficient threading took {end_time - start_time} seconds")
