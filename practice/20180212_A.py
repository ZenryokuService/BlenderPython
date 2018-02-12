import bpy
import numpy as np

import sys
sys.path.append('/usr/local/lib/python3.6/site-packages/cv2/')

import cv2


fileName = os.getcwd() + '/BlenderPython/img/images.jpeg'

im = cv2.imread(fileName,0)

thresh = cv2.Canny(im, 100, 200)

cv2.imshow('test', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()