import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1
x = np.random.normal(mu, sigma, 10000)
n, bins, patches = plt.hist(x, bins=100, facecolor='g', alpha=0.75)
plt.text(-3, 250, r'$\mu=0,\ \sigma=1$')
plt.grid(True)
plt.show()
