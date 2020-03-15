# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tips_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TipsDialog(object):
    def setupUi(self, TipsDialog):
        TipsDialog.setObjectName("TipsDialog")
        TipsDialog.resize(349, 132)
        self.verticalLayout = QtWidgets.QVBoxLayout(TipsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(TipsDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(TipsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TipsDialog)
        self.buttonBox.accepted.connect(TipsDialog.accept)
        self.buttonBox.rejected.connect(TipsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TipsDialog)

    def retranslateUi(self, TipsDialog):
        _translate = QtCore.QCoreApplication.translate
        TipsDialog.setWindowTitle(_translate("TipsDialog", "Tips"))
        self.label.setText(_translate("TipsDialog", "TextLabel"))
