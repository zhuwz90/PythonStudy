import numpy as np
import matplotlib.pyplot as plt


x = np.random.normal(0, 1, 1000)  # 1000个点的x坐标
y = np.random.normal(0, 1, 1000) # 1000个点的y坐标
c = np.random.rand(1000) #1000个颜色
s = np.random.rand(100)*100 #100种大小
plt.scatter(x, y, c=c, s=s,alpha=0.5)
plt.grid(True)
plt.show()