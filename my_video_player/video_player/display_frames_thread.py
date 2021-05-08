from video_player.producer_consumer_queue import ProducerConsumerQueue
import cv2
import os
from threading import Thread, Lock, Semaphore
from typing import Any, Callable, Iterable, List, Mapping, Optional



class DisplayFrames(Thread):

    def __init__(self, outputDir: str, clipFileName: str, frameDelay: int, grayFrameQueue: ProducerConsumerQueue) -> None:
        super().__init__()

        self.outputDir: str = outputDir
        self.clipFileName: str = clipFileName
        self.frameDelay = frameDelay
        self.frameCount: int = 0
        self.grayFrameQueue: ProducerConsumerQueue = grayFrameQueue

    
    def run(self) -> None:
        while (self.frameCount < 72):
            
            if (self.grayFrameQueue.qIsEmpty() is False):
                frame = self.grayFrameQueue.remove()

                # if frame is None:
                #     break

                cv2.imshow('Video', frame)

                if cv2.waitKey(self.frameDelay) and 0xFF == ord("q"):
                    break

                self.frameCount += 1

        cv2.destroyAllWindows()
