### import OpenCv ###
import os, sys, numpy as np
import bpy, bmesh
sys.path.append("/usr/local/lib/python3.6/site-packages/")

import cv2

imgPath = "/Users/takk/BlenderPython/img/kamon/mouri-motonari-kamon.png"

im = cv2.imread(imgPath,0)
# To GrayScale
#thresh = cv2.Canny(im, 100, 200)
## Setting up for Machine Learning ##########
responses = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Create SVM = Support Vecor Machine -> Name Of Algorithm
svm = cv2.ml.SVM_create()
svm_params = dict( kernel_type = cv2.SVM_LINEAR,
                    svm_type = cv2.SVM_C_SVC,
                    C=2.67, gamma=5.383 )
res = svm.train(im, response, svm_param)
print(res)
cv2.imshow(res)

