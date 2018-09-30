from types import *

from pyos3 import SystemCall

class Task(object):
    taskid = 0
    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid
        self.target = target
        self.sendval = None
        self.stack = []
    def run(self):
        while True:
            try:
                result = self.target.send(self.sendval)
                if isinstance(result,SystemCall): return result
                if isinstance(result, GeneratorType):
                    self.stack.append(self.target)
                    self.sendval = None
                    self.target = result
                else:
                    if not self.stack: return
                    self.sendval = result
                    self.target = self.stack.pop()
            except StopIteration:
                if not self.stack: raise
                self.sendval = None
                self.target = self.stack.pop()


