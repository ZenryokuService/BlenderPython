import bpy
from bpy.types import Operator, Panel
def main(context):
    for obj in context.scene.objects:
        print(obj)

class SimpleOperator(Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}

class HelloWorldPanel(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(HelloWorldPanel)
    
if __name__== "__main__":
    register()
    # test call
    bpy.ops.object.simple_operator()

