#Copyright 2020, Erik Jastad, All rights reserved.
#This script will remove the materials from everything
import bpy

for material in bpy.data.materials:
    material.user_clear()
    bpy.data.materials.remove(material)