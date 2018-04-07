import bpy

size = 4

for k in range(size):
    for j in range(size):
        for i in range(size):
            print('(X: %s,Y: %s,Z: %s)' % (i, j, k))
            bpy.ops.mesh.primitive_cube_add(radius=0.25, location=(i,j,k))
"""
print('*************')
for k in range(3):
    for j in range(3):
        for i in range(3):
            print(i, j, k)
"""