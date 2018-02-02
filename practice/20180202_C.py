import bpy
import math

print('*************')

def point(x,y) :
    bpy.ops.mesh.primitive_cube_add(radius=0.25, location=(x,y,0))

size = 15
for ang in range(24):
    rad = math.radians(ang * size);
    x = (math.pi * math.cos(rad));
    y = (math.pi * math.sin(rad));
    point(x,y);

