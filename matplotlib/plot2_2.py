import matplotlib.pyplot as plt
import numpy as np
import threading
import sys
from random import random, randrange
from time import sleep

'''
绘制2x2的画板
可设置窗口标题和4个子图标题
可更新曲线数据
'''
quit_flag = False  # 退出标志


class Plot2_2(object):
    def __init__(self, wtitle='Figure', p1title='1', p2title='2', p3title='3',
                 p4title='4'):
        self.sub_title = [p1title, p2title, p3title, p4title]
        self.fig, self.ax = plt.subplots(2, 2)
        self.fig.subplots_adjust(wspace=0.3, hspace=0.3)  # 设置子图之间的间距
        self.fig.canvas.set_window_title(wtitle)

        index = np.arange(len(self.sub_title))
        data = [([0], [0]) for i in range(len(self.sub_title))]
        self.plotdata = dict(zip(index, data))

        self.axdict = {0: self.ax[0, 0], 1: self.ax[0, 1], 2: self.ax[1, 0],
                       3: self.ax[1, 1]}

    def showPlot(self):
        plt.show()

    def setPlotStyle(self, index):
        self.axdict[index].set_title(self.sub_title[index], fontsize=12)

    def setPlotData(self, index, x, y):
        self.plotdata[index] = (x, y)

    def updatePlot(self, index, x, y):
        '''
        更新指定子图
        :param index: 子图序号
        :param x: 横轴数据
        :param y: 纵轴数据
        :return:
        '''
        if len(x) != len(y):
            ex = ValueError("x and y must have same first dimension")
            raise ex

        self.axdict[index].cla()
        self.axdict[index].plot(x, y)
        self.setPlotStyle(index)
        if min(x) < max(x):
            self.axdict[index].set_xlim(min(x), max(x))
        plt.draw()
        print("%s end" % sys._getframe().f_code.co_name)


def updatePlot(plot):
    '''
    模拟收到实时数据，更新曲线的操作
    :param plot: 曲线实例
    :return:
    '''
    print("Thread: %s" % threading.current_thread().getName())
    count = 0
    global quit_flag
    print("quit_flag[%s]" % str(quit_flag))
    while True:
        if quit_flag:
            print("quit_flag[%s]" % str(quit_flag))
            break
        count += 1
        print("count#%d" % count)
        x = np.arange(0, 100, 1)
        y = np.random.normal(loc=1, scale=1, size=100)
        index = randrange(4)
        plot.updatePlot(index, x, y)
        sleep(random() * 3)


def main():
    p = Plot2_2()

    t = threading.Thread(target=updatePlot, args=(p,))
    t.start()

    p.showPlot()
    print("plot close")
    global quit_flag
    quit_flag = True

    t.join()
    print("Thread: %s end" % threading.current_thread().getName())


if __name__ == '__main__':
    main()
