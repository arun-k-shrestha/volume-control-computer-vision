import cv2
import time
import numpy as np
import Module
import math 
import osascript



WIDTH_CAMERA = 1280
HEIGHT_CAMERA = 720

cap = cv2.VideoCapture(0)
cap.set(3, WIDTH_CAMERA)
cap.set(4, HEIGHT_CAMERA)
PreviousTime = 0

detector = Module.handDetector(min_detection_confidence = 0.7)

while True:
    any_variable, img = cap.read()
    img = detector.FindHands(img,draw= False)
    lis = detector.findPosition(img,draw=False)
    if len(lis) != 0:

        Thumb_X, Thumb_Y = lis[4][1], lis[4][2]
        Index_X, Index_Y = lis[8][1], lis[8][2]

        cv2.circle(img,(Thumb_X,Thumb_Y), 15, (0,0,255), thickness= 10)
        cv2.circle(img,(Index_X,Index_Y), 15, (0,0,255), thickness= 10)
        cv2.line(img, (Thumb_X,Thumb_Y),(Index_X,Index_Y), (0,0,255), 3)

        Length = math.hypot(Index_X - Thumb_X, Index_Y -Thumb_Y)

        Main_Volume = np.interp(Length, [50,300],[0, 100])
        vol = "set volume output volume " + str(Main_Volume)
        osascript.osascript(vol)
        

    CurrentTime = time.time()
    fps = 1/(CurrentTime- PreviousTime)
    PreviousTime = CurrentTime

    cv2.putText(img,f'FPS: {int(fps)}', (40,40),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)

    cv2.imshow("Volume Control", img)
    cv2.waitKey(1)



