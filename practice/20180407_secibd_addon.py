import bpy
from bpy import context

# Get Current Scene
scene = context.scene

# Get 3D Cursol
cursor = scene.cursor_location

# Get active object (assume we have one)
obj = scene.objects.active

# Now make a new copy object
obj_new = obj.copy()

# The object won't automatically get into a new scene
scene.objects.link(obj_new)

# Now we place the object
obj_new.location = cursor

