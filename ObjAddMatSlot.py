#Copyright 2020, Erik Jastad, All rights reserved.
#This script will assign a new material and slot to every object (mat name is obj name)
import bpy

for obj in bpy.data.objects:
    if obj.type == "MESH":
        mat = bpy.data.materials.new(name=obj.name)
        obj.data.materials.append(mat)