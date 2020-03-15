#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Game 2048 designed with pyqt5

Author: WenZheng Zhu
Date: 2020.02.23
'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QRect
import sys
import os
import copy
import random


class GameForm(QMainWindow):
    def __init__(self, parent=None):
        super(GameForm, self).__init__(parent)
        self.initUi()
        # 定义各数字的背景颜色
        self.colors = {0: (204, 192, 179), 2: (238, 228, 218), 4: (237, 224, 200),
                       8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
                       64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 207, 114),
                       512: (237, 207, 114), 1024: (237, 207, 114), 2048: (237, 207, 114),
                       4096: (237, 207, 114), 8192: (237, 207, 114), 16384: (237, 207, 114),
                       32768: (237, 207, 114), 65536: (237, 207, 114), 131072: (237, 207, 114),
                       262144: (237, 207, 114), 524288: (237, 207, 114), 1048576: (237, 207, 114),
                       2097152: (237, 207, 114), 4194304: (237, 207, 114),
                       8388608: (237, 207, 114), 16777216: (237, 207, 114),
                       33554432: (237, 207, 114), 67108864: (237, 207, 114),
                       134217728: (237, 207, 114), 268435456: (237, 207, 114),
                       536870912: (237, 207, 114), 1073741824: (237, 207, 114),
                       2147483648: (237, 207, 114), 4294967296: (237, 207, 114),
                       8589934592: (237, 207, 114), 17179869184: (237, 207, 114),
                       34359738368: (237, 207, 114), 68719476736: (237, 207, 114),
                       137438953472: (237, 207, 114), 274877906944: (237, 207, 114),
                       549755813888: (237, 207, 114), 1099511627776: (237, 207, 114),
                       2199023255552: (237, 207, 114), 4398046511104: (237, 207, 114),
                       8796093022208: (237, 207, 114), 17592186044416: (237, 207, 114),
                       35184372088832: (237, 207, 114), 70368744177664: (237, 207, 114),
                       140737488355328: (237, 207, 114), 281474976710656: (237, 207, 114),
                       562949953421312: (237, 207, 114), 1125899906842624: (237, 207, 114),
                       2251799813685248: (237, 207, 114), 4503599627370496: (237, 207, 114),
                       9007199254740992: (237, 207, 114), 18014398509481984: (237, 207, 114),
                       36028797018963968: (237, 207, 114), 72057594037927936: (237, 207, 114)}
        self.initGameData()

    def initUi(self):
        self.setWindowTitle("2048")
        self.resize(505, 720)
        self.setFixedSize(self.width(), self.height())
        self.initGameOpt()

    def initGameOpt(self):
        ''' 初始化游戏配置 '''
        self.lbFont = QFont('SimSun', 12)  # label字体
        self.lgFont = QFont('SimSun', 50)  # Logo字体
        self.nmFont = QFont('SimSun', 36)  # 面板数字字体

    def initGameData(self):
        ''' 初始化游戏数字 '''
        self.data = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        count = 0
        while count < 2:
            row = random.randint(0, len(self.data) - 1)
            col = random.randint(0, len(self.data[0]) - 1)
            if self.data[row][col] != 0:
                continue
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            count += 1

        self.curScore = 0
        self.bstScore = 0
        # 载入最高得分
        if os.path.exists("bestscore.ini"):
            with open("bestscore.ini", "r") as f:
                self.bstScore = int(f.read())

    def paintEvent(self, e):
        ''' 重写绘图事件 '''
        qp = QPainter()
        qp.begin(self)
        self.drawGameGraph(qp)
        qp.end()

    def keyPressEvent(self, e):
        keyCode = e.key()
        ret = False
        if keyCode == Qt.Key_Left:
            ret = self.move("Left")
        elif keyCode == Qt.Key_Right:
            ret = self.move("Right")
        elif keyCode == Qt.Key_Up:
            ret = self.move("Up")
        elif keyCode == Qt.Key_Down:
            ret = self.move("Down")
        else:
            pass

        if ret:
            self.repaint()

    def closeEvent(self, e):
        # 保存最高得分
        with open("bestscore.ini", "w") as f:
            f.write(str(self.bstScore))

    def drawGameGraph(self, qp):
        ''' 绘制游戏图形 '''
        self.drawLog(qp)
        self.drawLabel(qp)
        self.drawScore(qp)
        self.drawBg(qp)
        self.drawTiles(qp)

    def drawScore(self, qp):
        ''' 绘制得分 '''
        qp.setFont(self.lbFont)
        fontsize = self.lbFont.pointSize()
        scoreLabelSize = len(u"SCORE") * fontsize
        bestLabelSize = len(u"BEST") * fontsize
        curScoreBoardMinW = 15 * 2 + scoreLabelSize  # SCORE栏的最小宽度
        bstScoreBoardMinW = 15 * 2 + bestLabelSize  # BEST栏的最小宽度
        curScoreSize = len(str(self.curScore)) * fontsize
        bstScoreSize = len(str(self.bstScore)) * fontsize
        curScoreBoardNedW = 10 + curScoreSize
        bstScoreBoardNedW = 10 + bstScoreSize
        curScoreBoardW = max(curScoreBoardMinW, curScoreBoardNedW)
        bstScoreBoardW = max(bstScoreBoardMinW, bstScoreBoardNedW)
        qp.setBrush(QColor(187, 173, 160))
        qp.setPen(QColor(187, 173, 160))
        qp.drawRect(505 - 15 - bstScoreBoardW, 40, bstScoreBoardW, 50)
        qp.drawRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 40, curScoreBoardW, 50)

        bstLabelRect = QRect(505 - 15 - bstScoreBoardW, 40, bstScoreBoardW, 25)
        bstScoreRect = QRect(505 - 15 - bstScoreBoardW, 65, bstScoreBoardW, 25)
        scoerLabelRect = QRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 40, curScoreBoardW, 25)
        curScoreRect = QRect(505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 65, curScoreBoardW, 25)

        qp.setPen(QColor(238, 228, 218))
        qp.drawText(bstLabelRect, Qt.AlignCenter, u"BEST")
        qp.drawText(scoerLabelRect, Qt.AlignCenter, u"SCORE")

        qp.setPen(QColor(255, 255, 255))
        qp.drawText(bstScoreRect, Qt.AlignCenter, str(self.bstScore))
        qp.drawText(curScoreRect, Qt.AlignCenter, str(self.curScore))

    def drawBg(self, qp):
        ''' 绘制背景图 '''
        col = QColor(187, 173, 160)
        qp.setPen(col)

        qp.setBrush(QColor(187, 173, 160))
        qp.drawRect(15, 150, 475, 475)  # 绘制游戏区域

    def drawLog(self, qp):
        ''' 绘制Logo '''
        qp.setFont(self.lgFont)
        qp.setPen(QColor(27, 220, 55))
        qp.drawText(QRect(10, 0, 150, 150), Qt.AlignCenter, "2048")

    def drawLabel(self, qp):
        ''' 绘制所有标签信息 '''
        qp.setFont(self.lbFont)
        qp.setPen(QColor(119, 110, 101))
        qp.drawText(15, 134, u"合并相同数字，得到2048吧!")
        qp.drawText(15, 660, u"怎么玩:")
        qp.drawText(45, 680, u"用-> <- 上下左右箭头按键来移动方块.")
        qp.drawText(45, 700, u"当两个相同数字的方块碰到一起时，会合成一个!")

    def drawTiles(self, qp):
        ''' 绘制数字背景 '''
        qp.setFont(self.nmFont)
        for row in range(4):
            for col in range(4):
                value = self.data[row][col]
                color = self.colors[value]

                qp.setPen(QColor(*color))
                qp.setBrush(QColor(*color))
                qp.drawRect(30 + col * 115, 165 + row * 115, 100, 100)  # 绘制数字的背景小方块
                size = self.nmFont.pointSize() * len(str(value))  # 获取当前字体下显示数字的长度
                # 根据尺寸调整字体大小
                while size > 100 - 15 * 2:
                    self.nmFont = QFont('SimSun', self.nmFont.pointSize() * 4 // 5)
                    qp.setFont(self.nmFont)
                    size = self.nmFont.pointSize() * len(str(value))  # 获取当前字体下显示数字的长度
                print("[%d][%d]: value[%d] weight: %d" % (row, col, value, size))

                # 显示非0数字
                if value == 2 or value == 4:
                    qp.setPen(QColor(119, 110, 101))  # 设置2和4数字的前景色
                else:
                    qp.setPen(QColor(255, 255, 255))  # 设置其他数字的前景色
                if value != 0:
                    rect = QRect(30 + col * 115, 165 + row * 115, 100, 100)
                    qp.drawText(rect, Qt.AlignCenter, str(value))

    def putTile(self):
        ''' 找到一个空位置（数值为0），并随机填充2或4 '''
        available = []
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                if self.data[row][col] == 0:
                    available.append((row, col))
        if available:
            row, col = available[random.randint(0, len(available) - 1)]
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            return True
        return False

    def merge(self, row):
        ''' 合并一行或一列 '''
        pair = False
        newRow = []
        for i in range(len(row)):
            if pair:
                newRow.append(2 * row[i])
                self.curScore += 2 * row[i]
                pair = False
            else:
                if i + 1 < len(row) and row[i] == row[i + 1]:
                    pair = True
                else:
                    newRow.append(row[i])
        return newRow

    def slideUpDown(self, isUp):
        ''' 上下方向移动数字方格 '''
        numRows = len(self.data)
        numCols = len(self.data[0])
        oldData = copy.deepcopy(self.data)

        for col in range(numCols):
            cvl = []
            for row in range(numRows):
                if self.data[row][col] != 0:
                    cvl.append(self.data[row][col])  # 将列里面的非0元素提取出来

            if len(cvl) >= 2:
                cvl = self.merge(cvl)  # 合并相同数字

            # 根据移动方向填充0
            for i in range(numRows - len(cvl)):
                if isUp:
                    cvl.append(0)
                else:
                    cvl.insert(0, 0)

            print("row=%d" % row)
            row = 0
            for row in range(numRows):
                self.data[row][col] = cvl[row]

        return oldData != self.data

    def slideLeftRight(self, isLeft):
        ''' 左右方向移动数字方格 '''
        numRows = len(self.data)
        numCols = len(self.data[0])
        oldData = copy.deepcopy(self.data)

        for row in range(numRows):
            rvl = []
            for col in range(numCols):
                if self.data[row][col] != 0:
                    rvl.append(self.data[row][col])

            if len(rvl) >= 2:
                rvl = self.merge(rvl)

            for i in range(numCols - len(rvl)):
                if isLeft:
                    rvl.append(0)
                else:
                    rvl.insert(0, 0)

            col = 0
            for col in range(numCols):
                self.data[row][col] = rvl[col]

        return oldData != self.data

    def move(self, direction):
        ''' 移动数字方格 '''
        isMove = False
        if direction == "Up":
            isMove = self.slideUpDown(True)
        elif direction == "Down":
            isMove = self.slideUpDown(False)
        elif direction == "Left":
            isMove = self.slideLeftRight(True)
        elif direction == "Right":
            isMove = self.slideLeftRight(False)
        else:
            pass

        if not isMove:
            return False

        self.putTile()  # 新增一个数字
        if self.curScore > self.bstScore:
            self.bstScore = self.curScore

        if self.isGameOver():
            button = QMessageBox.warning(self, "Warning", u"游戏结束，是否重新开始？",
                                         QMessageBox.Ok | QMessageBox.No,
                                         QMessageBox.Ok)

            if button == QMessageBox.Ok:
                self.initGameOpt()
                bstScore = self.bstScore
                self.initGameData()
                self.bstScore = bstScore
                return True
            else:
                return False
        else:
            return True

    def isGameOver(self):
        ''' 判断游戏是否无法继续 '''
        copyData = copy.deepcopy(self.data)  # 先暂存数据值
        curScore = self.curScore

        flag = False
        if not self.slideUpDown(True) and not self.slideUpDown(False) and \
                not self.slideLeftRight(True) and not self.slideLeftRight(False):
            flag = True  # 全部方向都不能再移动
        self.curScore = curScore
        if not flag:
            self.data = copyData  # 仍可以移动，则恢复原来数据
        return flag


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = GameForm()
    form.show()
    sys.exit(app.exec_())
