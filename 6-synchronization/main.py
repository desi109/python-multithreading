import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

# Synchronization example using mutex and ThreadPoolExecutor:

lock = threading.Lock()

def using_the_wc(lockWC, somebody):
    lockWC.acquire()
    print(f'WC is occupied by {somebody}!')
    start = time.perf_counter()
    time.sleep(random.randint(1, 5))
    end = time.perf_counter()
    print(f'{somebody} finished in {end - start} seconds')
    lockWC.release()

with ThreadPoolExecutor() as pool:
    people = ['Billy', 'Johny', 'Tony', 'Bobby']
    for someone in people:
        pool.submit(using_the_wc, lock, someone)

