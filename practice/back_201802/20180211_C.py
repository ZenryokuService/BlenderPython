import bpy
import numpy as np
import os
import sys
sys.path.append('/usr/local/lib/python3.6/site-packages/cv2/')
import cv2

fileName = os.getcwd() + '/BlenderPython/img/images.jpeg'

im = cv2.imread(fileName,0)
#imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# this is un usuful couse not flexible threashold
#ret, thresh = cv2.threshold(im, 200, 200, 200)

# this is flexible threashold
#thresh = cv2.adaptiveThreshold(imgray,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#            cv2.THRESH_BINARY,11,2)

# Using Canny
thresh = cv2.Canny(im, 100, 200)



#image, countours, hierarchy = cv2.findContours(
#                    thresh
#                    , cv2.RETR_TREE
#                    , cv2.CHAIN_APPROX_SIMPLE)

#img = cv2.drawContours(image,countours, -1, (0,255,0), 3)

cv2.imshow('test', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()