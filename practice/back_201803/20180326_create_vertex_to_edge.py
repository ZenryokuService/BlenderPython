import bpy, bmesh

ob = bpy.context.object
bm = bmesh.from_edit_mesh(ob.data)

vList = []
vList.append((-0.5, -0.5, 0.0))
vList.append((0.5, -0.5, 0.0))
vList.append((0.5, 0.5, 0.0))
vList.append((-0.5, 0.5, 0.0))

i = 0
list = []
for v in bm.verts:
    print(v.co)
    if i >= 4:
        print("*** IN ***")
        bm.verts.new(vList[i-4])
        list.append(v)
    if i -3 == len(vList):
        break
    print(i)
    i = i+1
print(i)
print(len(list))

bm.edges.new((list[0], list[1]))
