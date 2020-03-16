from gevent import monkey
monkey.patch_all()
import gevent
import time
import threading
import matplotlib.pyplot as plt
import numpy as np
from random import randrange

'''
2x2 subplot, display real time data
'''

class MyPlot(object):
    '''
    Build a figure with 2x2 subplot
    '''

    def __init__(self, figtitle='Figure', p1title='1', p2title='2', p3title='3',
                 p4title='4'):
        self.fig = plt.figure(figtitle)
        sub_plot = [221, 222, 223, 224]
        self.sub_title = [p1title, p2title, p3title, p4title]
        self.ax = []
        for i in range(len(sub_plot)):
            self.ax.append(self.fig.add_subplot(sub_plot[i]))
        self.fig.subplots_adjust(wspace=0.3, hspace=0.3)  # 设置子图之间的间距
        plt.ion()

        index = np.arange(len(sub_plot))
        data = [([0], [0]) for i in range(len(sub_plot))]
        self.plotdata = dict(zip(index, data))

    def __del__(self):
        plt.ioff()
        plt.show()

    def setPlotStyle(self, index):
        self.ax[index].set_title(self.sub_title[index], fontsize=12)

    def setPlotData(self, index, x, y):
        self.plotdata[index] = (x, y)

    # def updatePlot(self, index, listx=None, listy=None):
    #     if listx is None or listy is None:
    #         return "no data"
    #
    #     if len(listx) != len(listy):
    #         ex = ValueError("listx and listy must have same first dimension")
    #         raise ex
    #
    #     self.ax[index].cla()
    #     self.ax[index].plot(listx, listy)
    #     self.ax[index].set_xlim(min(listx), max(listx))
    #     plt.pause(1)

    def updatePlot(self, index):
        x = self.plotdata[index][0]
        y = self.plotdata[index][1]
        if len(x) != len(y):
            ex = ValueError("x and y must have same first dimension")
            raise ex

        self.ax[index].cla()
        self.ax[index].plot(x, y)
        self.setPlotStyle(index)
        if min(x) < max(x):
            self.ax[index].set_xlim(min(x), max(x))
        plt.pause(0.1)


def setPlot(p):
    print("Thread: %s" % threading.current_thread().getName())
    while True:
        x = np.arange(0, 100, 1)
        y = np.random.normal(loc=1, scale=1, size=100)
        index = randrange(4)
        p.setPlotData(index, x, y)
        time.sleep(1)

def updatePlot(p):
    print("Thread: %s" % threading.current_thread().getName())
    while True:
        try:
            # listx = np.arange(0, 100, 1)
            # listy = np.random.normal(loc=1, scale=1, size=100)
            # index = randrange(4)
            # p.updatePlot(index, listx, listy)

            # x = np.arange(0, 100, 1)
            # y = np.random.normal(loc=1, scale=1, size=100)
            # index = randrange(4)
            # p.setPlotData(index, x, y)
            for i in range(4):
                p.updatePlot(i)
            time.sleep(0.001)
        except Exception:
            break;

p = MyPlot()

# g1 = gevent.spawn(setPlot, p)
# g2 = gevent.spawn(updatePlot, p)
# g1.join()
# g2.join()

t1 = threading.Thread(target=setPlot, args=(p,))
t2 = threading.Thread(target=updatePlot, args=(p,))
t1.start()
t2.start()
t1.join()
t2.join()


