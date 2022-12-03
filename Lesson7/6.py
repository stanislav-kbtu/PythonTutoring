import matplotlib.pyplot as plt
import numpy as np
import random 

x_values = [random.uniform(0, 1) for i in range(60)]
y_values = [random.uniform(0, 1) for i in range(60)]
sizes = [random.uniform(5, 700) for i in range(60)]
colors = [(np.random.random(), np.random.random(), np.random.random()) for i in range(60)]
plt.scatter(x_values, y_values, s = sizes, color = colors, linewidth= 1, edgecolor='black', alpha = 0.5)
plt.xlim(-0.2, 1.2)
plt.ylim(-0.2, 1.2)
plt.show()