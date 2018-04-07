import os
import bpy

file = os.path.abspath('/Users/takk/BlenderPython/img/Dojo.png')

print(os.path.basename(file))
print([{'name':os.path.basename(file)}])

bpy.ops.import_image.to_plane(
    use_shadeless=True
    ,[{'name':os.path.basename(file)}]
    ,directory=os.path.dirname(file)
)
