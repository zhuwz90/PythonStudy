import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt, QRect


class BrushDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('demo')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.penDraw(painter)
        painter.end()

    def penDraw(self, painter):
        # 设置钢笔
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(10, 10, 300, 100)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 4, 54])
        # 当改变钢笔的塑性时要setPen
        painter.setPen(pen)
        painter.drawLine(30, 30, 40, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = BrushDemo()
    sys.exit(app.exec_())
