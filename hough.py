from PIL import Image
from PIL import ImageFilter
import imgtools as it
import sys

#inputFile = sys.argv[1]
inputFile = 'lena.jpg'
inputImage = Image.open(inputFile)
edged = inputImage.filter(ImageFilter.FIND_EDGES)
edged = it.reverse(edged)
binimage = it.binarize(edged)
binimage.show()
