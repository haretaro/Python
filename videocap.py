#! /usr/bin/python2.7
#-*-coding:utf-8-*-

#OS X でOpenCV使って動画撮るスクリプト
import cv2

filename = 'output.avi'
fps = 30
frames = 300


cap = cv2.VideoCapture(0)
fourcc = cv2.cv.CV_FOURCC('m','p','4','v')#OS X だとmp4v以外はうまく動かないっぽい
width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
size = width, height
writer = cv2.VideoWriter(filename, fourcc, fps, size, True)
i = 0
while(cap.isOpened() and i < frames):
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow('frame',frame)
        i += 1
cap.release()
writer.release()
