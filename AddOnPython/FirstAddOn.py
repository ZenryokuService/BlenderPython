bl_info = {"name": "My Test Addon", "category": "Object"}

def register():
    print("*** Testing ***")
    print(__name__)
    
def unregister():
    print("Goodbye World")


