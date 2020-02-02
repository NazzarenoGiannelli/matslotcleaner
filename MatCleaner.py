bl_info = {
'name': 'MatCleaner',
'author': 'Nazzareno Giannelli',
'version': (1, 0),
'blender': (2, 81, 1),
'location': 'View3D > Object',
'description': 'Delete unused materials from all selected meshes at once',
'wiki_url': '',
'tracker_url': '',
'category': '3D View'}

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)

class OBJECT_OT_matcleaner(Operator):
    bl_label = 'MatCleaner'
    bl_idname = 'object.matcleaner'
    bl_description = 'Delete unused materials from all selected meshes at once'
    bl_space_type = 'VIEW_3D'
    bl_region_type= 'UI'
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        selected = bpy.context.selected_objects

        for s in selected:
            bpy.context.view_layer.objects.active = s
            bpy.ops.object.material_slot_remove_unused()
            
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_matcleaner.bl_idname)
    
def register():
    bpy.utils.register_class(OBJECT_OT_matcleaner)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_matcleaner)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
if __name__ == '__main__':
    register()