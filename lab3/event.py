from threading import enumerate, Event, Thread, Condition


class Master(Thread):
    def __init__(self, max_work, condition):
        Thread.__init__(self, name = "Master")
        self.max_work = max_work
        # self.work_available = work_available
        # self.result_available = result_available
        self.condition = condition

    def set_worker(self, worker):
        self.worker = worker
    
    def run(self):
        for i in range(self.max_work):
            # generate work
            self.work = i
            # notify worker
            # self.work_available.set()
            with self.condition:
                self.condition.notify()
            # get result
            with self.condition:
                self.condition.wait()
            # self.result_available.wait()
            # self.result_available.clear()
            if self.get_work() + 1 != self.worker.get_result():
                print ("oops")
            print ("%d -> %d" % (self.work, self.worker.get_result()))
    
    def get_work(self):
        return self.work

class Worker(Thread):
    def __init__(self, terminate, condition):
        Thread.__init__(self, name = "Worker")
        self.terminate = terminate
        self.condition = condition
        # self.work_available = work_available
        # self.result_available = result_available

    def set_master(self, master):
        self.master = master
    
    def run(self):
        while(True):
            # wait work
            with self.condition:
                self.condition.wait()
            # self.work_available.wait()
            # self.work_available.clear()
            if(terminate.is_set()): break
            # generate result
            self.result = self.master.get_work() + 1
            # notify master

            with self.condition:
                self.condition.notify()
            # self.result_available.set()
    
    def get_result(self):
        return self.result

if __name__ ==  "__main__":
    # create shared objects
    terminate = Event()
    work_available = Event()
    result_available = Event()
    condition = Condition()
    
    # start worker and master
    w = Worker(terminate, condition)
    m = Master(10, condition)
    w.set_master(m)
    m.set_worker(w)
    w.start()
    m.start()

    # wait for master
    m.join()

    # wait for worker
    terminate.set()
    # work_available.set()
    with condition:
        condition.notify()
    w.join()

    # print running threads for verification
    print(enumerate())

