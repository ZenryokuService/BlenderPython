import bpy

name = 'TestPanel'
size = 1
rows = 2
columns = 2

def vert(column, row): return (column * size, row * size, 0)

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

###### for test ############
v = [x for x in range(3)]
print(v)
###### for test2 ############
w = [(x,y) for x in range(3) for y in range(2)]
print(w)
###### for test3 ############
verts_num = [vert(x, y) for x in range(3) for y in range(2)]
faces_num = [face(x, y) for x in range(3 -1) for y in range(2 - 1)]
print('*** verts_num ***')
print(verts_num)
print('*** faces_num ***')
print(faces_num)

