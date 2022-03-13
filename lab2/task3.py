"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""

from threading import Semaphore, Thread
from random import  choice

class Coffee:
    """ Base class """
    def __init__(self, coffee, size):
        self.coffee = coffee
        self.size = size

    def get_name(self):
        """ Returns the coffee name """
        return self.coffee

    def get_size(self):
        """ Returns the coffee size """
        return self.size

class ExampleCoffee:
    """ Espresso implementation """
    def __init__(self, size):
        pass

    def get_message(self):
        """ Output message """
        raise NotImplementedError

class AmericanoCoffee(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self, "Americano", size)

    def get_message(self):
        """ Output message """
        return "You've got your " + self.get_name() + " size:" + self.get_size()

class CappuccinoCoffee(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self, "Cappuccino", size)

    def get_message(self):
        """ Output message """
        return "You've got your " + self.get_name() + " size:" + self.get_size()

class EspressoCoffee(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self, "Espresso", size)

    def get_message(self):
        """ Output message """
        return "You've got your " + self.get_name() + " size:" + self.get_size()

TYPES = [EspressoCoffee, AmericanoCoffee, CappuccinoCoffee]
SIZES = ['s', 'l', 'xxl']

class Distributor:
    def __init__(self, n):
        self.full = n
        self.arr = []
        self.sem_producer = Semaphore(self.full)
        self.sem_consumer = Semaphore(0)

    def produce(self, coffee, name, nr):
        self.sem_producer.acquire()
        self.arr.append(coffee)
        print(name, nr, 'produced', coffee.get_message())
        self.sem_consumer.release()

    def consume(self, name, nr):
        self.sem_consumer.acquire()
        print(name, nr, 'consumed', self.arr.pop().get_name())
        self.sem_producer.release()


class CoffeeFactory:
    def __init__(self, name, nr, distributor):
        self.name = name
        self.nr = nr
        self.distributor = distributor

    def process(self):
        while True:
            coffee_type = choice(TYPES)
            self.distributor.produce(coffee_type(choice(SIZES)), self.name, self.nr)

class User:
    def __init__(self, name, nr, distributor):
        self.name = name
        self.nr = nr
        self.distributor = distributor

    def process(self):
        while True:
            self.distributor.consume(self.name, self.nr)

if __name__ == '__main__':
    nr_producers = 5
    nr_consumers = 9
    distributor = Distributor(nr_producers)
    threads = []

    for i in range(nr_producers):
        p = CoffeeFactory('Factory', i, distributor)
        threads.append((Thread(target=p.process)))

    for i in range(nr_consumers):
        c = User('Consumer', i, distributor)
        threads.append((Thread(target=c.process)))

    for i in threads:
        i.start()

    for i in threads:
        i.join()
