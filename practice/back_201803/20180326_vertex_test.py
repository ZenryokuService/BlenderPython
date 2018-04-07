import bpy, bmesh

ob = bpy.context.object
bpy.ops.object.mode_set(mode='EDIT')
bm = bmesh.from_edit_mesh(ob.data)

bpy.ops.mesh.select_all(action='DESELECT')

v1 = bm.verts.new((0,0,1))
v1.select = True
v2 = bm.verts.new((1,0,1))
v2.select = True
v3 = bm.verts.new((0,1,1))
v3.select = True

#bpy.ops.mesh.select_all(action='SELECT')
for v in bm.verts:
    if v.co[2] < 1:
        print(v.co)
        v.select = True

bpy.ops.mesh.edge_face_add()

#bm.edges.new((v1, v2))
#bm.edges.new((v2, v3))
#bm.edges.new((v3, v1))

