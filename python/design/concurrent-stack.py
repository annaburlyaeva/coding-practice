# Implement concurrent stack


import threading
import time


class ConcurrentStack:
    def __init__(self):
        self.stack = []
        self.lock = threading.Lock()

    def push(self, item):
        with self.lock:
            self.stack.append(item)

    def pop(self):
        with self.lock:
            if self.stack:
                return self.stack.pop()
            else:
                return None


# Define a producer function that pushes items to the stack
def producer(stack):
    for i in range(5):
        item = f'item {i}'
        print(f'Pushing {item}')
        stack.push(item)
        time.sleep(1)  # Simulate work


# Define a consumer function that pops items from the stack
def consumer(stack):
    while True:
        item = stack.pop()
        if item is None:
            break
        print(f'Popping {item}')
        time.sleep(2)  # Simulate work


# Create a concurrent stack
cs = ConcurrentStack()

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(cs,))
consumer_thread = threading.Thread(target=consumer, args=(cs,))

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the producer to finish
producer_thread.join()

# Stop the consumer thread
consumer_thread.join()

print("All tasks completed.")
