import bpy
import re

prefix = "submesh_"
suffix = "_LOD_"
lodvalues = [1, 2, 4, 8]

meshindex = int(0)
lodindex = int(0)

def namedefaultlod():
    for meshindex, obj in enumerate(bpy.context.selected_objects, 1):
        bpy.context.view_layer.objects.active = obj
        obj.name = prefix + str.format('{meshindex:02d}') + suffix + lodvalues[lodindex]

def createnewlod():
    for obj in bpy.context.selected_objects:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.duplicate()
        tempindex = int(re.search(r"(?<={prefix})\d+(?={suffix})"))
        objcount = range(len(bpy.context.selected_objects))
        obj.name = prefix + (tempindex + meshindex) + suffix + lodvalues[(lodindex)]

namedefaultlod()
for i in range(3):
    createnewlod()
