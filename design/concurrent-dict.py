# Implement concurrent dictionary

import threading
import time


class ConcurrentDictionary:
    def __init__(self):
        self.dictionary = {}
        self.lock = threading.Lock()

    def set(self, key, value):
        with self.lock:
            self.dictionary[key] = value

    def get(self, key):
        with self.lock:
            return self.dictionary.get(key)

    def delete(self, key):
        with self.lock:
            if key in self.dictionary:
                del self.dictionary[key]


# Define a function that updates the dictionary
def update_dict(dictionary):
    for i in range(5):
        dictionary.set(i, f'value {i}')
        print(f'Setting key {i} to value {i}')
        time.sleep(1)  # Simulate work


# Define a function that reads from the dictionary
def read_dict(dictionary):
    for i in range(5):
        value = dictionary.get(i)
        print(f'Reading key {i}, value: {value}')
        time.sleep(2)  # Simulate work


# Create a concurrent dictionary
cd = ConcurrentDictionary()

# Create threads for updating and reading the dictionary
update_thread = threading.Thread(target=update_dict, args=(cd,))
read_thread = threading.Thread(target=read_dict, args=(cd,))

# Start the threads
update_thread.start()
read_thread.start()

# Wait for the threads to finish
update_thread.join()
read_thread.join()

print("All tasks completed.")
