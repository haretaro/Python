#coding: utf-8
#背景差分法でマスク処理して動体を切り出すプログラム
import cv2
import numpy as np

threshold = 40
cap = cv2.VideoCapture(0)

grabbed, base = cap.read()
base = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
prev = base

key = 0
initkey = 0
while True:
    if key == ord('q'):
        break
    if key == ord('i'):
        prev = frame
    if key == 0:
        threshold += 1
        print('threshold={}'.format(threshold))
    if key == 1:
        threshold -= 1
        print('threshold={}'.format(threshold))
    grabbej, frame = cap.read()
    frame = frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not grabbed:
        break
    diff = cv2.absdiff(frame,prev)
    ret, diff = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    mask = diff
    mask = cv2.medianBlur(mask,5)
    operator = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, operator, iterations=4)
    mask = cv2.dilate(mask, operator, iterations=4)

    masked = cv2.bitwise_and(frame, mask)
    cv2.imshow('hogehoge', masked)
    key = cv2.waitKey(100) & 0xFF

cap.release()
print(mask)
