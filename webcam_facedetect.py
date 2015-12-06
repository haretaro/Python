from facedetection import detect
import cv2

cap = cv2.VideoCapture(0)
#cap.set(3, 320) #width
#cap.set(4, 180) #height

print('press q to stop')

key = 0
while True:
    if key == ord('q'):
        break
    grabbed, frame = cap.read()
    if not grabbed:
        break
    result = detect(frame)
    #result = cv2.resize(result,(1280,760))
    cv2.imshow('frame',result)
    key = cv2.waitKey(100) & 0xFF
cap.release()
