import pandas as pd
import matplotlib.pyplot as plt
#.groupby('_columnname_')


table = pd.read_csv('glass.csv')

print(table.groupby('Type')['Na'].describe()['max'])
plt.bar(table['Type'].unique(),table.groupby('Type')['Na'].describe()['max'], color = 'orange')
plt.ylabel('Max value of Na.')
plt.xlabel('Type')
plt.show()