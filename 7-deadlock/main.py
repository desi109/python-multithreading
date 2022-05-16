from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import time
import random


class DiningPhilosophers:
    def __init__(self, number_of_phils, meals_to_eat):
        self.meals = [meals_to_eat for _ in range(number_of_phils)]
        self.chopsticks = [Lock() for _ in range(number_of_phils)]

    def serveMeals(self, current_philosopher):
        first_chopstick = current_philosopher
        second_chopstick = (current_philosopher + 1) % 5

 # яж докато има на масата
        while self.meals[current_philosopher] > 0:
            # thinking state
            time.sleep(random.random()*5)
            self.chopsticks[first_chopstick].acquire()
            time.sleep(random.random())

            if not self.chopsticks[second_chopstick].locked():
                self.chopsticks[second_chopstick].acquire()
                print(f'Philosopher {current_philosopher} starts eating...')
                # eating state
                time.sleep(random.random()*5)
                self.meals[current_philosopher] -= 1
                self.chopsticks[first_chopstick].release()
                self.chopsticks[second_chopstick].release()
                print(f'Philosopher {current_philosopher} stops eating. {self.meals[current_philosopher]} meal(s) left')
            else:
                self.chopsticks[first_chopstick].release()


def main():
    philosophers = [0, 1, 2, 3, 4]
    meals_to_eat = 2
    dining_philosophers = DiningPhilosophers(len(philosophers), meals_to_eat)

    with ThreadPoolExecutor(max_workers=5) as pool:
        for philosopher in philosophers:
            pool.submit(dining_philosophers.serveMeals, philosopher)


if __name__ == "__main__":
    main()

