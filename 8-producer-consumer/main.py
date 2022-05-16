import random
from threading import Thread
from queue import Queue
import time


def produce_work(buffer, finished, max_capacity):
    finished.put(False)
    for position in range(max_capacity):
        value = random.randint(1, 100)
        buffer.put(value)
        print(f'producing {value} in position {position}')
    finished.put(True)


def consume_work(buffer, finished):
    position = 0
    while True:
        if buffer.empty():
            print('No items to consume')
            if finished.get() is True:
                break
            continue

        value = buffer.get()
        print(f'Consuming {value} from position {position}')
        position += 1


def main():
    max_capacity = 20
    buffer = Queue()
    finished = Queue()

    producer = Thread(target=produce_work, args=[buffer, finished, max_capacity])
    consumer = Thread(target=consume_work, args=[buffer, finished])

    producer.start()
    consumer.start()

    producer.join()
    print('Producer finished')

    consumer.join()
    print('Consumer finished')


if __name__ == "__main__":
    main()


