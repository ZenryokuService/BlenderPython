import os
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages/cv2/')

import cv2

# this is Normal Loading
#image = cv2.imread(os.getcwd() + '/BlenderPython/img/Dojo.png')

# this is GrayScale Loading 
image = cv2.imread(os.getcwd() + '/BlenderPython/img/Dojo.png', cv2.IMREAD_GRAYSCALE)

width = 0
height = 0
channels = 0

print(image.shape)

if image is None:
    print("File is None!")
    sys.exit(1)

if len(image.shape) == 3:
    height, width, channels = image.shape[:3]
else:
    height, width = image.shape[:2]
    channels = 1

print("width; %d" % width)
print("height; %d" % height)
print("channels; %d" % channels)
print("dtype;" + str(image.dtype))
