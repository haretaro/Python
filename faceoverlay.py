#coding:utf-8
import cv2
from overlayImage import overlay
cap = cv2.VideoCapture(0)
#cap.set(3, 800) #width
#cap.set(4, 450) #height
scale = 1.7 #顔の拡大率
faceoffset = 0.05 #顔の上下移動(顔何個分)

cascade_path = '/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_path)
face = cv2.imread('cage.png',-1)

key = 0
while True:
    if key == ord('q'):
        break
    grabbed, frame = cap.read()
    if not grabbed:
        break
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(60,60))
    if len(facerect) > 0:
        for rect in facerect:
            size = tuple(int(x*scale) for x in rect[2:4])
            offset = rect[0:2] - rect[2:4] * ((scale-1)/2)
            offset[1] += size[1] * faceoffset
            offset = tuple(int(x) for x in offset)
            frame = overlay(frame, face, offset, size)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(100) & 0xFF

cap.release()



