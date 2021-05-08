from video_player.convert_to_grayscale_thread import ConvertToGrayscale
from video_player.display_frames_thread import DisplayFrames
from video_player.extract_frames_thread import ExtractFrames
from video_player.producer_consumer_queue import ProducerConsumerQueue

# Path to the video clip we are extracting the frames from.
clipFileName: str = "test/clip.mp4"
# The capacity of the queue. Not to large or you might run out of memory.
queueCapacity: int = 24
# The number of frames we are extracting from the video clip.
maxFrameCount: int = 72
# How long to wait, in ms, between each frame.
displayFrameDelay: int = 42

def main():
    '''Main method.
    LOGIC:
        1) Create queues that will hold the colored and grayscaled frames.
        2) Initialize the threads that will extract the frames, convert to grayscale, and display the frames.
        3) Start these threads so they are happening concurrently.
        4) One thread will be extracting the frames, one will be converting those frames to grayscale, and the other thread
        will be displaying the grayscale frames, which is all happening at the same time..
    '''
    
    # Initialize the two producer consumer queses that will allow threads to work with the same data.
    # One is for the colored frames, the other is for the grayscale.
    colorFrameQueue: ProducerConsumerQueue = ProducerConsumerQueue(queueCapacity)
    grayFrameQueue: ProducerConsumerQueue = ProducerConsumerQueue(queueCapacity)

    # Initialize the threads that will extract, convert to grayscale, and display the frames.
    frameExtract: ExtractFrames = ExtractFrames(clipFileName, maxFrameCount, colorFrameQueue)
    convertGrayscale: ConvertToGrayscale = ConvertToGrayscale(maxFrameCount, colorFrameQueue, grayFrameQueue)
    displayFrames: DisplayFrames = DisplayFrames(maxFrameCount, displayFrameDelay, grayFrameQueue)

    # Start all three threads.
    frameExtract.start()
    convertGrayscale.start()
    displayFrames.start()


        

if __name__ == '__main__':
    main()