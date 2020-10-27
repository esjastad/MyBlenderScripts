#Copyright 2020, Erik Jastad, All rights reserved.
#This script will remove the material slot from every obj
import bpy

for obj in bpy.data.objects:
    if obj.type == "MESH":
        obj.active_material_index = 0
        for i in range(len(obj.material_slots)):
            bpy.ops.object.material_slot_remove({'object': obj})
