import matplotlib.pyplot as plt
import numpy as np


x_values = np.linspace(0, 10)
y_values = np.linspace(0, 10)

plt.plot(x_values, y_values, color = 'red')
plt.plot()
plt.title('Graph y = x.')
#plt.xlim(-100, 100)
#plt.ylim(-100, 100)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

