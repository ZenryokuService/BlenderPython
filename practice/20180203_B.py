import bpy
import math

def point(x, y, z):
    bpy.ops.mesh.primitive_uv_sphere_add(size=spSize, location=(x,y,z))

angle = 0.5
span = 1.2
spSize = 0.5
for x_axis in range(0, 9):
    xValue = x_axis * span
    yValue = angle * (x_axis * span)
    point(xValue, yValue,0)

#select All Spheres
bpy.ops.object.select_by_type(type='MESH')
