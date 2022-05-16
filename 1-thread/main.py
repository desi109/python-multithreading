# The simplest way to use a Thread is to instantiate it with
# a target function and call start() to let it begin working.

import threading
import time

from threading import Thread


def work(seconds):
    time.sleep(seconds)
    # thread worker function
    print('...' + threading.current_thread().getName() + ' is working...')


# Extending Thread class
class MyThread(Thread):
    start_seconds = 0

    # default constructor
    def __init__(self, start_seconds):
        threading.Thread.__init__(self, name=name)
        self.start_seconds = start_seconds

    # Target function for thread
    def run(self):
        time.sleep(self.start_seconds)
        print('...' + threading.current_thread().getName() + ' is working...')


if __name__ == "__main__":
    counter_seconds = 5
    print('Start the threads after ' + str(counter_seconds) + ' seconds ...')
    thread_1 = threading.Thread(target=work, args=(counter_seconds,), name="Thread-1")

    # Create a Thread without using an Explicit function:
    thread_2 = Thread(target=work, args=(counter_seconds,), name="Thread-2")

    # Create Thread by extending Thread Class -> creating object of the class MyThread
    myThread = MyThread(Thread(name="My-Thread"), counter_seconds)

    thread_1.start()
    thread_2.start()
    myThread.start()

    for x in range(1, 6):
        # sleep the main thread while counting from 1 to 5
        time.sleep(0.9)
        print('Main thread is counting: ' + str(x))
