import bpy
##########################################################
# Addon Infomation Difiition
# [Properties]
#    "name": "Example Add-on Preferences",
#    "author": "Your Name Here",
#    "version": (1, 0),
#    "blender": (2, 65, 0),
#    "location": "SpaceBar Search -> Add-on Preferences Example",
#    "description": "Example Add-on",
#    "warning": "",
#    "wiki_url": "",
#    "tracker_url": "",
#    "category": "Object",
##########################################################
bl_info = {
    "name": "Example Add-on Preferences",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "SpaceBar Search -> Add-on Preferences Example",
    "description": "Example Add-on",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object",
}

# First Shakyo: Pattern Basic
import bpy
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty

class ExampleAddonPereference(AddonPreference):
    # this must mutch the add-on name -> use '__packagename__'
    bl_idname = "MyPreference"
    filePath = StringProperty(name="Example File Path",subtype="FILE_PATH")
    number = IntProperty(name="Example Number", default=4)
    boolean = BoolProperty(name="Example Boolean", deafault=False)

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is a Preferences view for our add-on")
        layout.prop(slef, "filePath")
        layout.prop(self, "number")
        layout.prop(self, "boolean")

    class OBJECT_OT_addon_prefs_example(Operator):
        bl_idname="object.addon_prefs_example"
        bl_label = "Add-on Preferences Example"
        bl_option = {'REGISTER', 'UNDO'}
        
        def execute(self, context):
            user_preferences = context.user_preferences
            addon_prefs = user_preferences.addons["MyPreference"].preferences
            info = ("Path %s, Number: %d, Boolean: %r" %
                (addon_prefs.filePath, addon_prefs.number, addon_prefs.boolean))
            self.report({'INFO'}, info)
            print(info)
            return {'FINISHED'}

def register():
    bpy.utils.reguster_class(OBJECT_OT_addon_prefs_example)
    bpy.utils.register_class(ExampleAddonPreferences)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_addon_prefs_example)
    bpy.utils.unregister_class(ExampleAddonPreferences)