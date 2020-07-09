import maya.cmds as cmds
import maya.OpenMaya as om


# Functions for applying selected color to the transform or shape
# nodes in viewport and/or outliner. Called from color_picker_ui.py

def apply_color(color, view_check, out_check, shape_check, trans_check):
    srgb_to_linear = lambda x: x / 12.92 if x < 0.04045 else (
                    (x + 0.055) / 1.055) ** 2.4
    lin_color = [srgb_to_linear(i) for i in color]
    # Get transform and shapes of selected objects
    sel_trans = cmds.ls(sl = True, l=True, o=True)
    sel_shape = cmds.listRelatives(sel_trans, f=True, s=True)
    if not sel_trans:
        om.MGlobal.displayWarning(
            "No objects selected. Please select one or more."
            )

    elif view_check or out_check:
        if view_check:
            if shape_check:
                for obj_shape in sel_shape:
                    viewport_override(obj_shape, sel_trans, lin_color)
            if trans_check:
                for obj_trans in sel_trans:
                    viewport_override(obj_trans, sel_shape, lin_color)
        if out_check:
            if shape_check:
                for obj_shape in sel_shape:
                    outliner_override(obj_shape, sel_trans, lin_color)
            if trans_check:
                for obj_trans in sel_trans:
                    outliner_override(obj_trans, sel_shape, lin_color)
            cmds.select(cl=1)
            cmds.select(sel_trans)


def viewport_override(obj_type, opposite_type, lin_color):
    cmds.setAttr(obj_type+'.overrideEnabled',1)
    cmds.setAttr(obj_type+'.overrideRGBColors',1)
    cmds.setAttr(obj_type+'.overrideColorRGB',
                 lin_color[0],lin_color[1],lin_color[2])
    for obj in opposite_type:
        cmds.setAttr(obj+'.overrideEnabled',0)


def outliner_override(obj_type, opposite_type, lin_color):
    cmds.setAttr(obj_type+'.useOutlinerColor', 1)
    cmds.setAttr(obj_type+'.outlinerColor',
                 lin_color[0], lin_color[1], lin_color[2])
    for obj in opposite_type:
        cmds.setAttr(obj+'.overrideEnabled',0)


def restore_default():
    sel_trans = cmds.ls(sl = True, l=True, o=True)
    sel_shape = cmds.listRelatives(sel_trans, f=True, s=True)
    if not sel_trans:
        om.MGlobal.displayWarning(
            "No objects selected. Please select one or more."
            )
    elif sel_trans:
        for any_obj in sel_trans:
            cmds.setAttr(any_obj+'.overrideEnabled',0)
            cmds.setAttr(any_obj+'.useOutlinerColor', 0)
        for any_obj in sel_shape:
            cmds.setAttr(any_obj+'.overrideEnabled',0)
            cmds.setAttr(any_obj+'.useOutlinerColor', 0)
        cmds.select(cl=1)
        cmds.select(sel_trans)


    