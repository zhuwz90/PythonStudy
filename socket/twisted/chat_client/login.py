from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from login_ui import *
import sys
import chatroom


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.initUi()
        self.chatDialog = None

    def initUi(self):
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.labelMsg.clear()

        self.pushButtonLogin.clicked.connect(self.login)

    def login(self):
        self.chatDialog = chatroom.ChatRoomDialog()
        ip = self.lineEditIp.text()
        port = self.spinBox.value()
        self.chatDialog.connectServer(ip, port)
        self.chatDialog.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginDialog()
    login.show()
    sys.exit(app.exec_())
