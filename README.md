# volume-control-computer-vision
# Volume Control

Volume control is a computer vision project that lets you control the volume of your computer with hand gestures through the computer lens. 
Tutorial help: `freeCodeCamp.org`

## Getting Started

Clone this repository to your local machine: 

   > Run `git clone https://github.com/arun-k-shrestha/volume-control-computer-vision.git`

## Setup

This project requires three important packages: OpenCv, Mediapipe, and osascript (for mac users)/ pycaw(for windows users)

Setup for Mac.

1. Install pip3 for mac. Documentation for pip: https://pip.pypa.io/en/stable/getting-started/

2. Install OpenCv through pip3:
   > Run `pip3 install opencv-python`

3. Install Mediapipe:
   > Run `pip3 install mediapipe`

4. Install Osascript:
   > Run `pip3 install osascript`

## Packages Information

1. OpenCv: An open source library that provides a real-time optimized Computer Vision tools/algorithms and hardware. Documentation: https://docs.opencv.org/master/index.html

2. Mediapipe: A cross-platform framework for building multimodal applied machine learning pipelines. This project uses the mediapipe's hand guesture detection. Documentation: https://github.com/google/mediapipe

3. Osascript (Open Scripting Architecture Scripting Language): An architecture that allows you to run scripts from the command line (such as AppleScript or JavaScript).

## How it Works

`VolumeControl.py` is the main file to run. `Module.py` contains helper functions from opencv and mediapipe packages.

UI includes a window with camera image. Play something on your computer, changing the distance between your index finger and thumb changes the volume.

## Common Errors

Few lines of code might not run on Windows. 

If you run into trouble, please don't hesitate to send me a message.
