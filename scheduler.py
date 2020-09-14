import time
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)


class Scheduler:
    def __init__(self, step):
        self.sch = []
        self.st = step

    def run(self):
        while True:
            for i in range(len(self.sch)):
                tmp = self.sch[i]
                tmp[2] += self.st
                if tmp[2] >= tmp[1]:
                    tmp[0]()
                    tmp[2] = 0
            time.sleep(self.st)

    def subscribe(self, funcname, sleeptime):
        self.sch.append([funcname, sleeptime, sleeptime + 1])


def f1():
    print("I Am Groot")


def f2():
    print("I Am Batman")


s = Scheduler(int(os.getenv('RUN_INTERVAL', 5)))
s.subscribe(f1, 3)
s.subscribe(f2, 12)
s.run()
