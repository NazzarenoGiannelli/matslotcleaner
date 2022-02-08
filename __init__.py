bl_info = {
'name': 'MatSlotCleaner',
'author': 'Nazzareno Giannelli',
'version': (1, 1),
'blender': (2, 81, 1),
'location': 'View3D > Object > MatSlotCleaner',
'description': 'Remove unused material slots from all selected meshes at once',
'wiki_url': 'https://nazzarenogiannelli.github.io/',
'tracker_url': '',
'category': '3D View'}

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)

class OBJECT_OT_matslotcleaner(Operator):
    bl_label = 'MatSlotCleaner'
    bl_idname = 'object.matslotcleaner'
    bl_description = 'Remove unused material slots from all selected meshes at once'
    bl_space_type = 'VIEW_3D'
    bl_region_type= 'UI'
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        selected = bpy.context.selected_objects

        for obj in selected:
            if(obj.type=='MESH'):
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.material_slot_remove_unused()
            
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_matslotcleaner.bl_idname)
    
def register():
    bpy.utils.register_class(OBJECT_OT_matslotcleaner)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_matslotcleaner)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
