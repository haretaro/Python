import cv2
import numpy as np

def overlay(src, dst, offset, size):
    src = cv2.resize(src, size)
    temp = [src[:,:,c] * (src[:,:,3] / 255) + dst[offset[0] : offset[0] + src.shape[0], offset[1] : offset[1] + src.shape[1] , c] * (1.0 - src[:,:,3]/255) for c in range(3)]
    temp = np.asarray(temp,dtype=np.uint8)
    temp = temp.transpose((1,2,0))
    result = dst.copy()
    result[offset[0] : offset[0] + src.shape[0], offset[1] : offset[1] + src.shape[1]] = temp
    return result

if __name__ == '__main__':
    src = cv2.imread('cage.png',-1)#use alpha channel
    dst = cv2.imread('hoge.jpg')
    result = overlay(src, dst, (20,20), (300,300))
    cv2.imshow('cage',result)
    cv2.waitKey(0)
