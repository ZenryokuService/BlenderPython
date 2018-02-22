# Property names of Add-on 
bl_info = {
    "name": "ZxTool",
    "category": "Object",
}

# Write Script
import bpy

# Override Operator
class ZsRoot(bpy.types.Operator):
    """ This is used as Tool Tip """
    bl_idname = "zst.root" 
    bl_label = "ZenryokuServiceTools"
    bl_option = {'REGISTER', 'UNDO'}
    
    # Called by Blender
    def execute(self, context):
        print('Hello World')
        return {'FINISHED'}
    
    def register():
        print('Register')
    
    def unregister():
        print('Unregister')
    
    
    if __name__ == '__main__':
        register()
