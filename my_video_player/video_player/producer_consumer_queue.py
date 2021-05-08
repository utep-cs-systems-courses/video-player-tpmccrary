from threading import Lock, Semaphore
from typing import List

# Lock for all threads.
queueLock: Lock = Lock()

class ProducerConsumerQueue():
    '''The producer and consumer that handles threads that are trying to access the same information. Namely, a queue with frames from a video clip.
    Counting semaphores are used in order to track the queue and its contents for the threads.
    '''

    def __init__(self, capacity: int) -> None:
        '''Initilalizer for the class.

        Args:
            capacity (int): The capacity of the queue.
        '''

        self.capacity: int = capacity
        # The queue that will hold the frames.
        self.frameQueue: List = list()
        # Counting semaphores. Represents resources with multiplicity.
        self.fullSem: Semaphore = Semaphore(0)
        self.emptySem: Semaphore = Semaphore(self.capacity)   

    def insert(self, frame) -> None:
        '''Inserts a frame into a queue that is shared by threads. Handles the producer consumer problem by using locks and semaphores.

        Args:
            frame (unkown): The frame to insert into the queue.
        '''

        # Using the global lock so all threads use it.
        global queueLock

        # Acquire an empty semaphore since we are taking up one cell. 
        self.emptySem.acquire()
        # Thread acquires the lock since this is a critical section.
        queueLock.acquire()
        # Add the given frame to the queue.
        self.frameQueue.append(frame)
        # Thread releases the lock since we are done with the critical section.
        queueLock.release()
        # We release a full semaphore because we have taken up a cell.
        self.fullSem.release()
        

    def remove(self):
        '''Removes a frame from the queue that is shared by threads. Handles the producer consumer problem by using locks and semaphores.

        Returns:
            unkown: The frame that was removed from the queue.
        '''

        # Using the global lock so all threads use it.
        global queueLock

        # We acquire a full semaphore since we are removing a frame from a cell.
        self.fullSem.acquire()
        # Thread acquires the lock since this is a critical section.
        queueLock.acquire()
        # Remove frame from the queue.
        frame = self.frameQueue.pop(0)
        # Thread releases the lock since we are done with the critical section.
        queueLock.release()
        # Release a empty sempahore since because we have gained a cell.
        self.emptySem.release()
        return frame


    def queueIsEmpty(self) -> bool:
        '''Returns true if the frame queue is empty.

        Returns:
            bool: True if frame is empty, false if it is not.
        '''

        global queueLock

        isEmpty: bool

        # Critical sections since we are checking the queue.
        queueLock.acquire()
        if len(self.frameQueue) == 0:
            isEmpty = True
        else:
            isEmpty = False
        queueLock.release()

        return isEmpty



