from facedetection import get_face_image
import cv2

cap = cv2.VideoCapture(0)

print('press q to stop')

key = 0
while True:
    if key == ord('q'):
        break
    grabbed, frame = cap.read()
    if not grabbed:
        break
    result = get_face_image(frame)
    if result is not None:
        cv2.imshow('frame',result)
    key = cv2.waitKey(100) & 0xFF
cap.release()
