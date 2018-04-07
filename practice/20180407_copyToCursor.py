import bpy
from bpy import context

# this scene => in this 3dview
scene = context.scene
# cursor position of circle which red and white stripe
cursor = scene.cursor_location
# object of selected
obj = scene.objects.active

total = 10

for i in range(total):
    obj_new = obj.copy()
    scene.objects.link(obj_new)
    # Now place the objection between the cursor
    # and the active object based on "i"
    factor = i / total
    obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))
    