#-*-coding:utf-8-*-
#引数の画像中の顔を検出する.
import cv2
import sys

img = cv2.imread(sys.argv[1])

cascade_path = '/usr/local/Cellar/opencv/2.4.12/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_path)
color = (255,128,0)
img_gray = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)

facerect = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1,1))

print( len(facerect))
print(facerect)

if len(facerect) > 0:
    for rect in facerect:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
    cv2.imshow('detection result',img)
    cv2.waitKey(0)
