import bpy

# Settings
name = 'Gridtastic'
rows = 5
columns = 10
size = 1

# Utility functions
def vert(column, row):
    print('""" Create a single vert """')
    print((column * size, row * size, 0))
    return (column * size, row * size, 0)


def face(column, row):
    print('""" Create a single face """')
    print((column* rows + row,
            (column + 1) * rows + row,
            (column + 1) * rows + 1 + row,
            column * rows + 1 + row))
    
    return (column* rows + row,
            (column + 1) * rows + row,
            (column + 1) * rows + 1 + row,
            column * rows + 1 + row)

# Looping to create the grid
verts = [(-1,-1,0), (1,-1,0), (1,1,0), (-1,1,0)]
faces = [(0,1,2,3)]

# Create Mesh Datablock
mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts, [0,0,1], faces)

# Create Object and link to scene
obj = bpy.data.objects.new(name, mesh)
bpy.context.scene.objects.link(obj)

# Select the object
bpy.context.scene.objects.active = obj
obj.select = True