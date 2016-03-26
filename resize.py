import sys
from PIL import Image

if len(sys.argv) < 2:
    print('argument needed')

f = sys.argv[1]
print('resize ',f)
out = f + '_resized.jpg'
Image.open(f).resize((40,40)).save(out)
