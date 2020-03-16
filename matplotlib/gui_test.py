#!/usr/bin/env python
# coding:utf-8
"""
可用的GUI窗口matplotlib
"""
import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

fullscreen_status = False  # 全屏状态

# 配色主题
thmem_colors = {
    "light": {
        "front_color": "black",
        "background_color": "white"
    },
    "dark": {
        "front_color": "gray",
        "background_color": "black"
    }
}

# 主题
theme = "dark"


# theme = "light"


# ----------------------------------------------------------------------
def drawPic():
    """
    获取GUI界面设置的参数，利用该参数绘制图片
    """

    # 获取GUI界面上的参数
    try:
        sampleCount = int(inputEntry.get())
    except:
        sampleCount = 50
        print('请输入整数')
        inputEntry.delete(0, END)
        inputEntry.insert(0, '50')

    # 清空图像，以使得前后两次绘制的图像不会重叠
    drawPic.figure.clf()

    color = ['b', 'r', 'y', 'g']

    """
    共享x、y轴
    fig, ax = plt.subplots(nrows=2,ncols=2, sharex=True, sharey=True)    
    """

    # 第一行
    drawPic.a = drawPic.figure.add_subplot(211, facecolor=thmem_colors[theme][
        "front_color"])

    ax = drawPic.figure.gca()  # 获取当前的axes
    # ax.spines['right'].set_color('green')
    # ax.spines['top'].set_color('yellow')
    # ax.spines['left'].set_linewidth(5)  # 设置边框线宽
    # ax.spines['left'].set_linestyle('--')  # 设置左边框样式
    # ax.axes.get_xaxis().set_visible(False)  # 隐藏X轴
    # ax.axes.get_yaxis().set_visible(False)  # 隐藏Y轴
    ax.tick_params(colors=thmem_colors[theme]["front_color"])  # 设置颜色

    # 生成随机数
    x = np.random.randint(0, 100, size=sampleCount)
    y = np.random.randint(0, 100, size=sampleCount)

    # 绘制这些随机点的散点图，颜色随机选取
    drawPic.a.scatter(x, y, s=3, color=color[np.random.randint(len(color))])
    drawPic.a.set_title('111: Draw N Random Dot',
                        fontdict={"color": thmem_colors[theme]["front_color"]})

    # 第二行
    drawPic.b = drawPic.figure.add_subplot(212)

    # 生成随机数
    x = np.random.randint(0, 200, size=sampleCount)
    y = np.random.randint(0, 200, size=sampleCount)

    drawPic.b.scatter(x, y, s=3, color=color[np.random.randint(len(color))])
    # drawPic.b.set_title('222: Draw N Random Dot')

    ax = drawPic.figure.gca()  # 获取当前的axes
    ax.tick_params(colors=thmem_colors[theme]["front_color"])  # 设置颜色

    # 显示画布
    drawPic.canvas.show()


# 监听事件
def listen_event():
    """
    鼠标事件 button_press_event / scroll_event / motion_notify_event 的 event 数据类型基本一样
    MPL MouseEvent: xy=(237,274) xydata=(42.75382026272066,42.40207948739251) button=up dblclick=False inaxes=AxesSubplot(0.125,0.53;0.775x0.35)
    dblclick的值:双击为 True,单击为 False
    button 在 button_press_event / scroll_event 事件中不为空,在 motion_notify_event 中为 None,值如下:
    1: 左键
    2: 中间
    3: 右键
    up: 滚轮向上
    down: 滚轮向下
    None: 光标移动事件
    """

    # def on_click(event):
    #     """鼠标点击事件"""
    #     print("on_click event::", event)
    #     drawPic()# 测试

    #
    # def on_scroll(event):
    #     """鼠标滚轮事件"""
    #     print("on_scroll event::", event)
    #
    # def on_motion_notify(event):
    #     """鼠标移动事件"""
    #     print("on_motion_notify event::", event)

    # 测试画布事件
    # 鼠标点击事件
    # click_id = drawPic.figure.canvas.mpl_connect('button_press_event', on_click)
    # print("click_id:", click_id)
    # 鼠标滚轮事件
    # scroll_id = drawPic.figure.canvas.mpl_connect('scroll_event', on_scroll)
    # print("scroll_id:", scroll_id)
    # 鼠标移动事件
    # motion_notify_id = drawPic.figure.canvas.mpl_connect('motion_notify_event', on_motion_notify)
    # print("motion_notify_id:", motion_notify_id)


# 初始化图形
def GUI_init_figure():
    drawPic.figure = Figure(figsize=(6, 5), dpi=100,
                            facecolor=thmem_colors[theme]["background_color"])
    drawPic.canvas = FigureCanvasTkAgg(drawPic.figure, master=root)
    drawPic.canvas.show()
    drawPic.canvas.get_tk_widget().grid(row=0, columnspan=4)
    listen_event()


# 切换主题
def GUI_toggle_theme():
    global theme
    if theme == "light":
        theme = "dark"
    else:
        theme = "light"

    GUI_init_figure()
    drawPic()  # 画图


# 切换全屏
def GUI_toggle_fullscreen(event=None):
    global fullscreen_status
    fullscreen_status = not fullscreen_status
    root.attributes("-fullscreen", fullscreen_status)


if __name__ == '__main__':
    matplotlib.use('TkAgg')
    root = Tk()

    # 在Tk的GUI上放置一个画布，并用.grid()来调整布局
    # GUI_init_figure() # 这里复制了函数里的内容,避免 drawPic 函数中的代码提示不出来
    drawPic.figure = Figure(figsize=(6, 5), dpi=100,
                            facecolor=thmem_colors[theme]["background_color"])
    drawPic.canvas = NavigationToolbar2Tk(drawPic.figure, master=root)
    drawPic.canvas.show()
    drawPic.canvas.get_tk_widget().grid(row=0, columnspan=4)
    listen_event()

    # 放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
    Button(root, text="切换主题", command=GUI_toggle_theme).grid(row=1, column=0)
    Label(root, text='请输入样本数量：').grid(row=1, column=1)
    inputEntry = Entry(root)
    inputEntry.grid(row=1, column=2)
    inputEntry.insert(0, '50')
    Button(root, text='画图', command=drawPic).grid(row=1, column=3)

    # 切换全屏,F11 和 ESC 都可以
    root.bind("<F11>", GUI_toggle_fullscreen)
    root.bind("<Escape>", GUI_toggle_fullscreen)

    # 启动事件循环
    root.mainloop()
