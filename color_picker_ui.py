# The file color_picker.py creates a window with two tabs.
# Each tab is a QGridLayout populated with QPushButtons
# that represent individual swatches for selection.
# Maya Colors tab contains typically used colors.
# Custom Colors tab has swatch buttons that can be
# customized with colors chosen in colorEditor.
# If running for the first time, local file defaults.py
# will be read and populate colors of Maya Colors tab
# and create white ("blank") Custom Color buttons.
# During first time loading the tool, a buttons.json
# file is written to record colors of all button swatches
# and each time a button color is updated in the Custom Colors
# tab, the button.json file is updated to reflect the new
# list of custom colors. On subsequent loads of the tool,
# the window will read from buttons.json if present instead
# of the defaults.py file.


from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from shiboken2 import wrapInstance

from maya import OpenMayaUI
from maya import cmds
import json

# For importing local related files.
import os
from .ui import main
from . import functions
from . import defaults

# Directory path for local python file imports.
DIR_PATH = os.path.dirname(__file__)


def get_main_window():
    mainwindow_ptr = OpenMayaUI.MQtUtil.mainWindow()
    mainwindow_widget = wrapInstance(long(mainwindow_ptr),
                                     QtWidgets.QWidget)
    return mainwindow_widget


def load_color_picker_tool():
    window = ColorPickerWindow()      
    for entry in QtWidgets.QApplication.allWidgets():
        if entry is not window and entry.objectName() == window.objectName():
            entry.close()
    window.show()
    window.raise_()


class UiColorPickerWidget(QtWidgets.QWidget, main.Ui_color_picker_ui):

    def __init__(self, *args):
        super(UiColorPickerWidget, self).__init__(*args)
        self.material_design_buttons = []
        self.custom_buttons = []
        self.maya_index_buttons = []
        self.setupUi(self)
        self.build_buttons()
        self.on_tab_change()
        self.tabs.currentChanged.connect(self.on_tab_change)
        self.color_button.clicked.connect(self.on_set_color)
        self.default_button.clicked.connect(self.on_restore_default)
        self.viewport_box.stateChanged.connect(self.update_viewport_box)
        self.outliner_box.stateChanged.connect(self.update_outliner_box)
        self.custom_button.clicked.connect(self.on_custom_color_change)
        self.cancel_button.clicked.connect(lambda: self.parent().close())
        self.shape_button.clicked.connect(lambda: self.on_shape_button_click())
        self.transform_button.clicked.connect(lambda: self.on_transform_button_click())
        size = 5    # Adjust tab grid layout size
        self.material_design_tab.setMinimumWidth(8 * size)
        self.material_design_tab.setMinimumHeight(4 * size)

    def update_viewport_box(self):
        viewport_val = self.viewport_box.isChecked()
        outliner_val = self.outliner_box.isChecked()
        if not viewport_val and not outliner_val:
            self.outliner_box.setChecked(True)

    def update_outliner_box(self):
        viewport_val = self.viewport_box.isChecked()
        outliner_val = self.outliner_box.isChecked()
        if not outliner_val and not viewport_val:
            self.viewport_box.setChecked(True)

    def on_custom_color_change(self):
        btn = None
        for button in self.custom_buttons:
            if button.isChecked():
                btn = button
                break
        if btn is None:
            raise RuntimeError(
                "No swatch button selected"
                )
        # Turn off color management temporarily before opening colorEditor
        cmds.colorManagementPrefs(e=True, cme=False)
        color_pick = cmds.colorEditor()
        values = cmds.colorEditor(query=True, rgb=True)
        btn.color = values
        all_buttons = self.update_color_buttons()
        cmds.colorManagementPrefs(e=True, cme=True)

    def update_color_buttons(self):
        # Updates selected swatch button with chosen color
        # after clicking custom_button. This also updates
        # the button.json file to reflect new color list.
        for i in range(self.material_design_gridLayout.count()):
            item = self.material_design_gridLayout.itemAt(i)
            is_child = isinstance(item.widget(), QtWidgets.QPushButton)
            material_design_key = "material_design_colors"
            material_design_list = []
            custom_key = "custom_colors"
            custom_list = []
            maya_index_key = "maya_index_colors"
            maya_index_list = []
            for each in self.material_design_buttons:
                material_design_list.append(each.color)
            for each in self.custom_buttons:
                custom_list.append(each.color)
            for each in self.maya_index_buttons:
                maya_index_list.append(each.color)
            new_vals = dict(
                            material_design_colors=material_design_list,
                            custom_colors=custom_list,
                            maya_index_colors=maya_index_list,
                            )
        json_file = os.path.join(DIR_PATH, "buttons.json")
        if os.path.exists(json_file):
            with open(json_file, "w") as f:
                json.dump(new_vals, f)

    def on_set_color(self):
        color_list = self.material_design_buttons
        if self.tabs.currentWidget() == self.custom_tab:
            print("UNO")
            color_list = self.custom_buttons
        elif self.tabs.currentWidget() == self.maya_index_tab:
            print("DOS")
            color_list = self.maya_index_buttons
        btn = None
        for button in color_list:
            if button.isChecked():
                btn = button
                break
        if btn is None:
            raise RuntimeError("No color button selected")
        chosen_color = btn.color
        self.check_settings(chosen_color)

    # 1 of 2 functions that sends to functions.py
    def on_restore_default(self):
        functions.restore_default()

    # 2 of 2 functions that sends to functions.py
    def check_settings(self, color):
        color = color
        view_check = self.viewport_box.isChecked()
        out_check = self.outliner_box.isChecked()
        shape_check = self.shape_button.isChecked()
        trans_check = self.transform_button.isChecked()
        functions.apply_color(
            color, view_check, out_check,
            shape_check, trans_check,
            )

    def on_tab_change(self, *args):
        self.custom_button.setVisible(
            self.tabs.currentWidget() == self.custom_tab)

    def build_buttons(self):
        # Initialize data
        json_file = os.path.join(DIR_PATH, "buttons.json")
        if os.path.exists(json_file):
            with open(json_file) as f:
                default_colors = json.load(f)
        else:
            # Doesnt exist create default data
            default_colors = defaults.color_defaults()

            with open(json_file, "w") as f:
                json.dump(default_colors, f)
        for tab_name, color_defaults in default_colors.items():
            make_buttons = self.grid_generation(color_defaults, tab_name)

    def grid_generation(self, button_colors, tab_name):
        # Creates a gridLayout of 4 rows and 8 columns 
        # and puts a button in each grid space. 32 buttons. 
        tab_name = tab_name
        colors = button_colors
        row = 0
        for clr, color in enumerate(colors):
            column = clr % 8
            button = CreateButton(color)
            if tab_name == "custom_colors":
                self.custom_gridLayout.addWidget(button, row, column)
                self.custom_buttons.append(button)
            elif tab_name == "material_design_colors":
                self.material_design_gridLayout.addWidget(button, row, column)
                self.material_design_buttons.append(button)
            elif tab_name == "maya_index_colors":
                self.maya_index_gridLayout.addWidget(button, row, column)
                self.maya_index_buttons.append(button)

            else:
                print("Error in grid_generation")
            if column == 7:
                row += 1

    # These last two exist solely to fix issue with non-exclusivity 
    # breaking down after any color button is pressed
    def on_shape_button_click(self):
        self.transform_button.setChecked(False)

    def on_transform_button_click(self):
        self.shape_button.setChecked(False)


class CreateButton(QtWidgets.QPushButton):

    def __init__(self, color, parent=None):
        QtWidgets.QPushButton.__init__(self, parent=parent)
        self.color = color
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding,
            )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setText("")
        self.setCheckable(True)
        self.setAutoExclusive(True)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        q_color = QtGui.QColor.fromRgbF(*color)
        self.setStyleSheet("""
               QPushButton{{
                    background-color: {color};
                }}
               QPushButton::hover{{
                    background-color: {color}; 
                    border: 3px solid black; 
                    border-radius: 20px;
                }}
               QPushButton::pressed{{
                    background-color: {color}; 
                    border: 3px solid white; 
                    border-radius: 20px;
                }}
               QPushButton::checked{{
               color: {color}; background-color: {color}; 
               border: 3px solid white; 
               border-radius: 20px;
               }}""".format(color=q_color.name()))


class ColorPickerWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ColorPickerWindow, self).__init__()
        self.main_widget = UiColorPickerWidget()
        self.setParent(get_main_window())
        self.setWindowFlags(QtCore.Qt.Window)
        self.setProperty("saveWindowPref", True)
        self.setWindowTitle("Color Picker")
        self.setObjectName("colorPicker_window")
        self.setCentralWidget(self.main_widget)

