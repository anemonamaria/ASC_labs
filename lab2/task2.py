"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""
import sys
import threading
from threading import Thread
from random import randint

def helloThread(nr, randNr):
    print("Hello, I'm Thread ", nr,
          " and I received the number ", randNr)

if __name__ == "__main__":

    threads = []

    nr = input("How many threads do you want?\n")

    for i in range(int(nr)):
        thread = Thread(target=helloThread, args=(i, randint(0, 100)))
        thread.start()
        threads.append(thread)

    for i in range(len(threads)):
        threads[i].join()