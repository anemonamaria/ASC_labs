
import sys
import random
import time
from threading import Thread, Semaphore


class Philosopher(Thread):
    def __init__(self, footman):
        Thread.__init__(self)
        self.footman = footman

    def set_right(self, fork):
        self.right_fork = fork

    def set_left(self, fork):
        self.left_fork = fork

    def get_forks(self):
        self.footman.acquire()
        self.right_fork.acquire()
        self.left_fork.acquire()

    def put_forks(self):
        self.right_fork.release()
        self.left_fork.release()
        self.footman.release()

    def run(self):
        iteration = 0
        while iteration < 20:
            time.sleep(random.uniform(0, 2))
            print("{} is hungry\n".format(self.name))

            self.get_forks()
            print("{} is eating\n".format(self.name))
            time.sleep(random.uniform(0, 1))

            self.put_forks()
            print("{} finished eating\n".format(self.name))

            iteration += 1

if __name__ == "__main__":
    num_philosophers = 5
    philosophers = []

    forks = [Semaphore(1) for i in range(num_philosophers)]

    footman = Semaphore(num_philosophers-1)

    for i in range(num_philosophers):
        philosophers.append(Philosopher(footman))
        philosophers[i].set_right(forks[i])
        philosophers[i].set_left(forks[(i+1) % num_philosophers])

    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()