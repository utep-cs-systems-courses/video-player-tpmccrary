
from video_player.convert_to_grayscale_thread import ConvertToGrayscale
from video_player.display_frames_thread import DisplayFrames
from video_player.extract_frames_thread import ExtractFrames
from video_player.producer_consumer_queue import ProducerConsumerQueue


outputDir = "frames"
clipFileName = "test/clip.mp4"

def main():
    
    colorFrameQueue: ProducerConsumerQueue = ProducerConsumerQueue(24)
    grayFrameQueue: ProducerConsumerQueue = ProducerConsumerQueue(24)

    frameExtract = ExtractFrames(outputDir, clipFileName, colorFrameQueue)
    convertGrayscale = ConvertToGrayscale(outputDir, clipFileName, colorFrameQueue, grayFrameQueue)
    displayFrames = DisplayFrames(outputDir, clipFileName, 42, grayFrameQueue)

    frameExtract.start()
    convertGrayscale.start()
    displayFrames.start()


        

if __name__ == '__main__':
    main()