import bpy

size = 5
for k in range(size):
    for j in range(size):
        for i in range(size):
            print('(X: %s,Y: %s,Z: %s)' % (i, j, k))
            bpy.ops.mesh.primitive_cube_add(raaadius=0.25, location=(i,j,k))