import maya.cmds as cmds

# Functions for the buttons created in color_picker_ui.py

def apply_color(color, view_check, out_check, shape_check, trans_check):
    # Get transform and shapes of selected objects
    sel_trans = cmds.ls(sl = True, l=True, o=True)
    sel_shape = cmds.listRelatives(sel_trans, f=True, s=True)
    print("TESSST", color, view_check, out_check, shape_check, trans_check)
    print(sel_trans, sel_shape)
    if view_check and shape_check:
        print("VIEW AND SHAPE")
        for obj_shape in sel_shape:
            cmds.setAttr(obj_shape+'.overrideEnabled',1)
            cmds.setAttr(obj_shape+'.overrideRGBColors',1)
            cmds.setAttr(obj_shape+'.overrideColorRGB',color[0],color[1],color[2])
            for obj_trans in sel_trans:
                cmds.setAttr(obj_trans+'.overrideEnabled',0)
    elif view_check and trans_check:
        print("VIEW AND TRANS")
        for obj_trans in sel_trans:
            cmds.setAttr(obj_trans+'.overrideEnabled',1)
            cmds.setAttr(obj_trans+'.overrideRGBColors',1)
            cmds.setAttr(obj_trans+'.overrideColorRGB',color[0],color[1],color[2])
            for obj_shape in sel_shape:
                cmds.setAttr(obj_shape+'.overrideEnabled',0)
    if out_check and shape_check:
        print("OUT AND SHAPE")
        for obj_shape in sel_shape:
            cmds.setAttr(obj_shape+'.useOutlinerColor', 1)
            cmds.setAttr(obj_shape+'.outlinerColor', color[0], color[1], color[2])
            for obj_trans in sel_trans:
                cmds.setAttr(obj_trans+'.overrideEnabled',0)
        cmds.select(cl=1)
        cmds.select(sel_trans)
    elif out_check and trans_check:
        print("OUT AND TRANS")
        for obj_trans in sel_trans:
            cmds.setAttr(obj_trans+'.useOutlinerColor', 1)
            cmds.setAttr(obj_trans+'.outlinerColor', color[0], color[1], color[2])
            for obj_shape in sel_shape:
                cmds.setAttr(obj_shape+'.overrideEnabled',0)
        cmds.select(cl=1)
        cmds.select(sel_trans)


def restore_default():
    sel_trans = cmds.ls(sl = True, l=True, o=True)
    sel_shape = cmds.listRelatives(sel_trans, f=True, s=True)
    if sel_trans is None:
            raise RuntimeError("No objects selected")
    for any_obj in sel_trans:
        cmds.setAttr(any_obj+'.overrideEnabled',0)
        cmds.setAttr(any_obj+'.useOutlinerColor', 0)
    for any_obj in sel_shape:
        cmds.setAttr(any_obj+'.overrideEnabled',0)
        cmds.setAttr(any_obj+'.useOutlinerColor', 0)
    cmds.select(cl=1)
    cmds.select(sel_trans)


    