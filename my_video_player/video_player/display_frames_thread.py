from video_player.producer_consumer_queue import ProducerConsumerQueue
import cv2
from threading import Thread


class DisplayFrames(Thread):
    '''Based of the code written by Dr. Freudenthal. Displays the grayscale frames on an x server. Extends the Threads class.

    Args:
        Thread (Thread): Extension of the Thread class.
    '''

    def __init__(self, maxFrameCount: int,  frameDelay: int, grayFrameQueue: ProducerConsumerQueue) -> None:
        '''Initializer for class.

        Args:
            maxFrameCount (int): The maximum number of frames to display.
            frameDelay (int): The delay between the showing of frames (in ms).
            grayFrameQueue (ProducerConsumerQueue): The producer consumer queue that contains the grayscale frames.
        '''

        super().__init__()
        
        self.maxFrameCount: int = maxFrameCount
        self.frameDelay: int = frameDelay
        self.grayFrameQueue: ProducerConsumerQueue = grayFrameQueue
        self.frameCounter: int = 0


    
    def run(self) -> None:
        '''Override from the Thread class. Displays grayscale frames the the grayscale queue.
        '''

        # Keep displaying until we have reached the max number of frames
        while (self.frameCounter < self.maxFrameCount):
            
            # If the grayscale queue is not empyt, display a frame.
            if (self.grayFrameQueue.queueIsEmpty() is False):
                # Remove the frame from the grayscale queue.
                frame = self.grayFrameQueue.remove()

                # Display the frame in a window called "Video"
                cv2.imshow('Video', frame)

                # Wait for 42ms and check if the user wants to quit
                if cv2.waitKey(self.frameDelay) and 0xFF == ord("q"):
                    break

                self.frameCounter += 1

        # Make sure we cleanup the windows, otherwise we might end up with a mess
        cv2.destroyAllWindows()
