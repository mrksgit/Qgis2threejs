# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis2\python\developing_plugins\Qgis2threejs\demproperties.ui'
#
# Created: Wed Apr 02 16:33:42 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DEMPropertiesWidget(object):
    def setupUi(self, DEMPropertiesWidget):
        DEMPropertiesWidget.setObjectName(_fromUtf8("DEMPropertiesWidget"))
        DEMPropertiesWidget.resize(368, 398)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DEMPropertiesWidget.sizePolicy().hasHeightForWidth())
        DEMPropertiesWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(DEMPropertiesWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.formLayout_DEMLayer = QtGui.QFormLayout()
        self.formLayout_DEMLayer.setObjectName(_fromUtf8("formLayout_DEMLayer"))
        self.label_DEMLayer = QtGui.QLabel(DEMPropertiesWidget)
        self.label_DEMLayer.setObjectName(_fromUtf8("label_DEMLayer"))
        self.formLayout_DEMLayer.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_DEMLayer)
        self.comboBox_DEMLayer = QtGui.QComboBox(DEMPropertiesWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_DEMLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_DEMLayer.setSizePolicy(sizePolicy)
        self.comboBox_DEMLayer.setObjectName(_fromUtf8("comboBox_DEMLayer"))
        self.formLayout_DEMLayer.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_DEMLayer)
        self.verticalLayout_9.addLayout(self.formLayout_DEMLayer)
        self.groupBox_Resampling = QtGui.QGroupBox(DEMPropertiesWidget)
        self.groupBox_Resampling.setObjectName(_fromUtf8("groupBox_Resampling"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_Resampling)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalSlider_Resolution = QtGui.QSlider(self.groupBox_Resampling)
        self.horizontalSlider_Resolution.setEnabled(True)
        self.horizontalSlider_Resolution.setMinimum(1)
        self.horizontalSlider_Resolution.setMaximum(6)
        self.horizontalSlider_Resolution.setSingleStep(1)
        self.horizontalSlider_Resolution.setPageStep(1)
        self.horizontalSlider_Resolution.setProperty("value", 2)
        self.horizontalSlider_Resolution.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Resolution.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider_Resolution.setTickInterval(1)
        self.horizontalSlider_Resolution.setObjectName(_fromUtf8("horizontalSlider_Resolution"))
        self.horizontalLayout.addWidget(self.horizontalSlider_Resolution)
        self.label_Resolution = QtGui.QLabel(self.groupBox_Resampling)
        self.label_Resolution.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Resolution.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Resolution.setObjectName(_fromUtf8("label_Resolution"))
        self.horizontalLayout.addWidget(self.label_Resolution)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_Width = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_Width.setEnabled(True)
        self.lineEdit_Width.setReadOnly(True)
        self.lineEdit_Width.setObjectName(_fromUtf8("lineEdit_Width"))
        self.horizontalLayout_3.addWidget(self.lineEdit_Width)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEdit_Height = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_Height.setEnabled(True)
        self.lineEdit_Height.setReadOnly(True)
        self.lineEdit_Height.setObjectName(_fromUtf8("lineEdit_Height"))
        self.horizontalLayout_3.addWidget(self.lineEdit_Height)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_HRes = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_HRes.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_HRes.sizePolicy().hasHeightForWidth())
        self.lineEdit_HRes.setSizePolicy(sizePolicy)
        self.lineEdit_HRes.setReadOnly(True)
        self.lineEdit_HRes.setObjectName(_fromUtf8("lineEdit_HRes"))
        self.horizontalLayout_4.addWidget(self.lineEdit_HRes)
        self.label_9 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_VRes = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_VRes.setEnabled(True)
        self.lineEdit_VRes.setReadOnly(True)
        self.lineEdit_VRes.setObjectName(_fromUtf8("lineEdit_VRes"))
        self.horizontalLayout_4.addWidget(self.lineEdit_VRes)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.radioButton_Advanced = QtGui.QRadioButton(self.groupBox_Resampling)
        self.radioButton_Advanced.setObjectName(_fromUtf8("radioButton_Advanced"))
        self.gridLayout_2.addWidget(self.radioButton_Advanced, 2, 0, 1, 1)
        self.radioButton_Simple = QtGui.QRadioButton(self.groupBox_Resampling)
        self.radioButton_Simple.setChecked(True)
        self.radioButton_Simple.setObjectName(_fromUtf8("radioButton_Simple"))
        self.gridLayout_2.addWidget(self.radioButton_Simple, 0, 0, 1, 1)
        self.verticalLayout_Advanced = QtGui.QVBoxLayout()
        self.verticalLayout_Advanced.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_Advanced.setObjectName(_fromUtf8("verticalLayout_Advanced"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_11 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.spinBox_Height = QtGui.QSpinBox(self.groupBox_Resampling)
        self.spinBox_Height.setEnabled(False)
        self.spinBox_Height.setMinimum(1)
        self.spinBox_Height.setMaximum(8)
        self.spinBox_Height.setProperty("value", 5)
        self.spinBox_Height.setObjectName(_fromUtf8("spinBox_Height"))
        self.horizontalLayout_5.addWidget(self.spinBox_Height)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_10 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_5.addWidget(self.label_10)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_Focus = QtGui.QLabel(self.groupBox_Resampling)
        self.label_Focus.setObjectName(_fromUtf8("label_Focus"))
        self.horizontalLayout_8.addWidget(self.label_Focus)
        self.toolButton_switchFocusMode = QtGui.QToolButton(self.groupBox_Resampling)
        self.toolButton_switchFocusMode.setEnabled(False)
        self.toolButton_switchFocusMode.setObjectName(_fromUtf8("toolButton_switchFocusMode"))
        self.horizontalLayout_8.addWidget(self.toolButton_switchFocusMode)
        self.toolButton_PointTool = QtGui.QToolButton(self.groupBox_Resampling)
        self.toolButton_PointTool.setObjectName(_fromUtf8("toolButton_PointTool"))
        self.horizontalLayout_8.addWidget(self.toolButton_PointTool)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_xmax = QtGui.QLabel(self.groupBox_Resampling)
        self.label_xmax.setObjectName(_fromUtf8("label_xmax"))
        self.horizontalLayout_6.addWidget(self.label_xmax)
        self.lineEdit_xmax = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_xmax.setEnabled(False)
        self.lineEdit_xmax.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_xmax.setReadOnly(True)
        self.lineEdit_xmax.setObjectName(_fromUtf8("lineEdit_xmax"))
        self.horizontalLayout_6.addWidget(self.lineEdit_xmax)
        self.label_ymax = QtGui.QLabel(self.groupBox_Resampling)
        self.label_ymax.setObjectName(_fromUtf8("label_ymax"))
        self.horizontalLayout_6.addWidget(self.label_ymax)
        self.lineEdit_ymax = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_ymax.setEnabled(False)
        self.lineEdit_ymax.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_ymax.setReadOnly(True)
        self.lineEdit_ymax.setObjectName(_fromUtf8("lineEdit_ymax"))
        self.horizontalLayout_6.addWidget(self.lineEdit_ymax)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_xmin = QtGui.QLabel(self.groupBox_Resampling)
        self.label_xmin.setEnabled(True)
        self.label_xmin.setObjectName(_fromUtf8("label_xmin"))
        self.horizontalLayout_9.addWidget(self.label_xmin)
        self.lineEdit_xmin = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_xmin.setEnabled(False)
        self.lineEdit_xmin.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_xmin.setReadOnly(True)
        self.lineEdit_xmin.setObjectName(_fromUtf8("lineEdit_xmin"))
        self.horizontalLayout_9.addWidget(self.lineEdit_xmin)
        self.label_ymin = QtGui.QLabel(self.groupBox_Resampling)
        self.label_ymin.setObjectName(_fromUtf8("label_ymin"))
        self.horizontalLayout_9.addWidget(self.label_ymin)
        self.lineEdit_ymin = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_ymin.setEnabled(False)
        self.lineEdit_ymin.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_ymin.setReadOnly(True)
        self.lineEdit_ymin.setObjectName(_fromUtf8("lineEdit_ymin"))
        self.horizontalLayout_9.addWidget(self.lineEdit_ymin)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addLayout(self.verticalLayout_Advanced, 3, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_Resampling)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_17 = QtGui.QLabel(DEMPropertiesWidget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_18.addWidget(self.label_17)
        self.spinBox_demtransp = QtGui.QSpinBox(DEMPropertiesWidget)
        self.spinBox_demtransp.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_demtransp.sizePolicy().hasHeightForWidth())
        self.spinBox_demtransp.setSizePolicy(sizePolicy)
        self.spinBox_demtransp.setPrefix(_fromUtf8(""))
        self.spinBox_demtransp.setMinimum(0)
        self.spinBox_demtransp.setMaximum(100)
        self.spinBox_demtransp.setSingleStep(10)
        self.spinBox_demtransp.setProperty("value", 0)
        self.spinBox_demtransp.setObjectName(_fromUtf8("spinBox_demtransp"))
        self.horizontalLayout_18.addWidget(self.spinBox_demtransp)
        self.label_16 = QtGui.QLabel(DEMPropertiesWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_18.addWidget(self.label_16)
        self.spinBox_sidetransp = QtGui.QSpinBox(DEMPropertiesWidget)
        self.spinBox_sidetransp.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_sidetransp.sizePolicy().hasHeightForWidth())
        self.spinBox_sidetransp.setSizePolicy(sizePolicy)
        self.spinBox_sidetransp.setPrefix(_fromUtf8(""))
        self.spinBox_sidetransp.setMinimum(0)
        self.spinBox_sidetransp.setMaximum(100)
        self.spinBox_sidetransp.setSingleStep(10)
        self.spinBox_sidetransp.setProperty("value", 0)
        self.spinBox_sidetransp.setObjectName(_fromUtf8("spinBox_sidetransp"))
        self.horizontalLayout_18.addWidget(self.spinBox_sidetransp)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.retranslateUi(DEMPropertiesWidget)
        QtCore.QMetaObject.connectSlotsByName(DEMPropertiesWidget)

    def retranslateUi(self, DEMPropertiesWidget):
        DEMPropertiesWidget.setWindowTitle(_translate("DEMPropertiesWidget", "Form", None))
        self.label_DEMLayer.setText(_translate("DEMPropertiesWidget", "DEM Layer", None))
        self.groupBox_Resampling.setTitle(_translate("DEMPropertiesWidget", "Resampling", None))
        self.label_Resolution.setText(_translate("DEMPropertiesWidget", "about 200 x 200 px", None))
        self.label_4.setText(_translate("DEMPropertiesWidget", "Columns", None))
        self.label_5.setText(_translate("DEMPropertiesWidget", "Rows", None))
        self.label_8.setText(_translate("DEMPropertiesWidget", "X resolution", None))
        self.label_9.setText(_translate("DEMPropertiesWidget", "Y resolution", None))
        self.radioButton_Advanced.setText(_translate("DEMPropertiesWidget", "Advanced (multiple resolutions)", None))
        self.radioButton_Simple.setText(_translate("DEMPropertiesWidget", "Simple", None))
        self.label_11.setText(_translate("DEMPropertiesWidget", "Quad tree height", None))
        self.label_10.setText(_translate("DEMPropertiesWidget", "Quad size", None))
        self.lineEdit.setText(_translate("DEMPropertiesWidget", "64", None))
        self.label_Focus.setText(_translate("DEMPropertiesWidget", "Focus point", None))
        self.toolButton_switchFocusMode.setText(_translate("DEMPropertiesWidget", "switch selection mode", None))
        self.toolButton_PointTool.setText(_translate("DEMPropertiesWidget", "Get point from map", None))
        self.label_xmax.setText(_translate("DEMPropertiesWidget", "x", None))
        self.label_ymax.setText(_translate("DEMPropertiesWidget", "y", None))
        self.label_xmin.setText(_translate("DEMPropertiesWidget", "xmin", None))
        self.label_ymin.setText(_translate("DEMPropertiesWidget", "ymin", None))
        self.label_17.setText(_translate("DEMPropertiesWidget", "DEM transparency (%)", None))
        self.label_16.setText(_translate("DEMPropertiesWidget", "Sides transparency (%)", None))
