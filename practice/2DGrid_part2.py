import bpy

name = 'Gridtastic'
rows = 5
columns = 10
size = 1

# Debug Mode ON
bpy.app.debug = True

def vert(column, row):
    return (column * size, row * size, 0)

def face(column, row):
    return (column * row + row
            , (column + 1 ) * rows + row
            , (column + 1 ) * rows + 1 + row
            , column * rows + 1 + row)

verts = [vert(x, y) for x in range(columns) for y in range(rows)]
faces = [face(x, y) for x in range(columns -1) for y in range(rows - 1)]

mesh = bpy.data.meshes.new(name)
mesh.from_pydata(verts, [], faces)

obj = bpy.data.objects.new(name, mesh)
bpy.context.scene.objects.link(obj)
