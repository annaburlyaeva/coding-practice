# Implement concurrent queue

import threading
import time


class ConcurrentQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.empty = threading.Condition(self.lock)

    def put(self, item):
        with self.lock:
            self.queue.append(item)
            # Notify any waiting threads that the queue is not empty
            self.empty.notify()

    def get(self):
        with self.lock:
            while not self.queue:  # Wait if the queue is empty
                self.empty.wait()
            return self.queue.pop(0)


# Define a producer function that adds items to the queue
def producer(queue):
    for i in range(5):
        item = f'item {i}'
        print(f'Producing {item}')
        queue.put(item)
        time.sleep(1)  # Simulate work


# Define a consumer function that processes items from the queue
def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f'Consuming {item}')
        time.sleep(2)  # Simulate work


# Create a concurrent queue
cq = ConcurrentQueue()

# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(cq,))
consumer_thread = threading.Thread(target=consumer, args=(cq,))

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the producer to finish
producer_thread.join()

# Stop the consumer thread
cq.put(None)
consumer_thread.join()

print("All tasks completed.")
