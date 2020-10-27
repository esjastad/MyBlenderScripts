#Copyright 2020, Erik Jastad, All rights reserved.
import bpy

run = True
i = 0

while(run):
    #Check that index is not beyond array length
    if (i <= (len(bpy.data.objects) - 1)):
        #Get the object name
        temp = bpy.data.objects[i].name.split(".obj")
        name = temp[0]
        
        #Get objects with similar name as object name captured above
        obs = [o for o in bpy.data.objects if o.name.split(".obj")[0] == name]        

        #Setup context, active and selected objects to join
        ctx = bpy.context.copy()
        ctx["active_object"] = ctx["object"] = bpy.data.objects[i]
        ctx["selected_objects"] = ctx["selected_editable_objects"] = obs

        #try to join the objects
        try:
            bpy.ops.object.join(ctx)        
        except:
            print("Skipping non mesh object")

        #Increment to next index            
        i += 1
    else:
        run = False    

        
