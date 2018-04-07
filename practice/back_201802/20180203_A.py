import bpy
import math

def point(x, y, z):
    bpy.ops.mesh.primitive_uv_sphere_add(size=0.1, location=(x,y,z))
    
point(0,0,0)