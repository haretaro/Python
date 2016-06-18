import sys
from PIL import Image

if len(sys.argv) < 2:
    print('argument needed')

for f in sys.argv[1:]:
    print('resize ',f)
    out = f + '_resized.jpg'
    Image.open(f).resize((52,52)).save(out)
