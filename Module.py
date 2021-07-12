import cv2 
import mediapipe as mp
import time
from mediapipe.python import solutions

class handDetector():
    def __init__(self, 
                static_image_mode = False, 
                max_num_hands =2,
                min_detection_confidence = 0.5,
                min_tracking_confidence = 0.5):

        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

  
        self.mpHands =  mp.solutions.hands
        self.hands = self.mpHands.Hands(self.static_image_mode,
                                        self.max_num_hands,
                                        self.min_detection_confidence,
                                        self.min_tracking_confidence )
        self.mpDraw = mp.solutions.drawing_utils
    
    def FindHands(self,img, draw= True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handmrk in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handmrk, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, HandNumber = 0, draw = True):
        lis = []

        if self.results.multi_hand_landmarks:
            Myhand = self.results.multi_hand_landmarks[HandNumber]

            for id, lm in enumerate(Myhand.landmark):
                height, width, channel = img.shape
                center_x, centre_y = int(lm.x*width), int(lm.y*height)
                #print(id, center_x, centre_y)
                lis.append([id, center_x,centre_y])
                if draw:
                    cv2.circle(img, (center_x, centre_y),15, (0,0,255), 10 )

        return lis


def main():

    PreviousTime = 0
    CurrentTime = 0
    VC = cv2.VideoCapture(0) # video object

    detector= handDetector()


    while True:
        success, img = VC.read()
        img = detector.FindHands(img, draw = False)
        lis = detector.findPosition(img, draw = False)
        if len(lis) != 0:
            print(lis[4])

        CurrentTime = time.time() 
        fps = 1/(CurrentTime-PreviousTime)
        PreviousTime = CurrentTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,225), 2)

        cv2.imshow("Image", img)

        cv2.waitKey(1)
    
if __name__== "__main__":
    main()