import pandas as pd
import matplotlib.pyplot as plt


table = pd.read_csv('glass.csv')
div = table.columns[:-1]
Explode = [0, 0, 0, 0, 1, 0, 0, 0, 0]
values = []
for elem in div:
    values.append(table[elem].mean())
print(values)
plt.pie(values, labels = div, shadow = True, startangle = 45)
plt.legend(title= 'Name of elements.')
plt.show()