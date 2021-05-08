from video_player.producer_consumer_queue import ProducerConsumerQueue
import cv2
from threading import Thread


class ConvertToGrayscale(Thread):
    '''Based of the code written by Dr. Freudenthal. Converts frames to grayscale. Extends the Threads class.

    Args:
        Thread (Thread): Extension of the Threads class.
    '''

    def __init__(self, maxFrameCount: int ,colorFrameQueue: ProducerConsumerQueue, grayFrameQueue: ProducerConsumerQueue) -> None:
        '''Initializer for class.

        Args:
            maxFrameCount (int): The maximum number of frames to convert to grayscale.
            colorFrameQueue (ProducerConsumerQueue): The producer consumer queue that holds the colored frames.
            grayFrameQueue (ProducerConsumerQueue): The producer consumer queue that will hold the grayscale frames.
        '''

        super().__init__()

        self.maxFrameCount: int = maxFrameCount
        self.colorFrameQueue: ProducerConsumerQueue = colorFrameQueue
        self.grayFrameQueue: ProducerConsumerQueue = grayFrameQueue
        self.frameCounter: int = 0
    
    def run(self) -> None:
        '''Override from the Thread class. Converts colored frames to grayscale.
        '''

        # Keep trying to convert to grayscale until we have reached the max number of frames.
        while (self.frameCounter < 72):
            
            # If the frame queue is not empty, make the next frame grayscale.
            if (self.colorFrameQueue.queueIsEmpty() is False):
                # Remove the frame from the queue.
                frame = self.colorFrameQueue.remove()

                # convert the image to grayscale
                grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                # Insert the grayscale frame into a new grayscale queue.
                self.grayFrameQueue.insert(grayscaleFrame)

                self.frameCounter += 1


