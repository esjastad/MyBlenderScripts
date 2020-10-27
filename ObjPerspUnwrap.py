#Copyright 2020, Erik Jastad, All rights reserved.
#This script will UV unwrap all scene objects based on current camera persepctive
import bpy

for obj in bpy.data.objects:
    if obj.type == "MESH":
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.select_all(action= 'SELECT')  

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                        bpy.ops.uv.project_from_view(override , camera_bounds=False, correct_aspect=True, scale_to_bounds=True)

        bpy.ops.object.mode_set(mode = 'OBJECT')