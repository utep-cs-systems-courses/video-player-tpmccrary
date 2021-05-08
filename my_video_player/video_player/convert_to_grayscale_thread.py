from video_player.producer_consumer_queue import ProducerConsumerQueue
import cv2
import os
import sys
from threading import Thread, Lock, Semaphore
from typing import Any, Callable, Iterable, List, Mapping, Optional



class ConvertToGrayscale(Thread):

    def __init__(self, outputDir: str, clipFileName: str, colorFrameQueue: ProducerConsumerQueue, grayFrameQueue: ProducerConsumerQueue) -> None:
        super().__init__()

        self.outputDir: str = outputDir
        self.clipFileName: str = clipFileName
        self.frameCount: int = 0
        self.colorFrameQueue: ProducerConsumerQueue = colorFrameQueue
        self.grayFrameQueue: ProducerConsumerQueue = grayFrameQueue
        

    
    def run(self) -> None:
        while (self.frameCount < 72):
            
            if (self.colorFrameQueue.qIsEmpty() is False):
                frame = self.colorFrameQueue.remove()

                # if (frame is None):
                #     print("frame is none")
                #     self.grayFrameQueue.insert(None)
                #     break


                # convert the image to grayscale
                grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                self.grayFrameQueue.insert(grayscaleFrame)

                self.frameCount += 1







