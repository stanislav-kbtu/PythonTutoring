import pandas

# .shape(), [_columnname_], [_columname_].value_counts(), to_csv(_filename_), 
# .iloc[rows, columns], .loc[condition statement], .describe()
table = pandas.read_csv('glass.csv')
print(table.loc[(table['Si'] > 72) & (table['Type'] == 4)])
print(table.loc[(table['Si'] > 72) & (table['Type'] == 4)].describe())


