# Implement an asynchronous channel (like the golang primitive one) that can
# be used for communicating between threads,
# such that all data sent will become available
# for receiving in the same order. Send should not block the thread it was
# called. Receive will block until the sent message is available,
# and the block should not waste CPU time on busy/spin wait.

from collections import deque
import threading


class AsyncChannel():
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)

    def send(self, message):
        self.queue.append(message)
        with self.lock:
            self.not_empty.notify()

    def receive(self):
        try:
            return self.queue.popleft()
        except IndexError:
            pass
        with self.lock:
            while not self.queue:
                self.not_empty.wait()
            return self.queue.popleft()


def sender(channel, messages):
    for msg in messages:
        print("Sent: " + msg)
        channel.send(msg)
    print("All Sent!")


def receiver(channel, num_messages):
    for _ in range(num_messages):
        msg = channel.receive()
        print("Received: " + msg)
    print("All Received!")


channel = AsyncChannel()
sender_1_thread = threading.Thread(target=sender,
                                   args=(channel, ["Hi", "This is Anna!"]))
sender_2_thread = threading.Thread(target=sender,
                                   args=(channel, ["Hi all!", "This is Bob!"]))
receiver_thread = threading.Thread(target=receiver, args=(channel, 4))

sender_1_thread.start()
sender_2_thread.start()
receiver_thread.start()

sender_1_thread.join()
sender_2_thread.join()
receiver_thread.join()




