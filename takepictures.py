import time
import cv2

camera = cv2.VideoCapture(0)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    #print('hogehoge')
    grabbed, frame = camera.read()
    if not grabbed:
        break
    cv2.imshow('frame',frame)
