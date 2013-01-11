#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

theta = np.linspace(-2 * np.pi, 2 * np.pi, 100)

ax = fig.gca(projection='3d')

x = np.sin(theta)
y = np.cos(theta)

ax.plot(theta, x, y)
ax.legend()

plt.show()