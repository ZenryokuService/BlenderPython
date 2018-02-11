import os
import sys
import bpy

sys.path.append('/usr/local/lib/python3.6/site-packages/cv2/')

import cv2

fileName = os.getcwd() + '/BlenderPython/img/Dojo.png'
# this is Normal Loading
#image = cv2.imread(fileName)

# this is GrayScale Loading 
image = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)

# Create Material
mat = bpy.data.materials.new('ImageMat')
# Create Texture
tex = bpy.data.textures.new(fileName, type='IMAGE')
tex.image = bpy.data.images.load(fileName)

# Add material slots
mat.texture_slots.add()
mat.texture_slots[0].texture = tex

obj = bpy.context.scene.objects.active
obj.data.materials.append(mat)