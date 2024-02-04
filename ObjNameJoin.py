#Copyright 2020, Erik Jastad, All rights reserved.
#This script will joins all objects that have a similar name (Skeleton.001 and Skeleton.002, etc, will join together)
import bpy

i = 0

while(i <= (len(bpy.data.objects) - 1)):
    temp = bpy.data.objects[i].name.split(".obj")
    name = temp[0]

    obs = [o for o in bpy.data.objects if o.name.split(".obj")[0] == name]

    # Set the first object in the list as the active object
    if obs:
        bpy.context.view_layer.objects.active = obs[0]

    # Select all objects in the list
    for obj in obs:
        obj.select_set(True)

    # Join the selected objects
    try:
        bpy.ops.object.join()
    except:
        print("Skipping")

    # Update the scene
    bpy.context.view_layer.update()
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    i+=1
