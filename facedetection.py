import cv2

cascade_path = '/usr/local/Cellar/opencv/2.4.12_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'

cascade = cv2.CascadeClassifier(cascade_path)

def detect(img,color=(255,0,0)):
    #img_gray = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(60,60))
    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
    return img

def get_face_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(60,60))

    max = 0
    maxh = 0
    maxw = 0
    resx = 0
    resy = 0
    if len(facerect) < 1:
        return None
    for (x,y,w,h) in facerect:
        if max<w*h:
            maxw = w
            maxh = h
            resx = x
            resy = y
            max = w*h
    return img[resy:resy+maxh, resx:resx+maxw]
