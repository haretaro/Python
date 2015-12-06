from PIL import Image
from PIL import ImageFilter
import math
import numpy as np

def binarize(image,threshold=127):
    """画像を2値化する"""
    data = image.getdata()
    binarylist = [int((r+g+b)/3 > threshold) for (r,g,b) in data]
    newimage = Image.new('1',image.size)
    newimage.putdata(binarylist)
    return newimage

def reverse(image):
    """画像を反転する"""
    array = np.asarray(image)
    width,height = image.size
    array.flags.writeable = True
    for i in range(width):
        for j in range(height):
            array[i][j] = array[i][j] + 127
    out = Image.fromarray(np.uint8(array))
    return out

def houghlinetransform(img,div=360):
    """直線のハフ変換
    div : θの分割数"""
    edged = reverse(inputImage.filter(ImageFilter.Find_Edges))
    binimage = binarize(edged)
    data = binimage.getdata()
    counter = {}#直線に乗ったドットの数を保持する辞書.キーは(theta,rho)のタプル
    width,height = img.size
    for x in range(width):
        for y in range(height):
            index = y*row + x
            if(data[index]):
                for theta in [2 * math.pi * k / div for k in range(0,div)]:
                    rho = int(x * 
                    


#hogehoge
