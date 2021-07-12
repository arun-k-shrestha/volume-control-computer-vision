import cv2
import time
import numpy as np

WIDTH_CAMERA = 1280
HEIGHT_CAMERA = 720

cap = cv2.VideoCapture(0) #id 0
cap.set(3, WIDTH_CAMERA)
cap.set(4, HEIGHT_CAMERA)
PreviousTime = 0

while True:
    success, img = cap.read()

    CurrentTime = time.time()
    fps = 1/(CurrentTime- PreviousTime)
    PreviousTime = CurrentTime

    cv2.putText(img,f'FPS: {int(fps)}', (40,40),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)

    cv2.imshow("Volume Control", img)
    cv2.waitKey(1)


