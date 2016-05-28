import cv2
import numpy as np

def overlay(dst, src, offset, size):
    offset = offset[1],offset[0]
    src = cv2.resize(src, size)
    offset = list(offset)
    if(offset[0] < 0):
        src = src[-offset[0]:]
        offset[0] = 0
    if(offset[1] < 0):
        src = src[:,-offset[1]:]
        offset[1] = 0
    if(offset[0] + size[1] > dst.shape[0]):
        src = src[: src.shape[0] - (offset[0] + size[1] - dst.shape[0])]
    if(offset[1] + size[0] > dst.shape[1]):
        src = src[:, : src.shape[1] - (offset[1] + size[0] - dst.shape[1])]
    temp = [src[:,:,c] * (src[:,:,3] / 255) + dst[offset[0] : offset[0] + src.shape[0], offset[1] : offset[1] + src.shape[1] , c] * (1.0 - src[:,:,3]/255) for c in range(3)]
    temp = np.asarray(temp,dtype=np.uint8)
    temp = temp.transpose((1,2,0))
    result = dst.copy()
    result[offset[0] : offset[0] + src.shape[0], offset[1] : offset[1] + src.shape[1]] = temp
    return result

if __name__ == '__main__':
    src = cv2.imread('cage.png',-1)#use alpha channel
    dst = cv2.imread('hoge.jpg')
    print(dst.shape)
    result = overlay(dst, src, (40,30), (250,270))
    cv2.imshow('cage',result)
    cv2.waitKey(0)
