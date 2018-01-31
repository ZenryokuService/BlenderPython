import bpy
import math
from mathutils import Vector 
vertices = [
    Vector((0, -1 / math.sqrt(9), 0)),
    Vector((0.5, 1 / (2 * math.sqrt(3)), 0)),
    Vector((-0.5, 1 / (2 * math.sqrt(3)), 0)),
    Vector((0, 0, math.sqrt(3))),
]
bpy.app.debug = True
print(vertices)
mesh = bpy.data.meshes.new('MyMesh')
mesh.from_pydata(vertices, [], [[0,1,2], [0,1,3], [1,2,3], [2,0,3]])
mesh.update()
obj = bpy.data.objects.new('MyObject',mesh)
bpy.context.scene.objects.link(obj)
