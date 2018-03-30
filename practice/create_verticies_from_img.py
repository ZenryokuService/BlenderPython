import os, sys, numpy as np
import bpy, bmesh

sys.path.append("/usr/local/lib/python3.6/site-packages/")

import cv2

imgPath = "/yourFolder/BlenderPython/img/kamon/mouri-motonari-kamon.png"

im = cv2.imread(imgPath,0)
thresh = cv2.Canny(im, 100, 200)
x = 0
y = 0
list = []
pickupFlg = False
addListFlg = True
centerFlg = False
tmp = 0

bpy.ops.object.editmode_toggle()

def judge(col, tmp):
    pickupFlg = (not col == tmp)
    tmp = col
    return pickupFlg

def isAddList(addListFlg, pickUpFlg, row, index):
#    pickUpFlg = judge(row[index],tmp)
    if pickUpFlg and addListFlg:
        addListFlg = judge(row[index + 1], tmp)
    return pickUpFlg

print_size = 2
x_mag = print_size / len(thresh)
y_mag = print_size / len(thresh[0])
first_x = 0
first_y = 0

for row in thresh:
    for col in row:
        pickupFlg = judge(col,tmp)
        addListFlg = isAddList(addListFlg, pickupFlg, row, x)
        if pickupFlg:
            if addListFlg:
                first_x = x * x_mag
                first_y = -(y * y_mag)
                list.append((first_x 
                            ,first_y, 0))
            addListFlg = not addListFlg
        x += 1
    x = 0
    y += 1
 
#print(list)
ob = bpy.context.object

bpy.ops.object.mode_set(mode='EDIT')
bm = bmesh.from_edit_mesh(ob.data)

print(len(list))
print(list[0])

for co in list:
    bm.verts.new(co)

bmesh.update_edit_mesh(ob.data)
#bpy.ops.object.mode_set(mode='OBJECT')

