# Producer Consumer Lab

For this lab you will implement a trivial producer-consumer system using
python threads where all coordination is managed by counting and binary
semaphores for a system of two producers and two consumers. The producers and
consumers will form a simple rendering pipeline using multiple threads. One
thread will read frames from a file, a second thread will take those frames
and convert them to grayscale, and the third thread will display those
frames. The threads will run concurrently.

In order to run this lab opencv will need to be installed. To install opencv
use the follwing commands (note that ordering is important):

    sudo zypper -n install python3-devel
    sudo zypper -n install ffmpeg ffmpeg-3
    sudo zypper -n install gstreamer gstreamer-devel
    sudo zypper -n install python3-numpy
    sudo pip install --upgrade pip
    sudo pip install opencv-python

## Allowed libraries
The purpose of this lab is to implement and use a producer-consumer system.
Python already has several synchronized bounded buffers and queues available 
as libraries. You *may not* use any of these as they would prevent you from 
demonstrating the knowledge you've gained. The only threading/synchronization
objects or methods you may use are mutexes and semaphores (we suggest using
the threads api).

## File List
### ExtractFrames.py
Extracts a series of frames from the video contained in 'clip.mp4' and saves 
them as jpeg images in sequentially numbered files with the pattern
'frame_xxxx.jpg'.

### ConvertToGrayscale.py
Loads a series for frams from sequentially numbered files with the pattern
'frame_xxxx.jpg', converts the grames to grayscale, and saves them as jpeg
images with the file names 'grayscale_xxxx.jpg'

### DisplayFrames.py
Loads a series of frames sequently from files with the names
'grayscale_xxxx.jpg' and displays them with a 42ms delay.

### ExtractAndDisplay.py
Loads a series of framss from a video contained in 'clip.mp4' and displays 
them with a 42ms delay

## Requirements
* Extract frames from a video file, convert them to grayscale, and display
them in sequence
* You must have three functions
  * One function to extract the frames
  * One function to convert the frames to grayscale
  * One function to display the frames at the original framerate (24fps)
* The functions must each execute within their own python thread
  * The threads will execute concurrently
  * The order threads execute in may not be the same from run to run
* Threads will need to signal that they have completed their task
* Threads must process all frames of the video exactly once
* Frames will be communicated between threads using producer/consumer idioms
  * Producer/consumer qeueus must be bounded at ten frames

Note: You may have ancillary objects and method in order to make you're code easer to understand and implement.

# Running on WSL and WSL2 with an X Server for Windows 10
This program was developed and ran on a Windows machine using Windows Subystem for Linux Ubuntu (WSL). 
In order to successfully run this program using WSL, python3-opencv must be installed on WSL, and an X server must be installed on Windows. 

Note, WSL and WSL2 take different commands since WSL2 is technically being ran in a virtual machine, unlike WSL. 

## Installing python3-opencv
1. To install opencv for WSL run command:
```
sudo apt install python3-opencv
```
2. Ensure install was correct by running Python3 using command:
```
python3
```
3. In Python3 run command:
```
import cv2 as cv
print(cv.__version__)
```
If no erros are displayed, opencv was successfully installed.
## Installing X Server for Windows 10
In order for WSL to display on Windows, an X server must be installed (Windows nor WSL come with an X server).

This program was developed using X410 (X Server 4 Windows 10), however, it is paid. A good free alternative is Xming. 

## Connecting WSL to the X Server
WSL will not have a display set, so we set it in the terminal.

Note: This will have to be done everytime the WSL terminal instance is closed.
1. Launch X410 (or preferred X server for Windows).
2. On the WSL terminal currently being used, export display:
```
export DISPLAY=localhost:0.0 or 
export DISPLAY=127.0.0:0.0
```

WSL should now to able to display on the Windows X server.

## Connecting WSL2 to the X Server
WSL2 will not have a display set, so we set it in the terminal.

Note: This will have to be done everytime the WSL2 terminal instance is closed.
1. Launch X410 (or preferred X server for Windows).
2. For X410, enable the settings "Allow Public Access". This will allow connections to X410 besides the localhost (since WSL2 is being run through a virtual machine it has its own unique IP).
3. On the WSL2 terminal currently being used, export display:
```
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
```

WSL should now to able to display on the Windows X server.


