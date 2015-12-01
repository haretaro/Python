import os
from fnmatch import fnmatch

imagepath = '.'
print(os.listdir(imagepath))
frames = [f for f in filter(lambda name: fnmatch(name, '*.jpg'),os.listdir(imagepath))]

print(frames)
