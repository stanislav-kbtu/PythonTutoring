import matplotlib.pyplot as plt
import numpy as np
import random 

x_values = [random.uniform(0, 0.3) for i in range(100)]
y_values = [random.uniform(0, 0.3) for i in range(100)]
plt.scatter(x_values, y_values, color = 'blue', s = 20, label = 'water')

x_values = [random.uniform(0.4, 0.7) for i in range(100)]
y_values = [random.uniform(0, 0.5) for i in range(100)]
plt.scatter(x_values, y_values, color = 'green', s = 20, label = 'tea')

x_values = [random.uniform(0.6, 1.2) for i in range(100)]
y_values = [random.uniform(0, 1) for i in range(100)]
plt.scatter(x_values, y_values, color = 'red', s = 20, label = 'coffee')



plt.title('Matplot scatter plot')
plt.xlim(-0.2, 1.4)
plt.ylim(-0.2, 1.4)
plt.legend()
plt.show()