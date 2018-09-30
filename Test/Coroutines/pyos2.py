from queue import Queue

from pyos1 import Task
from pyos3 import SystemCall
from pyos5 import NewTask, KillTask, WaitTask
from echobad import server

class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}
        self.exit_waiting = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def schedule(self, task):
        self.ready.put(task)

    def exit(self, task):
        del self.taskmap[task.tid]
        print("task %d termined" % task.tid)
        for task in self.exit_waiting.pop(task.tid, []):
            self.schedule(task)

    def waitforexit(self, task, waittid):
            if waittid in self.taskmap:
                self.exit_waiting.setdefault(waittid,[]).append(task)
                return True
            else:
                return False

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
                if isinstance(result, SystemCall):
                    result.task = task
                    result.sched = self
                    result.handle()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

class GetTid(SystemCall):
    def handle(self):
        self.task.sendval = self.task.tid
        self.sched.schedule(self.task)

####selfTest####
def foo():
    mytid = yield GetTid()
    # while True:
    for i in range(5):
        print("I'm foo", mytid)
        yield

def bar():
    mytid = yield GetTid()
    # while True:
    for i in range(5):
        print("I'm bar", mytid)
        yield

def main():
    child = yield NewTask(foo())
    # for i in range(5):
    #     yield
    print("waiting for child")
    yield WaitTask(child)
    print("Child done")
    # yield KillTask(child)
    # print("main done")

def alive():
    while True:
        print("I'm alive")
        yield

sched = Scheduler()
# sched.new(foo())
# sched.new(bar())
# sched.new(main())
sched.new(alive())
sched.new(server(45000))
sched.mainloop()
