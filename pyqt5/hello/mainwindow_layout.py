from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, \
    QSpacerItem, QSizePolicy
from random import randrange
import sys
import os


class Saying(object):
    ''' 生成名人名言 '''

    def __init__(self):
        self.data = None

    def loadData(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                self.data = f.readlines()
            return True
        else:
            return False

    @property
    def sentense(self):
        if self.data is not None:
            index = randrange(0, len(self.data))
            s = self.data[index].split(" ")
            return s[0], s[1]
        else:
            return "No data!"


class SayingForm(QMainWindow):
    ''' 随机输出名人名言 '''

    def __init__(self, parent=None):
        super(SayingForm, self).__init__(parent)
        self.initUi()

        self.say = Saying()
        self.say.loadData("SayingSentence.txt")


    def initUi(self):
        self.resize(640, 320)
        mainWidget = QWidget(self)
        self.btnNext = QPushButton(u"下一条", mainWidget)
        self.labelSaying = QLabel(u"名人名言", mainWidget)
        self.labelSaying.setAlignment(Qt.AlignHCenter | Qt.AlignHCenter)
        self.labelCelebrity = QLabel(u"请点击下一条", mainWidget)
        self.labelCelebrity.setAlignment(Qt.AlignHCenter | Qt.AlignHCenter)

        hLayout = QHBoxLayout()
        space = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hLayout.addItem(space)
        hLayout.addWidget(self.labelCelebrity)

        vLayout = QVBoxLayout(mainWidget)
        vLayout.addWidget(self.labelSaying)
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.btnNext)

        self.setCentralWidget(mainWidget)

        self.btnNext.clicked.connect(self.next)

    def next(self):
        sentense, name = self.say.sentense
        self.labelSaying.setText(sentense)
        self.labelCelebrity.setText(name)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = SayingForm()
    demo.show()

    sys.exit(app.exec_())
