import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-1, 1)
y_values = []
for x in x_values:
    y_values.append(x**2)

plt.plot(x_values, y_values)
plt.show()