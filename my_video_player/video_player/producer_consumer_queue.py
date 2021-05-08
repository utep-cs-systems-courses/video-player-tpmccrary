from threading import Lock, Semaphore
from typing import List


queueLock: Lock = Lock()

class ProducerConsumerQueue():

    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity 
        self.frameQueue: List = list()
        self.fullSem: Semaphore = Semaphore(0)
        self.emptySem: Semaphore = Semaphore(self.capacity)   

    def insert(self, frame) -> None:
        global queueLock
    
        self.emptySem.acquire()
        queueLock.acquire()
        self.frameQueue.append(frame)
        queueLock.release()
        self.fullSem.release()
        

    def remove(self):
        global queueLock

        self.fullSem.acquire()
        queueLock.acquire()
        frame = self.frameQueue.pop(0)
        queueLock.release()
        self.emptySem.release()
        return frame


    def qIsEmpty(self) -> bool:
        global queueLock

        isEmpty: bool

        queueLock.acquire()
        if len(self.frameQueue) == 0:
            isEmpty = True
        else:
            isEmpty = False
        queueLock.release()

        return isEmpty



