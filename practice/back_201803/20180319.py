# Action types, in order to filter the wanted curves if needed
actionTypes = ('location','rotation_euler','rotation_quaternion','scale')

# Get the object from which we want the animation data
obj = bpy.data.objects['Cube']

# If it has some animation
if obj.animation_data:
    # Iterates over the wanted curves
    # The data_path gives the action's type
    for curve in [c for c in obj.animation_data.action.fcurves if c.data_path.endswith( actionTypes )]:
        # The array_index give the corresponding X, Y or Z index of the curve
        print( curve.data_path, curve.array_index )
        for key in curve.keyframe_points:
            # The curve's points has a 'co' vector giving the frame and the value
            print( 'frame: ', key.co[0], ' value: ', key.co[1] )
    pass
else:
    print("no data")