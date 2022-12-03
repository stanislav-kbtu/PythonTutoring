import matplotlib.pyplot as plt
import numpy as np

divisions = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
heights = [25, 40, 78, 20, 30, 65, 78]

plt.bar(divisions, heights, color = ['green', 'red', 'orange', 'blue', 'black', 'brown', 'purple'])
plt.title('Weekday Data')
plt.show()