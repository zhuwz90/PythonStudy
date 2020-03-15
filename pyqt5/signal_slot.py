import random
import string
import sys
from time import sleep
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication
import threading


class SerialPort(QObject):
    msgReceived = pyqtSignal(str)

    def __init__(self):
        super(SerialPort, self).__init__()
        print("Create a %s object" % self.__class__.__name__)

    def receiveMsg(self):
        s = string.ascii_letters
        lst = []
        for i in range(random.randint(1, 52)):
            lst.append(random.choice(s))

        msg = ''.join(lst)
        print("%s receive a msg: %s" % (threading.current_thread().getName(), msg))

        self.msgReceived.emit("SIGNAL from %s :: msg[%s]" % (threading.current_thread().getName(), msg))

    def simulationWork(self):
        while True:
            self.receiveMsg()
            sleep(2)

        print("%s exit" % (threading.current_thread().getName()))


class Display(QObject):
    def __init__(self):
        super(Display, self).__init__()
        print("Create a %s object" % self.__class__.__name__)
        self.sp = SerialPort()
        self.sp.msgReceived.connect(self.showMsg)
        self.workThread = threading.Thread(target=self.sp.simulationWork, daemon=True)

    def showMsg(self, msg):
        print("%s display in %s" % (msg, threading.current_thread().getName()))

    def start(self):
        # self.sp.simulationWork()

        self.workThread.start()
        # self.workThread.join()

def main():
    app = QApplication(sys.argv)
    demo = Display()
    demo.start()
    sys.exit(app.exec_())
    print("%s exit" % (threading.current_thread().getName()))

if __name__ == '__main__':
    main()