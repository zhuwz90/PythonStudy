from PyQt5.QtCore import QObject, Qt, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QDialog
from chatroom_ui import *
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.python import log
import sys
import threading

log.startLogging(sys.stdout)


class ChatClient(LineReceiver, QObject):
    connectSucceed = pyqtSignal()
    disconnected = pyqtSignal(str)
    msgReceived = pyqtSignal(str)

    def connectionMade(self):
        log.msg("New connection", self.transport.getPeer())
        self.connectSucceed.emit()

    def connectionLost(self, reason):
        print("Connection lost")
        self.disconnected.emit("Connection lost")

    def lineReceived(self, line):
        self.msgReceived.emit(line.decode('utf-8'))
        print("Emit from: ", threading.current_thread().getName())


class ChatFactory(ReconnectingClientFactory, QObject):
    connectFailed = pyqtSignal(str)
    connectSucceed = pyqtSignal()

    def __init__(self):
        super(ChatFactory, self).__init__()
        self.protocol = ChatClient()

    def buildProtocol(self, addr):
        self.connectSucceed.emit()
        return self.protocol

    def clientConnectionFailed(self, connector, reason):
        self.connectFailed.emit("Connect failed")
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)

    def clientConnectionLost(self, connector, reason):
        self.connectFailed.emit("Connect lost")
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def startFactory(self):
        print("Connectting to chat room...")

    def stopFactory(self):
        print("Exit chat room")


class Connect(QThread):
    def __init__(self, cf, ip, port):
        super(Connect, self).__init__()
        self.cf = cf
        self.ip = ip
        self.port = port

    def run(self):
        reactor.connectTCP(self.ip, self.port, self.cf)
        reactor.run()


class ChatRoomDialog(QDialog, Ui_ChatDialog):
    def __init__(self, parent=None):
        super(ChatRoomDialog, self).__init__(parent)
        self.initUi()
        self.cf = ChatFactory()
        self.cf.protocol.disconnected.connect(self.showMsg)
        self.cf.protocol.msgReceived.connect(self.showMsg)
        self.cf.connectFailed.connect(self.showMsg)
        self.cf.connectSucceed.connect(self.setPostEnabled)
        self.conn = None
        print("%s init in: %s" % (self.__class__.__name__, threading.current_thread().getName()))

    def initUi(self):
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint)
        self.plainTextEditSend.setFocus()
        self.pushButtonSend.setDefault(True)
        self.pushButtonSend.setEnabled(False)
        self.pushButtonSend.clicked.connect(self.sendMsg)

    def setPostEnabled(self):
        self.pushButtonSend.setEnabled(True)

    def connectServer(self, ip, port):
        # self.chatThread = threading.Thread(target=self.connect, args=(ip, port))
        # self.chatThread.setDaemon(True)
        # self.chatThread.start()

        self.conn = Connect(self.cf, ip, port)
        self.conn.start()

    def connect(self, ip, port):
        reactor.connectTCP(ip, port, self.cf)
        reactor.run()

    def showMsg(self, msg):
        self.plainTextEditRecv.appendPlainText(msg)

    def closeEvent(self, a0):
        reactor.stop()
        # self.chatThread.join()

    def sendMsg(self):
        msg = self.plainTextEditSend.toPlainText()
        self.cf.protocol.sendLine(msg.encode('utf-8'))
        self.plainTextEditSend.clear()
