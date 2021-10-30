import cv2
import mediapipe as mp
import numpy as np

mp_droeing = mp.solutions.drawing_utils
mp_pos = mp.solutions.pose
cap = cv2.VideoCapture(0)
#video feed
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('mediapipe feed', frame)

     

    if cv2.waitKey(1) == 27:
        #print frame data
        #print (frame)
        break
cap.release()
cv2.destroyAllwindows()