# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Walter\Desktop\color_picker\resource\main.ui'
#
# Created: Fri May 22 12:45:08 2020
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_color_picker_ui(object):
    def setupUi(self, color_picker_ui):
        color_picker_ui.setObjectName("color_picker_ui")
        color_picker_ui.resize(452, 396)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(color_picker_ui.sizePolicy().hasHeightForWidth())
        color_picker_ui.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(color_picker_ui)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabs = QtWidgets.QTabWidget(color_picker_ui)
        self.tabs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setStyleSheet("QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"border: 2px solid #C4C4C3;\n"
"border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 35ex;\n"
"padding: 2px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: #9B9B9B;\n"
"border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 4px; /* make non-selected tabs look smaller */color: gray;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"/* expand/overlap to the left and right by 4px */font: bold; color: green;\n"
"margin-left: -4px;\n"
"margin-right: -4px;\n"
"}\n"
"QTabBar::tab:first:selected {\n"
"margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"QTabBar::tab:last:selected {\n"
"margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"QTabBar::tab:only-one {\n"
"margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
"}\n"
"\n"
" QTabWidget::pane\n"
" {\n"
"     border-top: 1px solid gray;\n"
"     border-left: 1px solid gray;\n"
"     border-right: 1px solid gray;\n"
"     border-bottom: 1px solid gray;\n"
" }\n"
"\n"
"\n"
"")
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setIconSize(QtCore.QSize(14, 14))
        self.tabs.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabs.setObjectName("tabs")
        self.maya_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maya_tab.sizePolicy().hasHeightForWidth())
        self.maya_tab.setSizePolicy(sizePolicy)
        self.maya_tab.setCursor(QtCore.Qt.ArrowCursor)
        self.maya_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maya_tab.setAutoFillBackground(False)
        self.maya_tab.setObjectName("maya_tab")
        self.maya_gridLayout = QtWidgets.QGridLayout(self.maya_tab)
        self.maya_gridLayout.setSpacing(0)
        self.maya_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.maya_gridLayout.setObjectName("maya_gridLayout")
        self.tabs.addTab(self.maya_tab, "")
        self.custom_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_tab.sizePolicy().hasHeightForWidth())
        self.custom_tab.setSizePolicy(sizePolicy)
        self.custom_tab.setObjectName("custom_tab")
        self.custom_gridLayout = QtWidgets.QGridLayout(self.custom_tab)
        self.custom_gridLayout.setSpacing(0)
        self.custom_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.custom_gridLayout.setObjectName("custom_gridLayout")
        self.tabs.addTab(self.custom_tab, "")
        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_2 = QtWidgets.QFrame(color_picker_ui)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.color_check_layout = QtWidgets.QVBoxLayout()
        self.color_check_layout.setObjectName("color_check_layout")
        self.color_label = QtWidgets.QLabel(color_picker_ui)
        self.color_label.setObjectName("color_label")
        self.color_check_layout.addWidget(self.color_label)
        self.viewport_box = QtWidgets.QCheckBox(color_picker_ui)
        self.viewport_box.setChecked(True)
        self.viewport_box.setObjectName("viewport_box")
        self.color_check_layout.addWidget(self.viewport_box)
        self.outliner_box = QtWidgets.QCheckBox(color_picker_ui)
        self.outliner_box.setObjectName("outliner_box")
        self.color_check_layout.addWidget(self.outliner_box)
        self.horizontalLayout.addLayout(self.color_check_layout)
        spacerItem1 = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.vertical_line = QtWidgets.QFrame(color_picker_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vertical_line.sizePolicy().hasHeightForWidth())
        self.vertical_line.setSizePolicy(sizePolicy)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line.setObjectName("vertical_line")
        self.horizontalLayout.addWidget(self.vertical_line)
        spacerItem2 = QtWidgets.QSpacerItem(12, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.override_check_layout = QtWidgets.QVBoxLayout()
        self.override_check_layout.setObjectName("override_check_layout")
        self.override_label = QtWidgets.QLabel(color_picker_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.override_label.sizePolicy().hasHeightForWidth())
        self.override_label.setSizePolicy(sizePolicy)
        self.override_label.setObjectName("override_label")
        self.override_check_layout.addWidget(self.override_label)
        self.shape_button = QtWidgets.QRadioButton(color_picker_ui)
        self.shape_button.setChecked(True)
        self.shape_button.setAutoRepeat(True)
        self.shape_button.setObjectName("shape_button")
        self.override_check_layout.addWidget(self.shape_button)
        self.transform_button = QtWidgets.QRadioButton(color_picker_ui)
        self.transform_button.setAutoRepeat(True)
        self.transform_button.setObjectName("transform_button")
        self.override_check_layout.addWidget(self.transform_button)
        self.horizontalLayout.addLayout(self.override_check_layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        self.custom_button = QtWidgets.QPushButton(color_picker_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_button.sizePolicy().hasHeightForWidth())
        self.custom_button.setSizePolicy(sizePolicy)
        self.custom_button.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 3px;\n"
"border-style: solid black;\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 3, stop: 0 #fff, stop: 1 #888\n"
");\n"
"padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.custom_button.setCheckable(False)
        self.custom_button.setObjectName("custom_button")
        self.gridLayout.addWidget(self.custom_button, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(color_picker_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        spacerItem7 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem7)
        self.color_button = QtWidgets.QPushButton(color_picker_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_button.sizePolicy().hasHeightForWidth())
        self.color_button.setSizePolicy(sizePolicy)
        self.color_button.setStyleSheet("")
        self.color_button.setObjectName("color_button")
        self.buttons_layout.addWidget(self.color_button)
        self.default_button = QtWidgets.QPushButton(color_picker_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.default_button.sizePolicy().hasHeightForWidth())
        self.default_button.setSizePolicy(sizePolicy)
        self.default_button.setObjectName("default_button")
        self.buttons_layout.addWidget(self.default_button)
        self.cancel_button = QtWidgets.QPushButton(color_picker_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cancel_button.setObjectName("cancel_button")
        self.buttons_layout.addWidget(self.cancel_button)
        self.gridLayout_2.addLayout(self.buttons_layout, 3, 0, 1, 1)

        self.retranslateUi(color_picker_ui)
        self.tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabs, QtCore.SIGNAL("currentChanged(int)"), self.custom_button.hide)
        QtCore.QObject.connect(self.tabs, QtCore.SIGNAL("currentChanged(int)"), self.custom_button.show)
        QtCore.QMetaObject.connectSlotsByName(color_picker_ui)

    def retranslateUi(self, color_picker_ui):
        color_picker_ui.setWindowTitle(QtWidgets.QApplication.translate("color_picker_ui", "Form", None, -1))
        self.tabs.setTabText(self.tabs.indexOf(self.maya_tab), QtWidgets.QApplication.translate("color_picker_ui", "Maya Colors", None, -1))
        self.tabs.setTabText(self.tabs.indexOf(self.custom_tab), QtWidgets.QApplication.translate("color_picker_ui", "Custom Palette", None, -1))
        self.color_label.setText(QtWidgets.QApplication.translate("color_picker_ui", "Color:", None, -1))
        self.viewport_box.setText(QtWidgets.QApplication.translate("color_picker_ui", "Viewport", None, -1))
        self.outliner_box.setText(QtWidgets.QApplication.translate("color_picker_ui", "Outliner", None, -1))
        self.override_label.setText(QtWidgets.QApplication.translate("color_picker_ui", "Override:", None, -1))
        self.shape_button.setText(QtWidgets.QApplication.translate("color_picker_ui", "Shape", None, -1))
        self.transform_button.setText(QtWidgets.QApplication.translate("color_picker_ui", "Transform", None, -1))
        self.custom_button.setText(QtWidgets.QApplication.translate("color_picker_ui", "Add Custom Color To \n"
"Selected Swatch Above", None, -1))
        self.color_button.setText(QtWidgets.QApplication.translate("color_picker_ui", "Update Color In Scene", None, -1))
        self.default_button.setText(QtWidgets.QApplication.translate("color_picker_ui", "Restore Defaults", None, -1))
        self.cancel_button.setText(QtWidgets.QApplication.translate("color_picker_ui", "Cancel", None, -1))

