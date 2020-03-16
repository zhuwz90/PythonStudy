from time import sleep
from threading import Thread
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


# 实验数据
range_start, range_end, range_step = 0, 1, 0.005
t = np.arange(range_start, range_end, range_step)
s = np.sin(4 * np.pi * t)

fig = plt.figure() # 创建画板
fig.subplots_adjust(bottom=0.2)
ax = fig.add_subplot(111)
ax.plot(t, s, color='r', lw=2)


# 自定义类，用来封装两个按钮的单击事件处理函数
class ButtonHandler:
    def __init__(self):
        self.flag = True
        self.range_s, self.range_e, self.range_step = 0, 1, 0.005

    # 线程函数，用来更新数据并重新绘制图形
    def threadStart(self):
        while self.flag:
            sleep(0.1)
            self.range_s += self.range_step
            self.range_e += self.range_step
            t = np.arange(self.range_s, self.range_e, self.range_step)
            ydata = np.sin(4 * np.pi * t)
            # 更新数据
            # ax.cla()
            ax.plot(t, ydata, color='r', lw=2)
            ax.set_xlim(self.range_s, self.range_e)

            # 重新绘制图形
            plt.draw()

    def Start(self, event):
        self.flag = True
        # 创建并启动新线程
        t = Thread(target=self.threadStart)
        t.start()

    def Stop(self, event):
        self.flag = False


callback = ButtonHandler()
# 创建按钮并设置单击事件处理函数
axprev = plt.axes([0.81, 0.05, 0.1, 0.06])
bprev = Button(axprev, 'Stop')
bprev.on_clicked(callback.Stop)
axnext = plt.axes([0.7, 0.05, 0.1, 0.06])
bnext = Button(axnext, 'Start')
bnext.on_clicked(callback.Start)
plt.show()
