from queue import Queue
from threading import Thread
from time import time
from random import random
q = Queue(maxsize=2)

def waitSeconds():
    randNum = random.randint(1,5)
    print(f"waiting for {randNum} seconds\n")
    time.sleep(randNum)
    print("My wait is done!")

def runQueue(q):
    while True:
        q.get()
        q.task_done()

worker = Thread(target=runQueue,args=(q,))
worker.setDaemon(True)
worker.start()


q.put(waitSeconds)
q.put(waitSeconds)
q.put(waitSeconds)
q.put(waitSeconds)
q.join()