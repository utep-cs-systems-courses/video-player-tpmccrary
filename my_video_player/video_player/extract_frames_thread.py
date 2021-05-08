from video_player.producer_consumer_queue import ProducerConsumerQueue
import cv2
import os
from threading import Thread, Lock, Semaphore
from typing import Any, Callable, Iterable, List, Mapping, Optional



class ExtractFrames(Thread):

    def __init__(self, outputDir: str, clipFileName: str, producerConsumerQ: ProducerConsumerQueue) -> None:
        super().__init__()

        self.outputDir: str = outputDir
        self.clipFileName: str = clipFileName
        self.frameCount: int = 0
        self.producerConsumerQ: ProducerConsumerQueue = producerConsumerQ

    
    def run(self) -> None:
        # Get the video clip.
        vidcap = cv2.VideoCapture(self.clipFileName)
    
        success, image = vidcap.read()
        print(f'Reading frame {self.frameCount} {success}')

        # Go through all 72 frames
        while success and self.frameCount < 72:            
            
            success,image = vidcap.read()
            print(f'Reading frame {self.frameCount}')

            self.producerConsumerQ.insert(image)   

            self.frameCount += 1
        
        # self.producerConsumerQ.insert(None)




