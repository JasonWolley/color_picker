import maya.cmds as cmds
import maya.OpenMaya as om


# Functions for the buttons created in color_picker_ui.py

def apply_color(color, view_check, out_check, shape_check, trans_check):
    srgb_to_linear = lambda x: x / 12.92 if x < 0.04045 else ((x + 0.055) / 1.055) ** 2.4
    lin_color = [srgb_to_linear(i) for i in color]
    # Get transform and shapes of selected objects
    sel_trans = cmds.ls(sl = True, l=True, o=True)
    sel_shape = cmds.listRelatives(sel_trans, f=True, s=True)
    if not sel_trans:
        om.MGlobal.displayWarning("No objects selected. Please select one or more.")
    elif view_check and shape_check:
        for obj_shape in sel_shape:
            cmds.setAttr(obj_shape+'.overrideEnabled',1)
            cmds.setAttr(obj_shape+'.overrideRGBColors',1)
            cmds.setAttr(obj_shape+'.overrideColorRGB',lin_color[0],lin_color[1],lin_color[2])
            for obj_trans in sel_trans:
                cmds.setAttr(obj_trans+'.overrideEnabled',0)
    elif view_check and trans_check:
        for obj_trans in sel_trans:
            cmds.setAttr(obj_trans+'.overrideEnabled',1)
            cmds.setAttr(obj_trans+'.overrideRGBColors',1)
            cmds.setAttr(obj_trans+'.overrideColorRGB',lin_color[0],lin_color[1],lin_color[2])
            for obj_shape in sel_shape:
                cmds.setAttr(obj_shape+'.overrideEnabled',0)
    elif out_check and shape_check:
        for obj_shape in sel_shape:
            cmds.setAttr(obj_shape+'.useOutlinerColor', 1)
            cmds.setAttr(obj_shape+'.outlinerColor', lin_color[0], lin_color[1], lin_color[2])
            for obj_trans in sel_trans:
                cmds.setAttr(obj_trans+'.overrideEnabled',0)
        cmds.select(cl=1)
        cmds.select(sel_trans)
    elif out_check and trans_check:
        for obj_trans in sel_trans:
            cmds.setAttr(obj_trans+'.useOutlinerColor', 1)
            cmds.setAttr(obj_trans+'.outlinerColor', lin_color[0], lin_color[1], lin_color[2])
            for obj_shape in sel_shape:
                cmds.setAttr(obj_shape+'.overrideEnabled',0)
        cmds.select(cl=1)
        cmds.select(sel_trans)


def restore_default():
    sel_trans = cmds.ls(sl = True, l=True, o=True)
    sel_shape = cmds.listRelatives(sel_trans, f=True, s=True)
    if not sel_trans:
        om.MGlobal.displayWarning("No objects selected. Please select one or more.")
    elif sel_trans:
        for any_obj in sel_trans:
            cmds.setAttr(any_obj+'.overrideEnabled',0)
            cmds.setAttr(any_obj+'.useOutlinerColor', 0)
        for any_obj in sel_shape:
            cmds.setAttr(any_obj+'.overrideEnabled',0)
            cmds.setAttr(any_obj+'.useOutlinerColor', 0)
        cmds.select(cl=1)
        cmds.select(sel_trans)


    