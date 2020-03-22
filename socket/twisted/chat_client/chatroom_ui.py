# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatDialog(object):
    def setupUi(self, ChatDialog):
        ChatDialog.setObjectName("ChatDialog")
        ChatDialog.resize(399, 513)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChatDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEditRecv = QtWidgets.QPlainTextEdit(ChatDialog)
        self.plainTextEditRecv.setReadOnly(True)
        self.plainTextEditRecv.setObjectName("plainTextEditRecv")
        self.verticalLayout.addWidget(self.plainTextEditRecv)
        self.line = QtWidgets.QFrame(ChatDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.plainTextEditSend = QtWidgets.QPlainTextEdit(ChatDialog)
        self.plainTextEditSend.setTabChangesFocus(False)
        self.plainTextEditSend.setObjectName("plainTextEditSend")
        self.verticalLayout.addWidget(self.plainTextEditSend)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(ChatDialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButtonSend = QtWidgets.QPushButton(ChatDialog)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.horizontalLayout.addWidget(self.pushButtonSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(ChatDialog)
        self.pushButton.clicked.connect(ChatDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ChatDialog)

    def retranslateUi(self, ChatDialog):
        _translate = QtCore.QCoreApplication.translate
        ChatDialog.setWindowTitle(_translate("ChatDialog", "ChatRoom"))
        self.pushButton.setText(_translate("ChatDialog", "Close"))
        self.pushButtonSend.setText(_translate("ChatDialog", "Send"))
