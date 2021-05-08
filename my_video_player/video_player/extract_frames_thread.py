from video_player.producer_consumer_queue import ProducerConsumerQueue
import cv2
from threading import Thread



class ExtractFrames(Thread):
    '''Based of the code written by Dr. Freudenthal. Extracts frames from a video clip. Extends the Threads class.

    Args:
        Thread (Thread): Extension of thread class
    '''

    def __init__(self, clipFileName: str, maxFrameCount: int, colorFrameQueue: ProducerConsumerQueue) -> None:
        '''Initializer for class.

        Args:
            clipFileName (str): The path and name of the video clip that frames will be extracted from.
            maxFrameCount (int): The maximum number of frames to extract from the video clip.
            colorFrameQueue (ProducerConsumerQueue): The producer consumer queue that will hold the extracted color frames.
        '''

        super().__init__()

        self.clipFileName: str = clipFileName
        self.maxFrameCount: int = maxFrameCount
        self.colorFrameQueue: ProducerConsumerQueue = colorFrameQueue
        self.frameCounter: int = 0

    
    def run(self) -> None:
        '''Override from the Thread class. Extracts frames from a video clip and stores it in a producer consumer queue.
        '''

        # Get the video clip.
        vidcap = cv2.VideoCapture(self.clipFileName)

        # Read the first frame from the clip.
        success, image = vidcap.read()
        print(f'Reading frame {self.frameCounter} {success}')

        # Go through all frames up to the max frame count.
        while success and self.frameCounter < self.maxFrameCount:            
            
            success,image = vidcap.read()
            print(f'Reading frame {self.frameCounter}')

            # Insert the frame in the queue.
            self.colorFrameQueue.insert(image)   

            self.frameCounter += 1
        



