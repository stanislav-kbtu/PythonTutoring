import matplotlib.pyplot as plt
import numpy as np
import random 

plt.subplot(221)
x_values = [random.uniform(0.1, 0.5) for i in range(200)]
y_values = [random.uniform(0, 8000) for i in range(200)]
plt.scatter(x_values, y_values, color = 'green')
plt.title('Spring')

plt.subplot(222)

plt.show()