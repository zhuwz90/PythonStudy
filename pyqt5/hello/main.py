import sys
from PyQt5.QtWidgets import QApplication, QDialog
from hello import *
from tips_ui import *


class TipsDialog(QDialog, Ui_TipsDialog):
    def __init__(self, parent=None):
        super(TipsDialog, self).__init__(parent)
        self.setupUi(self)
        self.label.setText(u"夜深了，请早点休息！")


class MyDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.setupUi(self)

        self.label.setText("Hello, World!")

        self.buttonBox.accepted.connect(self.handleOk)

    def handleOk(self):
        tips = TipsDialog(parent=self)
        tips.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qtDemo = MyDialog()
    qtDemo.show()
    sys.exit(app.exec_())
