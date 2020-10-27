#Copyright 2020, Erik Jastad, All rights reserved.
#This script will change the name of all the objects materials by appending "_mat" to the end of the current name.
import bpy

for ob in bpy.data.objects:
    if ob.type == "MESH":        
        for mat_slot in ob.material_slots:
            bpy.data.materials.get(mat_slot.name).name = bpy.data.materials.get(mat_slot.name).name + "_mat"